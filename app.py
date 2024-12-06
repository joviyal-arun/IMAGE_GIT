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