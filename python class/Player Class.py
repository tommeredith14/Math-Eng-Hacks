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

RESPONSE = 0.1

clock = pygame.time.Clock()


class Tank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Chassis.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() / 2 - self.image.get_width() / 2
        self.rect.y = screen.get_height() / 2 - self.image.get_height() / 2
        self.angle = 0.0
        self.image.set_colorkey(WHITE)
        self.image2 = self.image
        self.rect.topleft = [100,200]

##        self.speedx = 0
##        self.speedy = 0
##        self.accelx = 8
##        self.accely = -1
        
    
    def update(self):
##        self.speedx += self.accelx
##        self.speedy += self.accely
##        
##        self.speedx *= 0.95
##        self.speedy *= 0.95
##        
##        self.rect.x += self.speedx * RESPONSE
##        self.rect.y += self.speedy * RESPONSE
##
##        self.angle = math.atan2(self.speedx, self.speedy)

        self.image = pygame.transform.rotate(self.image2, math.pi / 4)
        self.rect = self.image.get_rect()
        

    def collideImmutable(self, immutable_list):
        immutCollisionList = pygame.sprite.spritecollide(self, immutable_list, False)

        if not immutCollisionList:
            return False
        else:
            return True
    

    def collideDestructable(self, destructable_list):
        destructCollisionList = pygame.sprite.spritecollide(self, destructable_list, True)

        if not destructCollisionList:
           return 0
        elif (self.playerXSpeed / math.cos(self.playerAngle) > 500):
            return 1
        else:
            return 2



class Block(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.rect = self.image.get_rect()




class PlayerHitbox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("tankChassis.png").convert()
        
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
            

tank_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block()

    block.rect.x = random.randrange(size[0])
    block.rect.y = random.randrange(size[1])

    all_sprites_list.add(block)


score = 0

screen.fill(WHITE)

tank = Tank()

tank_list.add(tank)


done = False
while done == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    tank_list.update()

    all_sprites_list.draw(screen)
    tank_list.draw(screen)


    
    pygame.display.flip()
    clock.tick(20)
    
pygame.quit()
