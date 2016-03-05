import pygame
import random
import math

pygame.init()

size = [1560, 900]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Will Clark's Game")

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

RESPONSE = 0.005

clock = pygame.time.Clock()

class Turret(pygame.sprite.Sprite):
    def __init__(self):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)

# Sets up the image and Rect
        self.image = pygame.image.load("tankGun.png").convert_alpha()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.centerx = size[0] / 2
        self.rect.centery = size[1] / 2
        self.image2 = self.image

    def update(self, xpos, ypos, angle):
        self.rect.centerx = xpos
        self.rect.centery = ypos
        self.image = pygame.transform.rotate(self.image2, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

class Tank(pygame.sprite.Sprite):
    def __init__(self, bullet_list):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        
        self.still_alive = True # It was a triumph.

# Sets up the image and Rect
        self.image = pygame.image.load("TestPic.png").convert_alpha()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.centerx = size[0] / 2
        self.rect.centery = size[1] / 2
        self.image2 = self.image
        self.angle = 0
        self.speedx = 1.0
        self.speedy = 1.0
        self.accelx = 2.0
        self.accely = -1.0
        self.bullet_list = bullet_list

        self.turret = Turret()
        self.turret_rot = 0
        self.turret_angle = 200


    def firebullet(self):
        fire_angle = angle + turret_angle # angle in degrees
        
        

    def inputFromController(self, xjoy, yjoy, turret_rot):
        self.accelx = xjoy
        self.accely = yjoy
        self.turret_rot = turret_rot


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
        elif (self.speedx / math.cos(self.playerAngle) > 500):
            self.speed.x = 0
            self.speed.y = 0
            return 1
        else:
            return 2

    def rotate(self):
        self.image = pygame.transform.rotate(self.image2, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)


    def update(self, immutable_list, destructable_list):

        if self.still_alive:
        
            self.turret_angle += 10 * self.turret_rot
            
            self.rotate()
            
 #           self.turret_angle += 30
            
            self.angle -=10
            
            oldxpos = self.rect.centerx
            oldypos = self.rect.centery

            self.speedx += self.accelx
            self.speedy += self.accely

            self.speedx *= 0.95
            self.speedy *= 0.95

            self.rect.centerx += self.speedx * RESPONSE
            self.rect.centery += self.speedy * RESPONSE

            if (self.speedx > 200 or self.speedy > 200):
                self.angle = math.atan2(self.speedx, self.speedy) * 180 / math.pi

            #self.image = pygame.transform.rotate(self.image2, self.angle)

            if (self.collideImmutable(immutable_list) or self.collideDestructable(destructable_list) == 2):
                self.rect.centerx = oldxpos
                self.rect.centery = oldypos
                self.speedx = 0
                self.speedy = 0

            self.turret.update(self.rect.centerx, self.rect.centery, self.angle + self.turret_angle)

    def render(self):
 #       screen.blit(self.image, (self.rect))
 #       screen.blit(self.turret.image, (self.turret.rect))
 
        rendering = pygame.sprite.Group()
        rendering2 = pygame.sprite.Group()
        rendering.add(self)
        rendering2.add(self.turret)
        rendering.draw(screen)
        #rendering2.draw(screen)
        




tank = Tank(14)

immut = pygame.sprite.Group()
destruct = pygame.sprite.Group()

done = False
while done == False:
    
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    tank.update(immut, destruct)
    tank.render()
    
    pygame.display.flip()
    clock.tick(20)
    
pygame.quit()
