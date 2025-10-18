import pygame
from constants import *
from player import Player


def main():
    print("Starting Asteroids!")
    pygame.init()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock() # clock to manage frame rate
    dt = 0 # delta time between frames in seconds
    while True:
        # clock.tick(60) returns the elapsed time in ms but dt is in seconds
        dt = clock.tick(60) / 1000.0  # Limit to a frame rate of 60 FPS
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
