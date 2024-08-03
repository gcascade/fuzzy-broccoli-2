"""
Fuzzy Broccoli 2

This module initializes and runs the main game loop for Fuzzy Broccoli 2.
"""

from core.game_initializer import initialize_game
from scripts.game import game_loop

screen, clock = initialize_game()

if __name__ == "__main__":
    game_loop(screen, clock)
