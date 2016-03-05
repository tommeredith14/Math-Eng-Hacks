class EnemyHitBox(pygame.sprite.Sprite):
    def __init__(self,x_pos, y_pos, enemy_list, bullet_list,speed=None):
        super().__init__()
        self.image = pygame.image.load("Chassis.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        if speed == None:
            self.speed= 0
        else:
            self.speed = speed
        self.xSpeed = self.speed
        self.ySpeed = self.speed
        enemy_list.add(self)
        self.list_to_fire = bullet_list

    def update(self):

        self.rect.x += self.xSpeed *  1
        self.rect.y += self.ySpeed *  1
    def fireBullet(self,xSpeed = None, ySpeed = None):
        # newBullet = Bullet(self.hitbox.rect.x, self.hitbox.rect.y, 1)
         newBullet = BulletHitBox(4,self.rect.x, self.rect.y,1, self.list_to_fire)
       #  bullet_list.add(newBullet)

class BulletHitBox(pygame.sprite.Sprite):
    def __init__(self, speed, x_pos, y_pos, angle, bullet_list):
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

