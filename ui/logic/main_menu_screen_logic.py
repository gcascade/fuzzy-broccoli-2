import sys
from typing import Callable

import pygame

from ui.components.ui_manager import UIManager
from ui.screens.party_screen import PartyScreen


def main_menu_screen_callbacks(
    ui_manager: UIManager, party_screen: PartyScreen
) -> dict[str, Callable[[], None]]:
    """
    Return a dictionary of main menu screen callbacks.

    :return: A dictionary of main menu screen callbacks.
    """

    def play_game():
        print("Play button clicked!")

    def view_party():
        ui_manager.set_active_screen(party_screen)

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
