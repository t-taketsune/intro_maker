import numpy as np
import cv2
import os
from glob import glob

def angle_hour(hour):
  h = hour % 12
  angle = - h * 30
  return angle

def angle_min(minute):
  m = minute % 60
  angle = - m * 6
  return angle

def rotate_image(image, center, angle):
  rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

def load_assets(
    backdrops_dir='backdrops',
    clock_fname='clock.png',
    hour_fname='hours.png',
    minute_fname='minutes.png',
    frames_dir='frames'
  ):

  clock = cv2.imread(os.path.join(backdrops_dir, clock_fname), flags=cv2.IMREAD_UNCHANGED)
  hour = cv2.imread(os.path.join(backdrops_dir, hour_fname), flags=cv2.IMREAD_UNCHANGED)
  minute = cv2.imread(os.path.join(backdrops_dir, minute_fname), flags=cv2.IMREAD_UNCHANGED)

  frames_files = sorted(glob(os.path.join(frames_dir, "*")))
  frames = [cv2.imread(f, flags=cv2.IMREAD_UNCHANGED) for f in frames_files]

  return clock, hour, minute, frames