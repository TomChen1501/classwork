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
pygame.display.set_caption('Pong')

# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
ball_width = 20
x_val = 150
y_val = 200
x_direction = 1
y_direction = 1
x_bounce = False
y_bounce = False

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
    pygame.draw.rect(screen,BLUE,(x_val,y_val,ball_width,ball_width))

    if x_bounce:
        if y_bounce:
            x_val += (-1) * x_direction
            y_val += (-1) * y_direction
        else:
            x_val += (-1) * x_direction
            y_val += y_direction
    else:
        if y_bounce:
            x_val +=  x_direction
            y_val += (-1) * y_direction
        else:
            x_val += x_direction
            y_val += y_direction

    if x_val == 620:
        x_bounce = True
    elif x_val == 0:
        x_bounce = False

    if y_val == 460:
        y_bounce = True
    elif y_val == 0:
        y_bounce = False

    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # -- the clock ticks over
    clock.tick(60)

pygame.quit()

