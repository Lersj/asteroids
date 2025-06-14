import pygame

from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        radius = self.radius
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
