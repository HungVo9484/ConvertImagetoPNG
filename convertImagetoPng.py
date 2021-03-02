#-------------Convert Images to Png--------------
#cmd line: $python3 convertImagetoPng.py folder1/ folder2/

import sys
import os
from PIL import Image

# Get params of the folders
folder1 = sys.argv[1]
folder2 = sys.argv[2]

# Check folder2 exist. If not, to create new folders.
if not os.path.exists(folder2):
    os.makedirs(folder2)

# Loop all the images in the folder1
for filename in os.listdir(folder1):
    try:
        img = Image.open(f'{folder1}{filename}')
        slpit_filename = os.path.splitext(filename)[0]
        img.save(f'{folder2}{slpit_filename}.png', 'png')
    except:
        print(f'file error! {filename}')
        continue
