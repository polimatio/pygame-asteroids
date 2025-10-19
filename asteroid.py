import pygame
from circleshape import CircleShape

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
