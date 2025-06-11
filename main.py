# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import *

def main():
    pygame.init() # Initialize the pygame library
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()  # Set the frame rate with this after every loop
    dt = 0  # dt = delta time, the time since the last frame

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        # Update game objects here
        player.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000 # Manages fps and saves dt in seconds.
        # THIS NEEDS TO BE AT THE END OF THE LOOP
if __name__ == "__main__":
    main()