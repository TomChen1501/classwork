import pygame
import random
import math
# -- Global Constants

score = 0

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
pygame.display.set_caption('Space Invaders')

## Define the class snow which is a sprite
class Invader(pygame.sprite.Sprite):
    # Define the construction of snow
    def __init__(self,color,width,height,speed):
        # Set speed of sprite
        self.speed = speed
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour

        self.status = 0 #0, flying, 1 destroyed
        
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,600)
        self.rect.y = random.randrange(-50,0)
        
    # Class update function - runs for each pass through the game loop
    def update(self):
        self.rect.y = self.rect.y + self.speed

class Player(pygame.sprite.Sprite):
    # Define the construction of snow
    def __init__(self,color,width,height):
        # Set speed of sprite
        self.speed = 0
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = size[0] - height 
        self.rect.y = 300
        self.height = height
        self.lives = 5
        self.bullet_count = 50
       

        
    def update(self):
        self.rect.x = self.rect.x + self.speed
        if self.rect.x > size[0] - self.height:
            self.rect.x = size[0] - self.height
        elif self.rect.x < 0:
            self.rect.x = 0

            
    def fire_bullet(self):
        
        # Create new bullet
        new_bullet = Bullet(RED, self.rect.x, self.rect.y)
        all_sprites_group.add(new_bullet)



        
    def player_set_speed(self,speed):
        self.speed = speed

class Bullet(pygame.sprite.Sprite):
    def __init__(self,color,x_pos,y_pos):
        self.speed = -2
        super().__init__()
        self.image = pygame.Surface([2,2])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y <= 0:
            self.kill()
        elif pygame.sprite.spritecollide(self,invader_group,True):
            self.kill()
            global score
            score += 5


# -- Exit game flag set to false
done = False

# Create a list of the snow blocks
invader_group = pygame.sprite.Group()
# Create a list of all sprite
all_sprites_group = pygame.sprite.Group()

# Create the snowflakes
number_of_flakes = 10 
for x in range(number_of_flakes):
    my_snow = Invader(WHITE,10,10,1)
    invader_group.add(my_snow)
    all_sprites_group.add(my_snow)

# Create player
player = Player(YELLOW,10,10)
all_sprites_group.add(player)


# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

### -- Game Loop
while not done:
    # -- user input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                player.player_set_speed(-3)
            elif event.key == pygame.K_RIGHT:
                player.player_set_speed(3)
            elif event.key == pygame.K_UP:
                player.fire_bullet()
                player.bullet_count -= 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.player_set_speed(0)
        
            
            

    # -- Game logic goes after this comment
    all_sprites_group.update()
    player_hit_group = pygame.sprite.spritecollide(player,invader_group,True)
    
    for foo in player_hit_group:
        player.lives = player.lives - 1
        

        
    # -- screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    all_sprites_group.draw(screen)
     
    
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # -- the clock ticks over
    clock.tick(60)

pygame.quit()

