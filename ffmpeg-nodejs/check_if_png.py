def is_png(file_path):
  with open(file_path, 'rb') as f:
    # PNG file signature (first 8 bytes)
    signature = f.read(8)

  # PNG signature: b'\x89PNG\r\n\x1a\n'
  return signature == b'\x89PNG\r\n\x1a\n'

file_path = "frames/frame0001.png"

if is_png(file_path):
  print("The file is in PNG format.")
else:
  print("The file is not in PNG format.")