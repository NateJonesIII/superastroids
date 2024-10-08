from pygame.locals import *
from constants import *
import pygame
from colors import DEFAULT
from circleshape import CircleShape
from weapons import Shot

# inheriting from circleshape parent
class Player(CircleShape):
    def __init__(self, x, y):
        # Call the parent class constructor
        super().__init__(x, y, PLAYER_RADIUS)
        # Initialize fields as required
        self.radius = PLAYER_RADIUS
        self.position = pygame.Vector2(x,y)
        self.rotation = 0
        self.timer = 0
    
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
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)    
        if keys[pygame.K_SPACE] or keys[pygame.K_KP1]:
            if self.timer > 0:
                pass
            else:
                self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN 
     