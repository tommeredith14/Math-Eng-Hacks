import pygame
import random
import math

pygame.init()

WHITE = (255, 255, 255)

RESPONSE = 0.005

class Turret(pygame.sprite.Sprite):
    def __init__(self):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)

# Sets up the image and Rect
        self.bitmap = pygame.image.load("tankGun.png").convert_alpha()
        self.bitmap.set_colorkey((255,255,255))
        self.rect = self.bitmap.get_rect()
        self.rect.centerx = size[0] / 2
        self.rect.centery = size[1] / 2
        self.bitmap2 = self.bitmap

    def update(self, xpos, ypos, angle):
        self.rect.centerx = xpos
        self.rect.centery = ypos
        self.bitmap = pygame.transform.rotate(self.bitmap2, angle)
        self.rect = self.bitmap.get_rect(center=self.rect.center)




class Tank(pygame.sprite.Sprite):
    def __init__(self, bullet_list):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)

# Sets up the image and Rect
        self.still_alive = True # It was a triumph.
        self.health = 80
        self.bitmap = pygame.image.load("Chassis.png")#.convert_alpha()
        self.bitmap.set_colorkey((255,255,255))
        self.rect = self.bitmap.get_rect()
        self.rect.centerx = size[0] / 2
        self.rect.centery = size[1] / 2
        self.bitmap2 = self.bitmap
        self.angle = 140
        self.speedx = 0.0
        self.speedy = 0.0
        self.accelx = 0.0
        self.accely = 0.0
        self.bullet_list = bullet_list

        self.turret = Turret()
        self.turret_rot = 0
        self.turret_angle = 200

    def doDamage(self, damage):
        self.health -= damage
        if (damage <= 0):
            self.still_alive = False


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
        self.bitmap = pygame.transform.rotate(self.bitmap2, self.angle)
        self.rect = self.bitmap.get_rect(center=self.rect.center)


    def update(self, immutable_list, destructable_list):

        if self.still_alive:
        
            self.turret_angle += 10 * self.turret_rot
            
            self.rotate()
            
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

            if (self.collideImmutable(immutable_list) or self.collideDestructable(destructable_list) == 2):
                self.rect.centerx = oldxpos
                self.rect.centery = oldypos
                self.speedx = 0
                self.speedy = 0

            self.turret.update(self.rect.centerx, self.rect.centery, self.angle + self.turret_angle)

    def render(self):
        screen.blit(self.bitmap, (self.rect))
        screen.blit(self.turret.bitmap, (self.turret.rect))
