
import pygame
from player import Player
from platform import Platform
from obstacle import Obstacle

# Initialize pygame
pygame.init()

# Define screen dimensions, colors, and fonts
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SKY_BLUE = (135, 206, 250)
font = pygame.font.Font(None, 74)

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
winning_platform = Platform(350, 100, 100, 20)

# Add platforms to the sprite groups
platforms.add(platform1, platform2, platform3, winning_platform)
all_sprites.add(platform1, platform2, platform3, winning_platform)

# Create obstacles (spikes for now)
obstacles = pygame.sprite.Group()
obstacle1 = Obstacle(300, 430, 50, 20)
obstacles.add(obstacle1)
all_sprites.add(obstacle1)

# Main game loop
running = True
has_won = False
game_over = False
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

    # Player-obstacle collision detection
    if pygame.sprite.spritecollide(player, obstacles, False):
        game_over = True

    # Check for winning condition
    if player.rect.colliderect(winning_platform.rect):
        has_won = True

    # Draw everything
    screen.fill(SKY_BLUE)
    all_sprites.draw(screen)
    
    # Display messages
    if has_won:
        win_text = font.render("You Won!", True, (255, 255, 255))
        screen.blit(win_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
    elif game_over:
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
