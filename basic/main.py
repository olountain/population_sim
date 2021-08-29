import math
import numpy as np

# default movement function (random walk)
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

# move towards a target
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

# find a target (need to update to include range/pathfinding)
def get_target(my_loc, target_locs):
    distances = np.zeros(len(target_locs))

    for i in range(len(target_locs)):
        distances[i] = math.sqrt(((my_loc[0]-target_locs[i][0])**2)+((my_loc[1]-target_locs[i][1])**2))
    
    index = np.argmin(distances)

    return target_locs[index]

# update which grid spaces are occupied
def update_occupied(occupied, index, location):
    occupied[index] = location
    return occupied


# animal class
class Animal:

    def __init__(self, location = None, move_speed = None, status = "default"):
        if location is None:
            self.location = (0,0)
        if move_speed is None:
            self.move_speed = 5

        self.hunger = 100
        self.thirst = 100

        self.status = status

    status_options = ["default", "hungry", "chased"]

    # called every iteration (frame)
    def update(self, frame, occupied, index, plants):
        # move animal
        if frame % self.move_speed == 0:
            self.move(occupied, plants)
            update_occupied(occupied, index, self.location)

        # update hunger (hard coded)
        if frame % 1 == 0:
            self.hunger -= 1

        # update thirst (hard coded)
        # if i % 4 == 0:
        #     self.thirst -= 1

        # update status
        if self.status == "default":
            if self.hunger < 40 and self.hunger < self.thirst and self.status != "hungry":
                self.status = "hungry"
            elif self.thirst < 40 and self.thirst < self.hunger and self.status != "thirsty":
                self.status = "thirsty"
            else:
                self.status = "default"


    def move(self, occupied, plants):

        # default movement
        if self.status == "default":

            new_loc = move_default(self.location, 100)

            if new_loc not in occupied:
                self.location = new_loc


        # move towards food
        if self.status == "hungry":

            target_loc = get_target(self.location, plants)

            new_loc = move_to_target(self.location, target_loc)

            if new_loc not in occupied:
                self.location = new_loc

            if self.location == target_loc:
                self.hunger = 100
                self.status = "default"
        
        return

# function to generate animals and their locations
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

