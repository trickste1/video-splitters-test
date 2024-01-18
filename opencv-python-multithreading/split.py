import cv2
import os
import time
from multiprocessing import Pool, cpu_count

def split_and_save_frames(video_path, output_folder, fps, thread_id, total_threads):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)

    # Get video properties
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate start and end frame for the current thread
    start_frame = int((thread_id - 1) * total_frames / total_threads)
    end_frame = int(thread_id * total_frames / total_threads)

    # Calculate the interval between frames based on desired fps
    frame_interval = int(video_capture.get(cv2.CAP_PROP_FPS) / fps)

    # Loop through frames and save them
    for frame_number in range(start_frame, end_frame, frame_interval):
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = video_capture.read()
        if not ret:
            break

        # Save the frame as an image
        frame_filename = os.path.join(output_folder, f"frame_{thread_id}_{frame_number}.png")
        cv2.imwrite(frame_filename, frame)

    # Release the video capture object
    video_capture.release()

def multi_run_wrapper(args):
   return split_and_save_frames(*args)

def split_video_into_frames(video_path, output_folder, fps):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Use multithreading to split the video into frames
    cpus = 8
    p = Pool(processes=cpus)
    p.map(multi_run_wrapper, [(video_path, output_folder, fps, i, cpus) for i in range(1, cpus + 1)])

if __name__ == "__main__":
    # Set the path to the input video
    input_video_path = "video.mp4"

    # Set the output folder for frames
    output_frames_folder = "frames"

    # Set the desired frames per second (fps)
    desired_fps = 30

    # Set the number of threads to split the video

    start = time.time()

    # Call the function to split video into frames using multithreading
    split_video_into_frames(input_video_path, output_frames_folder, desired_fps)
    end = time.time()

    print("Frames extracted successfully!")
    print("Time spent in seconds: ", end - start)

