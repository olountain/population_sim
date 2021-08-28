import matplotlib.pyplot as plt
import numpy as np
from perlin_noise import PerlinNoise

noise = PerlinNoise(octaves=4)
xpix, ypix = 100, 100
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

# plt.imshow(pic, cmap='gray')
# plt.imshow(pic, cmap=colors.ListedColormap(['white', 'black']))
# plt.show()
translation = -0.1
tmp = [[x + translation for x in y] for y in pic]
tmp = np.sign(tmp).astype(int)

plt.imshow(tmp, cmap=colors.ListedColormap(['green', 'blue']))
plt.show()

my_indices = np.where(tmp == 1)

a = [(my_indices[0][i], my_indices[1][i]) for i in range(len(my_indices[0]))]
a