# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import *
from asteroid import *
from asteroidfield import *

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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(x, y)
    asteroidfield = AsteroidField()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        

        dt = clock.tick(60) / 1000 # Manages fps and saves dt in seconds.
        # THIS NEEDS TO BE AT THE END OF THE LOOP
if __name__ == "__main__":
    main()