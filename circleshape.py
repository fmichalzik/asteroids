import pygame
# in pygame, there is a base class called Sprite, to represent visual objects
# create a CircleShape class that inherits from Sprite to represent objects in the game

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    # detecting a collision between two objects
    def collision(self, other):
        return pygame.Vector2.distance_to(self.position, other.position) <= (self.radius + other.radius)