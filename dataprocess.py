from __future__ import print_function

from PIL import Image

from os import listdir
from os.path import isfile, join

import cv2
import sys

import matplotlib.pyplot as plt

inp_data_dir = "/media/samtitar/Ubuntu Data 2/terrain-selection-tool/data/mountains"
out_data_dir = "data/Terrain/processed/mountains"

images = [f for f in listdir(inp_data_dir) if isfile(join(inp_data_dir, f))]

num_images = len(images)
progress = 0

image_path = images[0]

for image_path in images:
    progress += 1
    try:
        print("\rProgress: {:.2f}%".format(progress / num_images * 100), end="")

        data_path = join(inp_data_dir, image_path)
        new_data_path = join(out_data_dir, ''.join(image_path.split('.')[:-1]) + '.png')

        image = cv2.imread(data_path)
        result = Image.fromarray(image)
        result.save(new_data_path)
    except Exception as e:
        print("\rError at image {}".format(progress))
        continue
print()