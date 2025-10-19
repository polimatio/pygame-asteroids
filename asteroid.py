import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

# Asteroid class representing an asteroid in the game
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Override draw method of CircleShape
    def draw(self, screen):
        pygame.draw.circle(screen, "gray", self.position, self.radius, 2)
    
    # Override update method of CircleShape
    def update(self, dt):
        # Move asteroid in a straight line at constant speed
        self.position += self.velocity * dt

    # Asteroids can split into smaller asteroids when hit
    def split(self):
        self.kill()  # remove the current asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # asteroid was too small to split further; just destroy it
        
        # Create two smaller asteroids moving in different directions
        random_angle = random.uniform(20, 50)
        split_vector1 = self.velocity.rotate(random_angle)
        split_vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = split_vector1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = split_vector2 * 1.2
