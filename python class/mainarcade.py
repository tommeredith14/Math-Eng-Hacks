import pygame
import random
pygame.init()

#Colours
BLACK = [  0,  0,  0]
GREY = [122, 79, 79]
WHITE = [255,255,255]
RED = [255,  0,  0]
PURPLE = [153,0,153]
GREEN=[0,255,0]
BLUE =[0,0,255]
BROWN = [139,69,19]

SCREEN_DIMS = [1680,1050]
SCALE_FACTOR = 0.5
TILE_DIMS = [30,30]
OBSTACLE_PNG=["grasstile.png", "bricktile.png","fence.png", "tnttile.png"]
TILE_TYPE=[0,1,2,3]

immutable_object=pygame.sprite.Group()
destructible_object=pygame.sprite.Group()
bystander_object=pygame.sprite.Group()
explosive_object=pygame.sprite.Group()



class Tile(pygame.sprite.Sprite):
    """This is a class obstacle which is basically a wall"""
    def __init__(self,tiletype):
        """constructor function"""
        super().__init__()
        
        self.image=pygame.image.load(OBSTACLE_PNG[tiletype]).convert()
        self.image.set_colorkey(WHITE)
        

        self.tiletype=tiletype
        self.rect=self.image.get_rect()

class Map():
    def __init__(self,tilelist):
        self.tilelist=tilelist
    def draw_map(self):
        for tile in self.tilelist:
            currenttile = Tile(self.tilelist[tile])
            currenttile.rect.x=(tile%56)*30
            currenttile.rect.y=tile/56*30
            print (currenttile.rect.x)
        
            if(self.tilelist[tile]==0):
                bystander_object.add(currenttile)
            if(self.tilelist[tile]==1):
                immutable_object.add(currenttile)
            if(self.tilelist[tile]==2):
                destructive_object.add(currenttile)
            if(self.tilelist[tile]==3):
                explosive_object.add(currenttile)

            
            
            
        
        



screen = pygame.display.set_mode(SCREEN_DIMS) #pygame.FULLSCREEN)
pygame.display.set_caption("ARCADE")
clock=pygame.time.Clock()


#Main Program Loop
def main():
    done = False
    screen.fill(GREY)
    tilelist=[]
    for i in range(0,1960):
        tilelist.append(1)
    backgroundmap = Map(tilelist)
    backgroundmap.draw_map()

    immutable_object.draw(screen)
    destructible_object.draw(screen)
    bystander_object.draw(screen)
    explosive_object.draw(screen)
   
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
       
        

        
        
        pygame.display.flip()
        clock.tick(20)
        
    pygame.quit()
main()

    
    
