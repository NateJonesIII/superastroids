# this allows us to use code from
# the open-source pygame library
# throughout this file
from menu import main_menu
import pygame, sys, os
from constants import *
from colors import *
from pygame.locals import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from weapons import Shot

# Set the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Replace with your music file's relative path
music_path = 'assets/music/space-120280.mp3'  

 # main game function 
def main():
    pygame.init()
    pygame.mixer.init()
        
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FramePerSec = pygame.time.Clock()
    pygame.display.set_caption("Super Asteroids")
    

     # Load and play background music
    pygame.mixer.music.load(music_path)  # Replace with your music file
    pygame.mixer.music.set_volume(0.5)  # Set the volume
    pygame.mixer.music.play(-1)  # Loop the music indefinitely
   
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (shots, updatable, drawable)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (drawable, updatable)
    
    FPS_NUM = 120
    
    dt = 0

    # player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    main_menu(screen)  # Display the main menu
    
    # game loop begins
    while True:
        # close applciaton on exit/quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update all updatable objects    
        for obj in updatable:
            obj.update(dt)     
            
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                sys.exit()
                
        
            for bullet in shots:
                if asteroid.collide(bullet):
                    bullet.kill()
                    asteroid.split()
                    
                
        # black out screen   
        screen.fill(BLACK)
        
        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)
        
        # Update the display
        pygame.display.flip()

        # limit frames to FPS setting
        dt = FramePerSec.tick(FPS_NUM)/1000
# running main module        
if __name__ == "__main__":
    main()