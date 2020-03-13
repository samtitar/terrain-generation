from __future__ import print_function

from PIL import Image

from os import listdir
from os.path import isfile, join

import cv2
import sys

data_dir = "data/raw/mountains"
result_data_dir = "data/terrain/mountains"

images = [f for f in listdir(data_dir) if isfile(join(data_dir, f))]

num_images = len(images)
progress = 0

for image_path in images:
    try:
        print("\rProgress: {:.2f}%".format(progress / num_images * 100), end="")

        data_path = join(data_dir, image_path)
        new_data_path = join(result_data_dir, ''.join(image_path.split('.')[:-1]) + '.jpg')

        image = cv2.imread(data_path)

        result = Image.fromarray(image)
        result.save(new_data_path)

        progress += 1
    except Exception as e:
        print("Error at image {}".format(progress))
        continue
print()
