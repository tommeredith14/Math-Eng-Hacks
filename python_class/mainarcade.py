import pygame
import random
pygame.init()
import Enemy_Bullet_Classes
from Enemy_Bullet_Classes import *
#pygame.mixer.music.load('Cave_Story')
#import Geoff.py
import serial
import time
ser = serial.Serial('/dev/ttyACM1', 9600)

Input = [0, 0, 0, 0, 0, 0]
print('Horizontal   Vertical  Shooting  Steering   Other   Pause')

def Update(Input): #UPDATES DATA READINGS
    ser.write(b'`')     #tells arduino it wants some readings
    val1 = ser.readline().strip() #reads all input at once as a string
    if (len(val1) != 0):          #makes sure not empty
        rawArray = val1.decode().split(' ')    #generates array with ' ' delimiter
        if (len(rawArray) == 6):           #gets rid of first garbage read
            Input[0] = int(rawArray[0])
            Input[1] = int(rawArray[1])
            Input[2] = int(rawArray[2])
            Input[3] = str(rawArray[3])
            Input[4] = int(rawArray[4])
            Input[5] = int(rawArray[5])
            return


import RPi.GPIO as GPIO
LEDS = [7, 11, 12, 13, 15, 16, 18, 22] #starts at red to green
Buzzer = 29
HealthLevel = 8

def SetLights(level):
    #fixes wrong levels
    if (level > 8):
        level = 8
    if (level < 0):
        level = 0
        
    #turn off all lights above level
    for i in range(7, level-1, -1):
        GPIO.output(LEDS[i], GPIO.LOW)
    #turn on all lights at and below level
    for i in range(level):
        GPIO.output(LEDS[i], GPIO.HIGH)

def TurnOff():
    for i in range(8):
        GPIO.output(LEDS[i], GPIO.LOW)
    GPIO.output(Buzzer, GPIO.LOW)

        
GPIO.setmode(GPIO.BOARD) # Number GPIOs by its physical location
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.LOW)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.LOW)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, GPIO.LOW)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, GPIO.LOW)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, GPIO.LOW)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.LOW)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.LOW)
GPIO.setup(29, GPIO.OUT)
GPIO.output(29, GPIO.LOW)

#testing
SetLights(HealthLevel)
GPIO.output(Buzzer, GPIO.HIGH)
time.sleep(2)
GPIO.output(Buzzer, GPIO.LOW)
HealthLevel = 1
SetLights(HealthLevel)

            
#time.sleep(2)
#SetLights(3)
#time.sleep(2)
#SetLights(12)
#time.sleep(2)
#SetLights(-4)
#time.sleep(2)



#Colours
BLACK = [  0,  0,  0]
GREY = [122, 79, 79]
WHITE = [255,255,255]
RED = [255,  0,  0]
PURPLE = [153,0,153]
GREEN=[0,255,0]
BLUE =[0,0,255]
BROWN = [139,69,19]
START_X = 800
START_Y = 300

SCREEN_DIMS = [1560,900]
SCALE_FACTOR = 0.5
TILE_DIMS = [30,30]
OBSTACLE_PNG=["grasstile.png", "bricktile.png","fence.png", "tnttile.png","watertile.png","fire.png"]
TILE_TYPE=[0,1,2,3,4,5]

immutable_object=pygame.sprite.Group()
destructible_object=pygame.sprite.Group()
bystander_object=pygame.sprite.Group()
explosive_object=pygame.sprite.Group()
drowning_object=pygame.sprite.Group()
fire_object=pygame.sprite.Group()



class Tile(pygame.sprite.Sprite):
    """This is a class obstacle which is basically a wall"""
    def __init__(self,tiletype):
        """constructor function"""
        super().__init__()
        
        self.image=pygame.image.load(OBSTACLE_PNG[tiletype]).convert()
       
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale2x(self.image)

        self.tiletype=tiletype
        self.rect=self.image.get_rect()
    def switchType(self, newType):
        self.tiletype=newType
        self.image=pygame.image.load(OBSTACLE_PNG[newType]).convert()
        self.image = pygame.transform.scale2x(self.image)

class Map():
    def __init__(self,tilelist):
        self.tilelist=tilelist
    def draw_map(self):
        for tile,value in enumerate(self.tilelist):
            currenttile = Tile(self.tilelist[tile])
            currenttile.rect.x=(tile%52)*30
            currenttile.rect.y=(tile//52)*30
            
        
            if(self.tilelist[tile]==0):
                bystander_object.add(currenttile)
            if(self.tilelist[tile]==1):
                immutable_object.add(currenttile)
            if(self.tilelist[tile]==2):
                destructible_object.add(currenttile)
            if(self.tilelist[tile]==3):
                explosive_object.add(currenttile)
            if(self.tilelist[tile]==4):
                drowning_object.add(currenttile)
            if(self.tilelist[tile]==5):
                fire_object.add(currenttile)
            
    def update(self):
        bystander_object.empty()
        immutable_object.empty()
        explosive_object.empty()
        drowning_object.empty()
        self.draw_map()
            

            
            
            
        

    

    
        



screen = pygame.display.set_mode(SCREEN_DIMS)#,pygame.FULLSCREEN)
pygame.display.set_caption("ARCADE")
clock=pygame.time.Clock()


#Main Program Loop
def main():
    done = False
    count = 0
    screen.fill(GREY)
    tilelist=[]
    
    def map_one(tilelist):
        for i in range(0,1560):
            tilelist.append(0)
            if i<53 or i>1508 or i%52==0 or i%52==51:
                tilelist[i]=1
            elif i%52 == 5 and i<1000:
                tilelist[i]=2
            elif i%52 >20 and i%52<28 and i>500 and i<1000 :
                tilelist[i]=4
            elif i%52>20 and i<700 and i>599 :
                tilelist[i]=4
                if i%52 >40 and i%52 <44:
                    tilelist[i]=2
                elif i%52==40 or i%52==44:
                    tilelist[i]=1
            elif ((i%52==11) or (i%52==15)) and (i>400 and i<1200):
                tilelist[i] =1
            else:
                num=random.randint(0,100)
                if num>99:
                    tilelist[i]=3
    def map_two(tilelist):
        for i in range(0,1560):
            tilelist.append(0)
            if (i<53 or i>1508 or i%52==0 or i%52==51) :
                tilelist[i]=1
            elif (i%52%3==0 and i%52%6==0) and not(i>730 and i<1000) and not (i%52==48):
                tilelist[i]=1
            elif (i>1040 and i<1092) or (i>676 and i<728) :
                tilelist[i]=3


    
    
    map_one(tilelist)
    backgroundmap = Map(tilelist)
    backgroundmap.draw_map()

    #Collisions
    def bullet_collisions(bullet_list,enemy_list):
        hit_list=pygame.sprite.groupcollide(bullet_list,immutable_object,1,0)
        hit_list=pygame.sprite.groupcollide(destructible_object,bullet_list,0,1)
        for key in hit_list:
            destructible_object.remove(key)
            key.switchType(0)
            bystander_object.add(key)
    
        hit_list=pygame.sprite.groupcollide(explosive_object,bullet_list,0,1)
        for key in hit_list:
            destructible_object.remove(key)
            key.switchType(5)
            bystander_object.add(key)

        hit_list=pygame.sprite.groupcollide(enemy_list, bullet_list,0,0)
        for key in hit_list:
            
            if hit_list[key][0].sType != key.getType():
                key.do_damage(10)
                bullet_list.remove(hit_list[key])
        hit_list=pygame.sprite.spritecollide(player, bullet_list,0)
        if hit_list:
            if hit_list[0].sType != player.getType():
                player.health -= 10
                bullet_list.remove(hit_list[0])

    def enemy_collisions(enemy_list):
        hit_list=pygame.sprite.groupcollide(enemy_list,immutable_object,0,0)
        for key in hit_list:
            
           enemy_x = key.rect.x
           enemy_y = key.rect.y

           obs_x = hit_list[key][0].rect.x
           obs_y = hit_list[key][0].rect.y

           hardx  = False;
           hardy = False;

           if(enemy_x <= 31):
               key.xSpeed  = abs(key.xSpeed) + 1
               key.rect.x = 32
               hardx = True
           elif (enemy_x >= 869):
                key.xSpeed = -1*abs(key.xSpeed) - 1
                key.rect.x = 864
                hardx = True
           if(enemy_y <= 31):
                key.ySpeed = abs(key.ySpeed)+1
                key.rect.y = 35
                hardy = True
           elif(enemy_y >= 1529):
                key.ySpeed = -1*abs(key.ySpeed) - 1
                key.rect.y = 1528
                hardy = True
           if (abs(enemy_x - obs_x) <= abs(enemy_y - obs_y)) and hardy == False:
                key.ySpeed = -1 * (key.ySpeed)
                key.rect.y += 4*key.xSpeed
           elif (abs(enemy_y - obs_x) >= abs(enemy_y - obs_y)) and hardx == False:
                key.xSpeed = -1*(key.xSpeed)
                key.rect.x += 4*key.xSpeed


            
        hit_list=pygame.sprite.groupcollide(enemy_list,destructible_object,0,0)
        for key in hit_list:
            
            key.xSpeed = random.uniform(-2,2)
            key.ySpeed = random.uniform(-2,2)
    def player_collisions():
        hit_list = pygame.sprite.spritecollide(player,immutable_object,0)
        if hit_list:
            player.coll_Immutable = True
        else:
            player.coll_Immutable = False
        hit_list = pygame.sprite.spritecollide(player,destructible_object,0)
        if hit_list:
            for i in hit_list:
                destructible_object.remove(i)
                i.switchType(0)
                bystander_object.add(i)
            player.coll_Destructible = True
        else:
            player.coll_Destructible = False
        hit_list = pygame.sprite.spritecollide(player,explosive_object,0)
        if hit_list:
            for i in hit_list:
                explosive_object.remove(i)
                i.switchType(5)
                fire_object.add(i)
            player.coll_Explosion = True
        else:
            player.coll_Explosion = False            
        hit_list = pygame.sprite.spritecollide(player,fire_object,0)
        if hit_list:
            player.coll_Fire = True
        else:
            player.coll_Fire = False
        hit_list = pygame.sprite.spritecollide(player,drowning_object,0)
        if hit_list:
            player.coll_Drowning = True
        else:
            player.coll_Drowning = False
            
    bullet_list=pygame.sprite.Group()
    enemy_list=pygame.sprite.Group()
    enemy=Enemy(100,100,enemy_list,bullet_list,2)
    count=0
    enemy2=Enemy(300,100,enemy_list,bullet_list,4)
    player = Tank(bullet_list, START_X, START_Y)
    endExplosion = Explosion()
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        Update(Input)
        player.inputFromController(Input[0], Input[1], Input[3])

        
        player.update()        
        
            
        bullet_list.update()
        enemy_list.update()
        if count%10==0:
            enemy.fireBullet()
        if count%7==0:
            enemy2.fireBullet()
        if Input[2] == 1:
            player.firebullet()
        
        bullet_collisions(bullet_list, enemy_list)
        enemy_collisions(enemy_list)
        player_collisions()
        bullet_list.draw(screen)
        enemy_list.draw(screen)
        
        immutable_object.draw(screen)
        destructible_object.draw(screen)
        bystander_object.draw(screen)
        explosive_object.draw(screen)
        drowning_object.draw(screen)
        bullet_list.draw(screen)
        enemy_list.draw(screen)
        
        if player.still_alive == False:
            endExplosion.updateExplode(screen, player.rect.centerx, player.rect.centery)


        SetLights(math.ceil(8* (player.health / 1000)))

        player.react()
        player.render(screen)
        
        count+=1
        pygame.draw.rect(screen, RED, (650, 45, 200 * (player.health / 1000), 30))
        pygame.draw.rect(screen, RED, (650, 45, 200, 30), 5)
        
        
        
        pygame.display.flip()
        clock.tick(20)
        
    pygame.quit()
main()

    
    
