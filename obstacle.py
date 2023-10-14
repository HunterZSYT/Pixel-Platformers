
import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        # Create a rectangular obstacle (spikes for now)
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 0, 0))  # Red color to represent danger
        self.rect = self.image.get_rect()

        # Set position
        self.rect.x = x
        self.rect.y = y
