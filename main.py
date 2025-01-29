# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock # creates a new Clock object that can be used to track an amount of time and providing functions to control framerate
    dt = 0 # delta time

    # infinite while loop for the game loop
    while True:

        # this will check if the user has closed the window and exit the game loop if they do
        # basically it will make the window's close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # setup screen with a solid "black" color.
        screen.fill((0, 0, 0))

        # more gamelogic goes here

        # it will pause the game loop until 1/60th of a second has passed (max 60fps)
        # also returns the passed time (converted from ms to s) and save it into dt
        clock.tick(60)
        dt = clock.tick() / 1000

        # refresh the screen (last step in game loop)
        pygame.display.flip()
    

# this line ensures the main() function is only called when this file is run directly
if __name__ == "__main__":
    main()