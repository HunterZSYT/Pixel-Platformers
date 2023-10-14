
import pygame

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        width = 40
        height = 60
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 128, 255))  # Blue color

        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - height - 10  # Start near the bottom

        # Set speed vector
        self.change_x = 0
        self.change_y = 0

        # Define constants for player
        self.gravity = 0.35
        self.jump_strength = -10
        self.can_jump = True
        self.jumps_done = 0  # To track double jumps

    def update(self):
        # Gravity
        self.change_y += self.gravity
        self.rect.y += self.change_y

        # Horizontal movement
        self.rect.x += self.change_x

        # Reset jump count if on the ground
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height - 10:
            self.rect.y = SCREEN_HEIGHT - self.rect.height - 10
            self.can_jump = True
            self.jumps_done = 0

    def go_left(self):
        self.change_x = -5

    def go_right(self):
        self.change_x = 5

    def stop(self):
        self.change_x = 0

    def jump(self):
        if self.can_jump and self.jumps_done < 2:  # Allow for double jump
            self.change_y = self.jump_strength
            self.jumps_done += 1
            if self.jumps_done == 2:
                self.can_jump = False
