

import numpy as np

img = np.array([[1, 2], [3, 4]])
stacked_img = np.stack((img,)*3, axis=-1)

print(stacked_img)