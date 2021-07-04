from PIL import Image
import numpy as np

w, h = 1280, 720
data = np.zeros((h, w, 3), dtype=np.uint8)
data[0:128, 0:128] = [0, 255, 0] # red patch in upper left
img = Image.fromarray(data, 'RGB')
img.save('my.png')
