import sys

import pygame

# Initialize PyGame
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fuzzy Broccoli 2")


# Main game loop
def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game state

        # Render to screen
        screen.fill((0, 0, 0))  # Fill screen with black
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game_loop()
