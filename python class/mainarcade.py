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

SCREEN_DIMS = [840,525]
SCALE_FACTOR = 0.5
TILE_DIMS = [30,30]
OBSTACLE_COLOUR=[GREEN, BROWN,PURPLE]

class Obstacle(pygame.sprite.Sprite):
    """This is a class obstacle which is basically a wall"""
    def __init__(self,x,y,TILE_DIMS,color,blocktype):
        """constructor function"""
        super().__init__()
        
        self.image = pygame.Surface(TILE_DIMS)
        self.image.fill(OBSTACLE_COLOUR[blocktype])
        self.rect=self.image.get_rect()
        self.rect.y=y
        self.rect.x=x

        blocktype=0
        self.blocktype=blocktype
        
        



screen = pygame.display.set_mode(SCREEN_DIMS) #pygame.FULLSCREEN)
pygame.display.set_caption("ARCADE")
clock=pygame.time.Clock()


#Main Program Loop
def main():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(GREY)
        pygame.display.flip()
        clock.tick(20)
    pygame.quit()
main()

    
    
