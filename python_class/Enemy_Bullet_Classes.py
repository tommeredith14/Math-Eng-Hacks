import pygame
import math
import random

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

