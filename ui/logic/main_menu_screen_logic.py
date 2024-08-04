import sys
from typing import Callable

import pygame

from core.config import Config
from core.data import get_initial_characters
from core.game_data import GameData, load_key_from_config, save_game_data
from ui.components.ui_manager import UIManager
from ui.screens.party_screen import PartyScreen
from ui.screens.settings_screen import SettingsScreen


def main_menu_screen_callbacks(
    ui_manager: UIManager, party_screen: PartyScreen, settings_screen: SettingsScreen
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
        ui_manager.set_active_screen(settings_screen)

    def quit_game():
        key = load_key_from_config(Config.CONFIG_FILENAME)
        game_data = GameData(characters=get_initial_characters())
        save_game_data(game_data, Config.GAME_DATA_FILENAME, key)
        pygame.quit()
        sys.exit()

    return {
        "play": play_game,
        "view_party": view_party,
        "settings": settings,
        "quit": quit_game,
    }
