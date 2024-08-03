from core.config import Config
from core.game_data import load_game_data, load_key_from_config
from ui.components.ui_manager import UIManager
from ui.screens.main_menu_screen import MainMenuScreen


def start_game(ui_manager: UIManager, main_menu_screen: MainMenuScreen):
    """
    Start the game by setting the active screen to the main menu screen.

    :param ui_manager: The UIManager instance.
    :param main_menu_screen: The MainMenuScreen instance.
    """
    key = load_key_from_config(Config.CONFIG_FILENAME)
    if key:
        data = load_game_data(Config.GAME_DATA_FILENAME, key)
        print(data)
    ui_manager.set_active_screen(main_menu_screen)
