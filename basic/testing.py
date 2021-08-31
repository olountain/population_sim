from basic.generate_map import generate_map
from basic.main import *

##
an, an_locs = instantiate_animals(10,10)
my_map, occupied, plants = generate_map(x_dim = 100, y_dim = 100, n_plants = 500)
occupied = occupied + an_locs

for frame in range(1,300):
    for index in range(len(an)):
        an[j].update(frame = frame, occupied = occupied, index = index, plants = plants)
        print(j, an[j].location, an[j].hunger, an[j].status)