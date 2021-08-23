import matplotlib.pyplot as plt
from matplotlib import colors, interactive
from matplotlib import animation
import numpy as np

## movement function

def move_dir(x,y,max):
    my_dir_opt = {
        "0" : (1,0),
        "1" : (-1,0),
        "2" : (0,1),
        "3" : (0,-1)
    }
    
    my_rand = np.random.randint(4)

    my_dir = my_dir_opt[str(my_rand)]

    my_dist = np.random.randint(1,4)

    x += my_dir[0] * my_dist
    y += my_dir[1] * my_dist

    if x > max:
        x = max
    elif y > max:
        y = max
    if x < 0:
        x = 0
    elif y < 0:
        y = 0

    return (x,y)


## run sim
n_dim = 100
n_dim = dim
n_iter = 100

data = np.zeros((n_dim,n_dim))

cmap = colors.ListedColormap(['white', 'black'])

locations = [(k,l) for k in [0,25,50,75,99] for l in [0,25,50,75,99]]
# locations = [(k,l) for k in [0,5,10,20,30, 40] for l in [0,5,10,20,30, 40]]
for (x,y) in locations:
    data[x,y] = 1
my_plot = plt.matshow(data, cmap = cmap)

for i in range(n_iter):

    for j in range(len(locations)):
        (x,y) = locations[j]
        data[x,y] = 0

        tmp = move_dir(x,y,n_dim-1)
        x = tmp[0]
        y = tmp[1]

        data[x,y] = 1
        locations[j] = (x,y)

    my_plot.set_data(data)
    plt.pause(0.1)
