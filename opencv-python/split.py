import cv2
import os
import time

def split_video_to_frames(video_path, output_folder, fps):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    video_capture = cv2.VideoCapture(video_path)

    # Get video properties
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate the interval between frames based on desired fps
    frame_interval = int(video_capture.get(cv2.CAP_PROP_FPS) / fps)

    # Loop through frames and save them
    frame_number_for_name = 0
    for frame_number in range(0, total_frames, frame_interval):
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = video_capture.read()
        if not ret:
            break

        # Save the frame as an image
        frame_filename = os.path.join(output_folder, f"frame_{frame_number_for_name}.png")
        frame_number_for_name = frame_number_for_name + 1
        cv2.imwrite(frame_filename, frame)

    # Release the video capture object
    video_capture.release()

if __name__ == "__main__":
    # Set the path to the input video
    input_video_path = "video.mp4"

    # Set the output folder for frames
    output_frames_folder = "frames"

    # Set the desired frames per second (fps)
    desired_fps = 30

    start = time.time()
    print("Started extracting frames")

    # Call the function to split video into frames
    split_video_to_frames(input_video_path, output_frames_folder, desired_fps)

    end = time.time()
    print("Frames extracted successfully!")
    print("Time spent in seconds: ", end - start)
