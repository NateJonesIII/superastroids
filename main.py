# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from pygame.locals import *
from player import Player
 


def main():
    pygame.init()

    FPS = 120
    FramePerSec = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #Game loop begins
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))
        player.update(dt)
        player.draw(screen)
        
        pygame.display.flip()

        # Both are valued at 60
        dt = FramePerSec.tick(FPS)/1000
        

if __name__ == "__main__":
    main()