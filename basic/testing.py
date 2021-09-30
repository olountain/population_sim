from basic.generate_map import generate_map
from basic.main import *
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import pygame

## UI

# initialise game
pygame.init()

# setup
map_size = 60
my_map, occupied, plants = generate_map(x_dim = map_size, y_dim = map_size, n_plants = 10)
plt.imsave("basic/bg.png", my_map, cmap=ListedColormap(['green', 'blue']))
bg = pygame.image.load("basic/bg.png")
bg = pygame.transform.scale(bg, (map_size * 10, map_size * 10))
an, an_locs = instantiate_animals(10, map_size, occupied = occupied)
occupied = occupied + an_locs
# occupied = an_locs

# colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


# display dimensions
dis = pygame.display.set_mode((map_size * 10, map_size * 10))
# set window title
pygame.display.set_caption('Population Simulation')

# dis.fill(white)
dis.blit(bg, (0,0))
# pygame.surfarray.blit_array(dis, bg)
pygame.display.update()


game_over = False
clock = pygame.time.Clock()
frame = 1


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # dis.fill(white)
    dis.blit(bg, (0,0))
    for index in range(len(an)):
        an[index].update(frame = frame, occupied = occupied, index = index, plants = plants)
        pygame.draw.rect(dis, black, [an[index].location[0]*10, an[index].location[1]*10, 10, 10])

    frame += 1

    pygame.display.update()

    clock.tick(10)
                
pygame.quit()



##
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


my_map, occupied, plants = generate_map(x_dim = map_size, y_dim = map_size, n_plants = 10)
an, an_locs = instantiate_animals(10, map_size, occupied = occupied)
intersection(occupied, an_locs)

tmp = np.where(my_map == 1)

[(tmp[0][i], tmp[1][i]) for i in range(len(tmp[0]))]== occupied