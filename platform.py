
import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        # Create a rectangular platform
        self.image = pygame.Surface([width, height])
        self.image.fill((139, 69, 19))  # Brown color for now
        self.rect = self.image.get_rect()

        # Set position
        self.rect.x = x
        self.rect.y = y
