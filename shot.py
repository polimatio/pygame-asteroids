import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

# Shot class representing a projectile fired by the player
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    # Override draw method of CircleShape
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    # Override update method of CircleShape
    def update(self, dt):
        # Move projectile in a straight line at constant speed
        self.position += self.velocity * dt
