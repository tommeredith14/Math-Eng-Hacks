import pygame
import random
import math

pygame.init()

size = [1680, 1050]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Will Clark's Game")

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

clock = pygame.time.Clock()


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):

        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()


class PlayerHitbox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        
        self.image = pygame.image.load("tankChassis.png").convert()
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()

class Player():
    def __init__(self, xpos, ypos):

        self.chassisImage = pygame.image.load("tankChassis.png")
        self.turretImage = pygame.image.load("tankGun.png")

        self.playerXAccel = 0 # Input from controller, -100 to 100
        self.playerYAccel = 0 # Input from controller, -100 to 100

        self.playerXSpeed = 0 # Speed between -2000 and 2000
        self.playerYSpeed = 0 # Speed between -2000 and 2000
        
        self.playerXPos = xpos # Positive is down
        self.playerYPos = ypos # Positive is right

        self.turretCWPos = 0 # A number 0-360 degrees. 0 is down, 90 is left
        self.turretCWSpeed = 0
        
        self.turretCWAccel = 0 # -1, 0, 1. Input from controller.

        self.playerAngle = 0.0 # A number -Pi -> Pi radians. 0 is down, Pi/2 is left.

        self.scale = 1
        self.speed = 1

        self.colliding = False

    def collideImmutable(self):

            

        

    def collideDestructable(self):

    

    def updatePlayer(self):

        oldXLoc = self.playerXPos
        oldYLoc = self.playerYPos
        oldPlayerAngle = self.playerAngle

        
        self.playerXSpeed += self.playerXAccel # Apply acceleration
        self.playerYSpeed += self.playerYAccel # Apply acceleration
        
        self.playerXSpeed *= 0.95 # Apply drag
        self.playerYSpeed *= 0.95 # Apply drag

        moveAngle = math.atan2(playerYSpeed / playerXSpeed) # find player angle

        self.playerXLoc += self.PlayerXSpeed * math.cos(moveAngle) * 0.01
        self.playerYLoc += self.PlayerYSpeed * math.sin(moveAngle) * 0.01

        if playerXSpeed / math.cos(moveAngle) > 100:
            self.playerAngle = moveAngle

        if collideImmutable ||

        
        

        
        
        
            
        


block_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()

playerList  = pygame.sprite.Group()



for i in range(50):
    block = Block(BLACK, 20, 15)

    block.rect.x = random.randrange(size[0])
    block.rect.y = random.randrange(size[1])

    block_list.add(block)
    all_sprites_list.add(block)


score = 0

screen.fill(WHITE)


done = False
while done == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pos = pygame.mouse.get_pos()

    all_sprites_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(20)
    
pygame.quit()
