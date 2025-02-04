# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # creates a new Clock object that can be used to track an amount of time and providing functions to control framerate
    
    updateable = pygame.sprite.Group() # The Group class is a container that holds and manages multiple game objects. 
    drawable = pygame.sprite.Group() # We can organize our objects into various groups to track them more easily.
    
    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # instantiate a Player object

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
        updateable.update(dt)

        # to re-render the player on the screen each frame
        for obj in drawable:
            obj.draw(screen)
        
        # refresh the screen (last step in game loop)
        pygame.display.flip()

        # it will pause the game loop until 1/60th of a second has passed (max 60fps)
        # also returns the passed time (converted from ms to s) and save it into dt
        dt = clock.tick(60) / 1000


# this line ensures the main() function is only called when this file is run directly
if __name__ == "__main__":
    main()