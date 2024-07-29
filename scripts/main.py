"""
Fuzzy Broccoli 2

This module initializes and runs the main game loop for Fuzzy Broccoli 2.
"""

import pygame

from scripts.game import game_loop

# Initialize PyGame
pygame.init()

# Screen settings
screen_width = 1024
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Fuzzy Broccoli 2")

if __name__ == "__main__":
    game_loop(screen, clock)
