from basic.generate_map import generate_map
from basic.main import *
import pygame

# ##
# map_size = 100
# an, an_locs = instantiate_animals(10,map_size)
# my_map, occupied, plants = generate_map(x_dim = map_size, y_dim = map_size, n_plants = 500)
# occupied = occupied + an_locs

# for frame in range(1,300):
#     for index in range(len(an)):
#         an[index].update(frame = frame, occupied = occupied, index = index, plants = plants)
#         print(index, an[index].location, an[index].hunger, an[index].status)







## UI

# initialise game
pygame.init()

# setup
map_size = 60
an, an_locs = instantiate_animals(10, map_size)
my_map, occupied, plants = generate_map(x_dim = map_size, y_dim = map_size, n_plants = 10)
# occupied = occupied + an_locs
occupied = an_locs

# colours
white = (255,255,255)
black = (0,0,0)
# blue = (0,0,255)
red = (255,0,0)

# display dimensions
dis = pygame.display.set_mode((map_size * 10, map_size * 10))
# set window title
pygame.display.set_caption('Population Simulation')

dis.fill(white)
pygame.display.update()


game_over = False
clock = pygame.time.Clock()
frame = 1


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    dis.fill(white)
    for index in range(len(an)):
        an[index].update(frame = frame, occupied = occupied, index = index, plants = plants)
        pygame.draw.rect(dis, black, [an[index].location[0]*10, an[index].location[1]*10, 10, 10])

    frame += 1

    pygame.display.update()

    clock.tick(30)
                
pygame.quit()
