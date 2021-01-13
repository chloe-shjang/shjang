#!/usr/bin/python3

import PIL
import glob
import sys
import os
from PIL import Image, ImageDraw

print("Please present your Directory!!")

x = input()
os.chdir(str(x))

imglist = glob.glob("*.jpg")
img = Image.open(imglist[0])

for img_path in imglist:
	img = Image.open(img_path)
	img.transpose(Image.FLIP_LEFT_RIGHT).save(img_path)
