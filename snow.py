import pygame
import random
import math
# -- Global Constants


# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)


# -- Initialise PyGame
pygame.init()


# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption('Snow')

## Define the class snow which is a sprite
class Snow(pygame.sprite.Sprite):
    # Define the construction of snow
    def __init__(self,color,width,height):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,600)
        self.rect.y = random.randrange(0,400)


# -- Exit game flag set to false
done = False

# Create a list of the snow blocks
snow_group = pygame.sprite.Group()
# Create a list of all sprite
all_sprites_group = pygame.sprite.Group()

# Create the snowflakes
number_of_flakes = 50 # We are creating 50 snowflakes
for x in range(number_of_flakes):
    my_snow = Snow(WHITE,5,5)
    snow_group.add(my_snow)
    all_sprites_group.add(my_snow)

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

### -- Game Loop
while not done:
    # -- user input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # -- Game logic goes after this comment
    # -- screen background is BLACK
    screen.fill(BLACK)
    # -- Draw here
    all_sprites_group.draw(screen)
    
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # -- the clock ticks over
    clock.tick(60)

pygame.quit()

