import numpy as np
import cv2
import os
from glob import glob

def angle_hour(hour, minute):
  t = (hour % 12) + (minute % 60) / 60
  angle = - t * 30
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

  def gen_mask(fname):
    im = cv2.imread(fname, flags=cv2.IMREAD_UNCHANGED)
    mask = np.zeros(im.shape[:2])
    mask[im[:,:,3] > 1] = 1
    return mask

  clock = gen_mask(os.path.join(backdrops_dir, clock_fname))
  hour = gen_mask(os.path.join(backdrops_dir, hour_fname))
  minute = gen_mask(os.path.join(backdrops_dir, minute_fname))

  frames_files = sorted(glob(os.path.join(frames_dir, "*")))
  frames = [cv2.imread(f, flags=cv2.IMREAD_UNCHANGED) for f in frames_files]

  return clock, hour, minute, frames

def merge_alpha(i1, c1, i2, c2):
  nx0, nx1 = c1[1] - c2[1], c1[0] - c2[0]
  tmp = np.zeros(i1.shape)
  tmp[nx0:i2.shape[0]+nx0,nx1:i2.shape[1]+nx1] = i2
  tmp[i1 != 0] = 1
  return tmp
