import pygame

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
pygame.display.set_caption('My Window')

# -- Exit game flag set to false
done = False

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
    pygame.draw.rect(screen,BLUE,(200,165,200,150))
    pygame.draw.circle(screen,YELLOW,(40,100),40,0)
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # -- the clock ticks over
    clock.tick(60)

pygame.quit()

