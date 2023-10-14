
import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, move_type=None):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill((255, 0, 0))  # Red color for danger
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        # For moving obstacles
        self.move_type = move_type
        self.move_direction = 1  # 1: forward/right/up, -1: backward/left/down
        self.move_speed = 4
        self.move_range = 100
        self.move_start = pygame.Vector2(x, y)
        self.move_end = pygame.Vector2(x, y)

        if self.move_type == "horizontal":
            self.move_end.x += self.move_range
        elif self.move_type == "vertical":
            self.move_end.y += self.move_range

    def update(self):
        # Moving the obstacle based on its type
        if self.move_type == "horizontal":
            self.rect.x += self.move_speed * self.move_direction
            if self.rect.x <= self.move_start.x or self.rect.x >= self.move_end.x:
                self.move_direction *= -1
        elif self.move_type == "vertical":
            self.rect.y += self.move_speed * self.move_direction
            if self.rect.y <= self.move_start.y or self.rect.y >= self.move_end.y:
                self.move_direction *= -1
