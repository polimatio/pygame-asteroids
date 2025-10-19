import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

# Player class representing the player's ship
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 # degrees
        self.shot_cooldown = 0 # shooting cooldown timer, in seconds


    # Calculate the triangle vertices for the player's ship
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    # Override draw method of CircleShape
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_RATE * dt


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    # Override update method of CircleShape
    def update(self, dt):
        # Update shot cooldown timer
        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt
        
        # Handle player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()


    # The player's ship can shoot projectiles in the direction it is facing
    def shoot(self):
        # Enforce shot cooldown
        if self.shot_cooldown > 0:
            return
        # Create a new shot
        shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOT_SPEED
        # Reset shot cooldown timer
        self.shot_cooldown = PLAYER_SHOT_COOLDOWN
