import pygame

# -- Global Constants


# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)


# -- Initialise PyGame
pygame.init()


# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption('House')

# -- Exit game flag set to false
done = False

sun_x_init = -40
sun_y_init = 100
sun_x = sun_x_init
sun_y = sun_y_init


# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
count = 0
time = 0

### -- Game Loop
while not done:
    # -- user input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # -- Game logic goes after this comment
    # -- screen background is BLACK
    if count >= 255/4:
        screen.fill((0,0,255))
    else:
        screen.fill((0,0,0 + 4*count))
    # -- Draw here
    pygame.draw.rect(screen,BLACK,(200,165,200,150))
    pygame.draw.rect(screen,WHITE,(220,185,30,30))
    pygame.draw.rect(screen,WHITE,(350,185,30,30))
    pygame.draw.rect(screen,(25,255,0),(275,240,50,75))
    pygame.draw.circle(screen,RED,(sun_x,sun_y),40,0)
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # -- the clock ticks over
    clock.tick(60)

    if sun_x > 680:
        sun_x = -40
        time = 0
        count = 0
        pygame.time.delay(2000)

    sun_x = sun_x_init + 5 * time
    sun_y = sun_y_init + 0.019 * time ** 2 - 2.7596 * time   
    time += 1
    
    if time <= 72:
        count += 1
    else:
        count -=1
        if count < 0:
            count = 0
    

pygame.quit()

