import sys
from typing import Callable

import pygame


def main_menu_screen_callbacks() -> dict[str, Callable[[], None]]:
    """
    Return a dictionary of main menu screen callbacks.

    :return: A dictionary of main menu screen callbacks.
    """

    def play_game():
        print("Play button clicked!")

    def view_party():
        print("View Party button clicked!")

    def settings():
        print("Settings button clicked!")

    def quit_game():
        pygame.quit()
        sys.exit()

    return {
        "play": play_game,
        "view_party": view_party,
        "settings": settings,
        "quit": quit_game,
    }
