# Import the pygame library and initialise the game engine
import pygame
pygame.init()
class Paddle(pygame.sprite.Sprite):

 
# Define some colors
    BLACK = (0,0,0)
WHITE = (255,255,255)
 
# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
 
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200


all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True


# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while carryOn:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              carryOn = False 
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: 
                     carryOn=False 
  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)
    
    all_sprites_list.update()
 
 
 
    screen.fill(BLACK)
    
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
 
    pygame.display.flip()
     
    clock.tick(60)
 
pygame.quit()







import pygame
BLACK = (0,0,0)
 
class Paddle(pygame.sprite.Sprite):
    
    
    def __init__(self, color, width, height):
            
    
   
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def moveUp(self, pixels):
        self.rect.y -= pixels
       
        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):
        self.rect.y += pixels
        
        if self.rect.y > 400:
          self.rect.y = 400