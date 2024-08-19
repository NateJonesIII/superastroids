# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from colors import *
from pygame.locals import *
from player import Player
 


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FramePerSec = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (drawable, updatable)
    
    FPS_NUM = 120
    
    dt = 0

    # player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    #Game loop begins
    while True:
        # close applciaton on exit/quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update all updatable objects    
        for obj in updatable:
            obj.update(dt)     
    
        # black out screen   
        screen.fill(BLACK)
        
        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)
        
        # Update the display
        pygame.display.flip()

        # Both are valued at 60
        dt = FramePerSec.tick(FPS_NUM)/1000
        
if __name__ == "__main__":
    main()