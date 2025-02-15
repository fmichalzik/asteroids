# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # creates a new Clock object that can be used to track an amount of time and providing functions to control framerate
    
    updateable = pygame.sprite.Group() # the Group class is a container that holds and manages multiple game objects. 
    drawable = pygame.sprite.Group() # we can organize our objects into various groups to track them more easily.
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    Player.containers = (updateable, drawable) # adds all instances of a Player to the groups
    Asteroid.containers = (asteroids, updateable, drawable) # adds all instances of a Asteroid to the groups
    AsteroidField.containers = (updateable)  # adds all instances of a AsteroidField to the groups
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots) # instantiate a Player object
    asteroid_field = AsteroidField()

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
        
        # checks if any asteroid collide with the player
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                exit()
            # checks if any shot collide with the asteroid    
            for shot in shots:
                if shot.collision(asteroid):
                    # asteroid.kill()
                    asteroid.split()
                    pygame.sprite.Sprite.kill(shot)

        # to re-render objects (in drawable group) on the screen each frame
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