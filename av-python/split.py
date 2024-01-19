import os
import av
from io import BytesIO
import math

input_file = 'video.mp4'
output_directory = 'frames'
output_pattern = 'frame%04d.png'
desired_fps = 24

# Create output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

container = av.open(input_file)
video_stream = container.streams.video[0]

# Calculate delay between frames based on the desired frame rate
frameIndexMultiplier = math.ceil(1000 / desired_fps)

for packet in container.demux(video=0):
  for frame in packet.decode():
    # Calculate the time at which this frame should appear
    if frame.index % frameIndexMultiplier != 0:
      continue

    print(frame.index)

    image = frame.to_image()

    # Convert image to bytes
    image_bytes = BytesIO()
    image.save(image_bytes, format='PNG')

    # Save the image
    output_path = os.path.join(output_directory, output_pattern % frame.index)
    with open(output_path, 'wb') as f:
      f.write(image_bytes.getvalue())
