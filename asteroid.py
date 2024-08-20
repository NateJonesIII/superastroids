from colors import DEFAULT
import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call the parent constructor
        super().__init__(x, y, radius)   
        
    def draw(self, screen):
        pygame.draw.circle(screen, DEFAULT,self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt