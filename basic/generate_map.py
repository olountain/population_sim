import numpy as np
from perlin_noise import PerlinNoise

def generate_map(x_dim = 100, y_dim = 100, octaves = 4, translation = -0.1, n_plants = 500):
    noise = PerlinNoise(octaves=4)
    my_map = [[noise([i/x_dim, j/y_dim]) for j in range(x_dim)] for i in range(y_dim)]
    my_map = [[x + translation for x in y] for y in my_map]
    my_map = np.sign(my_map).astype(int)
    
    my_indices = np.where(my_map == 1)
    occupied = [(my_indices[0][i], my_indices[1][i]) for i in range(len(my_indices[0]))]

    my_indices = np.where(my_map == -1)
    unoccupied = [(my_indices[0][i], my_indices[1][i]) for i in range(len(my_indices[0]))]

    plant_ind = np.random.choice(list(range(len(unoccupied))), n_plants, replace = False)
    plants = [unoccupied[i] for i in plant_ind]
    
    return my_map, occupied, plants


## driver
# my_map, occupied, plants = generate_map(x_dim = 100, y_dim = 100, n_plants = 500)

# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# plt.imshow(my_map, cmap=ListedColormap(['green', 'blue']))
# plt.show()




