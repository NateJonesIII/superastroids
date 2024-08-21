from colors import DEFAULT
from constants import *
import pygame, random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call the parent constructor
        super().__init__(x, y, radius)   
        
    def draw(self, screen):
        pygame.draw.circle(screen, DEFAULT,self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            
            dir1 = self.velocity.rotate(random_angle)
            dir2 = self.velocity.rotate(-random_angle)
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = dir1 * 1.2
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = dir2 * 1.2