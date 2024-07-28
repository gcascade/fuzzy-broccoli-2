from ui.components.ui_manager import UIManager
from ui.screens.main_menu_screen import MainMenuScreen


def start_game(ui_manager: UIManager, main_menu_screen: MainMenuScreen):
    """
    Start the game by setting the active screen to the main menu screen.

    :param ui_manager: The UIManager instance.
    :param main_menu_screen: The MainMenuScreen instance.
    """
    ui_manager.set_active_screen(main_menu_screen)
