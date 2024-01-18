import av
from PIL import Image
import time
from io import BytesIO

input_file = 'video.mp4'
output_pattern = 'frames/frame%04d.png'
desired_fps = 24

container = av.open(input_file)
stream = container.streams.video[0]

# Set the desired fps
stream.rate = desired_fps

start = time.time()
print("Started extracting frames")

for frame in container.decode(video=0):
  image = frame.to_image()
    
  # Convert image to bytes
  image_bytes = BytesIO()
  image.save(image_bytes, format='PNG')
  # Save the image
  with open(output_pattern % frame.index, 'wb') as f:
    f.write(image_bytes.getvalue())

end = time.time()
print("Frames extracted successfully!")
print("Time spent in seconds: ", end - start)
