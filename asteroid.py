import pygame
import random

from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        radius = self.radius
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            angle1 = self.velocity.rotate(random_angle)
            angle2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            split_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid1.velocity = angle1 * 1.2
            split_asteroid2.velocity = angle2 * 1.2
            
    def update(self, dt):
        self.position += self.velocity * dt
        
