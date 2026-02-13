import pygame
import random
from logger import log_event 
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  
        log_event("asteroid_split")
        split_dir = random.uniform(20, 50)
        split_one = self.velocity.rotate(split_dir)
        split_two = self.velocity.rotate(split_dir * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first = Asteroid(self.position, self.position, new_radius)
        second = Asteroid(self.position, self.position, new_radius)
        first.velocity = split_one * 1.2
        second.velocity = split_two * 1.2
