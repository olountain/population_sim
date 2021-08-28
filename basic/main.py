from basic.basic_sim import move_dir
import math
import numpy as np

def move_default(my_loc,max):

    x = my_loc[0]
    y = my_loc[1]

    my_dir_opt = {
        "0" : (1,0),
        "1" : (-1,0),
        "2" : (0,1),
        "3" : (0,-1)
    }
    
    my_rand = np.random.randint(4)
    my_dir = my_dir_opt[str(my_rand)]

    x += my_dir[0]
    y += my_dir[1]

    if x > max:
        x = max
    elif y > max:
        y = max
    if x < 0:
        x = 0
    elif y < 0:
        y = 0

    return (x,y)


def move_to_target(my_loc, target_loc):

    if my_loc == target_loc:
        return my_loc

    x = my_loc[0]
    y = my_loc[1]

    dist_x = target_loc[0] - my_loc[0]
    dist_y = target_loc[1] - my_loc[1]

    if abs(dist_x) > abs(dist_y):
        if target_loc[0] > my_loc[0]:
            x += 1 
        else:
            x -= 1
    else:
        if target_loc[1] > my_loc[1]:
            y += 1 
        else:
            y -= 1

    return (x,y)

move_to_target((5,4), (8,3))

def get_target(my_loc, target_locs):
    distances = np.zeros(len(target_locs))

    for i in range(len(target_locs)):
        distances[i] = math.sqrt(((my_loc[0]-target_locs[i][0])**2)+((my_loc[1]-target_locs[i][1])**2))
    
    index = np.argmin(distances)

    return target_locs[index]



tmp = (1,2)
tmp1 = tmp[1]


class Animal:

    def __init__(self, location = None, move_speed = None, status = "default"):
        if location is None:
            self.location = (0,0)
        if move_speed is None:
            self.move_speed = 5

        self.status = status

    status_options = ["default", "hungry", "chased"]

    def move(self, i):

        if i % self.move_speed != 0:
            return

        # default movement
        if self.status == "default":

            self.location = move_default(self.location, 100)

        # move towards food
        if self.status == "hungry":

            target_loc = get_target(self.location, plants)

            new_loc = move_to_target(self.location, target_loc)


            self.location = new_loc

            if self.location == target_loc:
                self.status = "default"
        
        return



def instantiate_animals(n = 1, size = 10, occupied = []):

    locs = [(0,0)] * n

    animals = []

    for i in range(n):
        x = np.random.randint(size)
        y = np.random.randint(size)
        locs[i] = (x,y)

        while locs[i] in locs[0:i] or locs[i] in occupied:
            x = np.random.randint(size)
            y = np.random.randint(size)
            locs[i] = (x,y)

        a = Animal()
        a.location = locs[i]

        animals.append(a)

    return animals, locs

an, tmp = instantiate_animals(10,10)

occupied = []
occupied + tmp






plants = [(1,1),(2,3),(5,7),(10,13)]

get_target((5,5), plants)



a = Animal()
a.status = "hungry"
a.location = (5,5)

curr_locs


for i in range(1,101):
    a.move(i)
    print(a.location)
    print(a.status)

a.location = (5,5)
a.move(5,100)
a.location

move_default(5,5,100)



