const ffmpeg = require('fluent-ffmpeg');
const fs = require('fs');
const { promisify } = require('util');

const mkdirAsync = promisify(fs.mkdir);

async function splitVideoToFrames(videoPath, outputFolder, fps) {
  // Use ffmpeg to extract frames
  console.log('Started splitting video')
  console.time('answer time');
  await new Promise((resolve, reject) => {
    ffmpeg(videoPath)
      .outputOptions(`-vf fps=${fps}`)
      .on('end', resolve)
      .on('error', reject)
      .on('data', () => {})
      .save(`${outputFolder}/frame%04d.png`);
  });
  console.log('Time spent:')
  console.timeEnd('answer time');
  console.log('Frames extracted successfully!');
}

async function main() {
  // Set the path to the input video
  const inputVideoPath = 'video.mp4';

  // Set the output folder for frames
  const outputFramesFolder = 'frames';

  // Set the desired frames per second (fps)
  const desiredFps = 30;

  // Create output folder if it doesn't exist
  if (!fs.existsSync(outputFramesFolder)) {
    await mkdirAsync(outputFramesFolder);
  }

  // Run the function to split video into frames
  await splitVideoToFrames(inputVideoPath, outputFramesFolder, desiredFps);
}

main();
