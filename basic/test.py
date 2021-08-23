import matplotlib.pyplot as plt
from matplotlib import colors, interactive
from matplotlib import animation
import numpy as np
from sklearn.datasets import make_blobs

## generate terrain
def generate_terrain(dim):
    data = np.zeros((dim,dim))

    tmp = tuple(np.random.randint(20,30, size = 2))
    tmp

    tmp1



data = np.zeros((dim,dim))

centers = [(3, 3), (30,10), (35,40)]
cluster_std = [1.5, 1.5, 3]

for j in range(len(centers)):
    a,b = make_blobs(n_samples=300, cluster_std=cluster_std[j], centers=[centers[j]], n_features=3)
    a = np.round(a).astype(int)
    a = np.unique(a, axis = 0)

    for i in range(len(a)):
        data[tuple(a[i,:])] = 2

cmap = colors.ListedColormap(['white', 'black', 'blue'])
plt.matshow(data, cmap = cmap)
plt.show()