import pygame
import math
import random

RESPONSE = 0.004
WHITE = [255,255,255]
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x_pos, y_pos, enemy_list, bullet_list,speed=None):
        super().__init__()
        self.image = pygame.image.load("Chassis.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.health = 30
        if speed == None:
            self.speed= 0
        else:
            self.speed = speed
            
        self.xSpeed = self.speed
        self.ySpeed = self.speed
        enemy_list.add(self)
        self.enemy_list = enemy_list
        self.list_to_fire = bullet_list

    def update(self):

        self.rect.x += self.xSpeed *  1
        self.rect.y += self.ySpeed *  1
    def fireBullet(self, speed = None, angle = None):
        # newBullet = Bullet(self.hitbox.rect.x, self.hitbox.rect.y, 1)
        if self.health > 0:
            print("fire")
            if speed == None:
                speed = random.uniform(self.speed+1,7)
            if angle == None:
                angle = random.uniform(-math.pi,math.pi)
            newBullet = Bullet(speed,self.rect.x, self.rect.y,angle, self.list_to_fire,self)
           #  bullet_list.add(newBullet)
    def do_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.enemy_list.remove(self)
            self.remove()
    def getType(self):
        return "Enemy"

class Bullet(pygame.sprite.Sprite):
    def __init__(self, speed, x_pos, y_pos, angle, bullet_list,shooter):
        super().__init__()
        self.image = pygame.image.load("bullet.png").convert()
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect()
        self.xSpeed = speed * math.cos(angle) 
        self.ySpeed = speed * math.sin(angle)
        self.rect.x = x_pos + self.xSpeed *  1
        self.rect.y = y_pos + self.ySpeed *  1
        bullet_list.add(self)
        self.sType = shooter.getType()
        print("Success")

    def update(self):
        self.rect.x += self.xSpeed *  1
        self.rect.y += self.ySpeed *  1


###############################
        ########################
        #########################
        #########################

class Turret(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)

# Sets up the image and Rect
        self.image = pygame.image.load("tankGun.png").convert_alpha()
        self.image.set_colorkey([0,0,0,0])
        self.rect = self.image.get_rect()
        self.rect.centerx = x_pos
        self.rect.centery = y_pos
        self.image2 = self.image

    def update(self, xpos, ypos, angle):
        self.rect.centerx = xpos
        self.rect.centery = ypos
        self.image = pygame.transform.rotate(self.image2, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

class Tank(pygame.sprite.Sprite):
    def __init__(self, bullet_list, x_pos, y_pos):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        
        self.still_alive = True # It was a triumph.

# Sets up the image and Rect
        self.image = pygame.image.load("Chassis.png").convert_alpha()
        self.image.set_colorkey([0,0,0,0])
        self.rect = self.image.get_rect()
        self.rect.centerx = x_pos
        self.rect.centery = y_pos
        self.image2 = self.image
        self.angle = 0
        self.speedx = 0
        self.speedy = 0
        self.accelx = 0
        self.accely = 0
        self.bullet_list = bullet_list
        self.health = 100

        self.turret = Turret(x_pos, y_pos)
        self.turret_rot = 0
        self.turret_angle = 0
    
    def getType():
        return "Player"


    def firebullet(self):
        fire_angle = angle + turret_angle # angle in degrees
        newBullet = Bullet(10, self.rect.centerx,self.rect.centery,math.radians(fire_angle),self.bullet_list)
        
        

    def inputFromController(self, xjoy, yjoy, turret_rot):
        self.accelx = xjoy
        self.accely = yjoy
        if (turret_rot == "L"):
            self.turret_rot = 1
        elif (turret_rot == "R"):
            self.turret_rot = -1
        else:
            self.turret_rot = 0


    def collideImmutable(self, immutable_list):
        immutCollisionList = pygame.sprite.spritecollide(self, immutable_list, False)

        if not immutCollisionList:
            return False
        else:
            return True
    

    def collideDestructable(self, destructable_list):
        destructCollisionList = pygame.sprite.spritecollide(self, destructable_list, False)

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
            
 #           self.angle -=10
            
            oldxpos = self.rect.centerx
            oldypos = self.rect.centery

            self.speedx += self.accelx
            self.speedy += self.accely

            self.speedx *= 0.95
            self.speedy *= 0.95

            self.rect.centerx += self.speedx * RESPONSE
            self.rect.centery += self.speedy * RESPONSE

            self.angle = math.atan2(self.speedx, self.speedy) * 180 / math.pi

            #self.image = pygame.transform.rotate(self.image2, self.angle)

            if (self.collideImmutable(immutable_list) or self.collideDestructable(destructable_list) == 2):
                self.rect.centerx = oldxpos
                self.rect.centery = oldypos
                self.speedx = 0
                self.speedy = 0

            self.turret.update(self.rect.centerx, self.rect.centery, self.angle + self.turret_angle)

    def render(self, screen):
 #       screen.blit(self.image, (self.rect))
 #       screen.blit(self.turret.image, (self.turret.rect))
 
        rendering = pygame.sprite.Group()
        rendering2 = pygame.sprite.Group()
        rendering.add(self)
        rendering2.add(self.turret)
        rendering.draw(screen)
        rendering2.draw(screen)





