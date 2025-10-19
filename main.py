import pygame
from constants import *
from player import Player


def main():
    # Initialize Pygame and create the main game window
    print("Starting Asteroids!")
    pygame.init()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    # Create sprite instances
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # player in centre of screen
    
    # Game setup
    clock = pygame.time.Clock() # clock to manage frame rate
    dt = 0 # delta time between frames in seconds
    
    # Game loop
    while True:
        dt = clock.tick(60) / 1000.0  # Limit to a frame rate of 60 FPS
        # clock.tick(60) returns the elapsed time in ms but dt is in seconds
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Render frame
        screen.fill("black") # clear screen each frame
        updatable.update(dt) # update all updatable sprites
        #drawable.draw(screen) # draw all drawable sprites
        # custom draw to handle non-rectangular shapes
        for sprite in drawable:
            sprite.draw(screen) # call each sprite's draw method
        pygame.display.flip() # update the full display surface to the screen


if __name__ == "__main__":
    main()
