import sys, pygame, math
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

class BulletHitBox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("tankGun.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()


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


screen = pygame.display.set_mode(size)

ball = pygame.image.load("tankGun.png")
ballrect = ball.get_rect()


bullet = Bullet(10,20,math.pi/6,20)

bullet_list = pygame.sprite.Group()
bullet_list.add(bullet.hitbox)
clock = pygame.time.Clock()
while 1:
   for event in pygame.event.get():
       if event.type == pygame.QUIT: sys.exit()

   ballrect = ballrect.move(speed)
   if ballrect.left < 0 or ballrect.right > width:
       speed[0] = -speed[0]
   if ballrect.top < 0 or ballrect.bottom > height:
       speed[1] = -speed[1]

   bullet.updateBullet()

   screen.fill(black)
   screen.blit(ball, ballrect)
   bullet_list.draw(screen)
   pygame.display.flip()

   clock.tick(30)



