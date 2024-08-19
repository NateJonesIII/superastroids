from constants import PLAYER_RADIUS
import pygame
from colors import DEFAULT
from circleshape import CircleShape

# inheriting from circleshape parent
class Player(CircleShape):
    def __init__(self, x, y):
        # Call the parent class constructor
        super().__init__(x, y, PLAYER_RADIUS)
        # Initialize fields as required
        self.radius = PLAYER_RADIUS
        self.position = pygame.Vector2(x,y)
        self.rotation = 0
    
    
    
    # method of the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, DEFAULT, self.triangle(), 2)