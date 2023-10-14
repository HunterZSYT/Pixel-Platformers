
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # For now, we'll use a simple rectangle as the player's sprite
        # In the future, this can be replaced with a pixel art image
        self.image = pygame.Surface([50, 50])
        self.image.fill((0, 128, 0))  # Green color
        self.rect = self.image.get_rect()

        # Player's position
        self.rect.x = 375  # Start at the center of the screen
        self.rect.y = 500  # Start towards the bottom

        # Player's velocity
        self.change_x = 0
        self.change_y = 0

    def update(self):
        """Update player's position based on velocity"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    def go_left(self):
        """Make the player move to the left"""
        self.change_x = -5

    def go_right(self):
        """Make the player move to the right"""
        self.change_x = 5

    def stop(self):
        """Stop the player's movement"""
        self.change_x = 0
