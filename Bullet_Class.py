import sys, pygame, math, random

pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0
bullet_list = pygame.sprite.Group()
class EnemyHitBox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Chassis.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()



class Enemy:
     def __init__(self,x_pos, y_pos, speed=None):

        self.x_position = x_pos
        self.y_position = y_pos
        if speed == None:
            self.speed= 0
        else:
            self.speed = speed
        self.xSpeed = self.speed
        self.ySpeed = self.speed
        self.hitbox = EnemyHitBox()
        self.hitbox.rect.x = x_pos
        self.hitbox.rect.y = y_pos

     def updateEnemy(self):

        self.hitbox.rect.x += self.xSpeed *  0.1
        self.hitbox.rect.y += self.ySpeed *  0.1

     def fireBullet(self,xSpeed = None, ySpeed = None):
        # newBullet = Bullet(self.hitbox.rect.x, self.hitbox.rect.y, 1)
         newBullet = BulletHitBox(4,self.hitbox.rect.x, self.hitbox.rect.y,1)
       #  bullet_list.add(newBullet)


class BulletHitBox(pygame.sprite.Sprite):
    def __init__(self, speed, x_pos, y_pos, angle):
        super().__init__()
        self.image = pygame.image.load("tankGun.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.xSpeed = speed * math.cos(angle)
        self.ySpeed = speed * math.sin(angle)
        self.rect.x = x_pos
        self.rect.y = y_pos
        bullet_list.add(self)

    def update(self):
        self.rect.x += self.xSpeed *  1
        self.rect.y += self.ySpeed *  1




'''
class Bullet:
    def __init__(self,x_pos, y_pos, angle, speed=None):
        self.bulletImage = pygame.image.load("tankGun.png")
        self.x_position = x_pos
        self.y_position = y_pos
        if speed == None:
            self.speed= 30
        else:
            self.speed = speed
        self.xSpeed = self.speed * math.cos(angle)
        self.ySpeed = self.speed * math.sin(angle)
        self.hitbox = BulletHitBox()

    def updateBullet(self):

        self.hitbox.rect.x += self.xSpeed *  0.1
        self.hitbox.rect.y += self.ySpeed *  0.1
'''

screen = pygame.display.set_mode(size)




#bullet = Bullet(10,20,math.pi/6,20)
newEnemy = Enemy(50,50)


enemy_list = pygame.sprite.Group()
enemy_list.add(newEnemy.hitbox)


#bullet_list.add(bullet.hitbox)
clock = pygame.time.Clock()
count = 0
while 1:
   for event in pygame.event.get():
       if event.type == pygame.QUIT: sys.exit()



#   bullet.updateBullet()
   if count%5 == 0:
    newEnemy.fireBullet()
   print("Hello")
   screen.fill(black)
   bullet_list.update()
   bullet_list.draw(screen)
   enemy_list.draw(screen)
   pygame.display.flip()
   count+= 1
   clock.tick(30)



