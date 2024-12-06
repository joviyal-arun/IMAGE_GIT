# Modules 
import os

import cv2

def read_image(image_path):
  """Reads an image from the specified path.

  Args:
    image_path: The path to the image file.

  Returns:
    The image as a NumPy array.
  """

  img = cv2.imread(image_path)
  if img is None:
    print("Error: Could not read the image.")
    return None
  return img

def process_video(video_path):
  """Processes a video by converting each frame to grayscale.

  Args:
    video_path: The path to the video file.
  """

  cap = cv2.VideoCapture(video_path)

  while True:
    ret, frame = cap.read()

    if not ret:
      break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Video', gray_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  cap.release()
  cv2.destroyAllWindows()
