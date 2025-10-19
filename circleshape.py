import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # add to sprite containers if they exist
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        # Initialize position, velocity, and radius
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        
        # Groups expect sprites to have image and rect attributes
        self.image = pygame.Surface((1, 1), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.position)

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # keep rect in sync with position
        self.rect.center = self.position
        # sub-classes must override
        pass

    def is_colliding(self, other: "CircleShape") -> bool:
        # Ensure the other object is a CircleShape at runtime
        if not isinstance(other, CircleShape):
            raise TypeError("is_colliding expects another CircleShape")
        # Check for collision with another CircleShape
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)
