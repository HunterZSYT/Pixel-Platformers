
import pygame
from player import Player
from platform import Platform

# Initialize pygame
pygame.init()

# Define screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SKY_BLUE = (135, 206, 250)

# Setup game screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pixel Platformer")
clock = pygame.time.Clock()

# Create the player and sprite groups
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Create platforms
platforms = pygame.sprite.Group()
platform1 = Platform(100, 450, 200, 20)
platform2 = Platform(400, 350, 200, 20)
platform3 = Platform(150, 250, 200, 20)

# Add platforms to the sprite groups
platforms.add(platform1, platform2, platform3)
all_sprites.add(platform1, platform2, platform3)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.go_left()
            elif event.key == pygame.K_RIGHT:
                player.go_right()
            elif event.key == pygame.K_UP:
                player.jump()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stop()

    # Update
    all_sprites.update()

    # Player-platform collision detection
    platform_hit_list = pygame.sprite.spritecollide(player, platforms, False)
    for platform in platform_hit_list:
        if player.change_y > 0:
            player.rect.y = platform.rect.y - player.rect.height
            player.change_y = 0
            player.can_jump = True

    # Draw everything
    screen.fill(SKY_BLUE)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
