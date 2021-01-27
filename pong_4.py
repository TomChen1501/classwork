import pygame

# -- Global Constants
score = 0

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

# data of pong
ball_width = 20
x_val = 150
y_val = 200
x_direction = 1
y_direction = 1
x_bounce = False
y_bounce = False
difficulty = 3

# data of paddle
padd_length = 15
padd_width = 60
x_padd = 0 # position of the pad
y_padd = 20


### -- Game Loop
while not done:
    
    # -- user input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        '''if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_padd -= 5
                if y_padd == -5:
                    y_padd = 0
            elif event.key == pygame.K_DOWN:
                y_padd += 5
                if y_padd == 425:
                    y_padd = 420'''
    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_UP]:
        y_padd -= 5 
        if y_padd <= -5:
            y_padd = 0
                
    if keys[pygame.K_DOWN]:
        y_padd += 5 
        if y_padd >= 425:
            y_padd = 420
            
       
                    
    # -- Game logic goes after this comment                
    # -- screen background is BLACK
    screen.fill(BLACK)
    # -- Draw here
    pygame.draw.rect(screen,BLUE,(x_val,y_val,ball_width,ball_width))
    pygame.draw.rect(screen,WHITE,(x_padd,y_padd,padd_length,padd_width))

    if x_bounce:
        if y_bounce:
            x_val += (-difficulty) * x_direction
            y_val += (-difficulty) * y_direction
        else:
            x_val += (-difficulty) * x_direction
            y_val += difficulty * y_direction
    else:
        if y_bounce:
            x_val +=  difficulty * x_direction
            y_val += (-difficulty) * y_direction
        else:
            x_val += difficulty * x_direction
            y_val += difficulty * y_direction

    if x_val > 620:
        x_bounce = True
    elif (x_val <= 15) and (x_val >= -15) and (y_val in range(y_padd,y_padd + 61)):
        x_bounce = False
        difficulty += 1
        
    if y_val > 460:
        y_bounce = True
    elif y_val < 0:
        y_bounce = False

    if x_val < -200:
        score += 1
        x_val = 150
        y_val = 200
        x_bounce = False
        y_bounce = False
        
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # -- the clock ticks over
    clock.tick(60)

pygame.quit()

