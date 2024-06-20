import numpy as np
import cv2
import os

def rotate_image(image, angle, center):
  rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

def load_assets(
    backdrops_dir='backdrops',
    clock_fname='clock.png',
    hour_fname='hours.png',
    minute_fname='minutes.png'
  ):

  clock = cv2.imread(os.path.join(backdrops_dir, clock_fname), flags=cv2.IMREAD_UNCHANGED)
  hour = cv2.imread(os.path.join(backdrops_dir, hour_fname), flags=cv2.IMREAD_UNCHANGED)
  minute = cv2.imread(os.path.join(backdrops_dir, minute_fname), flags=cv2.IMREAD_UNCHANGED)

  return clock, hour, minute