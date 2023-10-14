
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Player sprite
        self.image = pygame.Surface([50, 50])
        self.image.fill((0, 128, 0))  # Green color for now
        self.rect = self.image.get_rect()

        # Starting position
        self.rect.x = 375
        self.rect.y = 500

        # Speed and movement attributes
        self.change_x = 0
        self.change_y = 0
        self.gravity = 0.5
        self.jump_power = -15
        self.can_jump = True

    def update(self):
        # Apply gravity
        self.change_y += self.gravity

        # Update position based on velocity
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        # Temporary boundary conditions to keep player in the screen
        if self.rect.y > 550:  
            self.rect.y = 550
            self.can_jump = True

    def go_left(self):
        self.change_x = -5

    def go_right(self):
        self.change_x = 5

    def stop(self):
        self.change_x = 0

    def jump(self):
        if self.can_jump:
            self.change_y = self.jump_power
            self.can_jump = False
