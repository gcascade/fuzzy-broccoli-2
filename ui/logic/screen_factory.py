from ui.components.ui_manager import UIManager
from ui.logic.main_menu_screen_logic import main_menu_screen_callbacks
from ui.logic.party_screen_logic import go_back
from ui.logic.start_screen_logic import start_game
from ui.screen_type import ScreenType
from ui.screens.main_menu_screen import MainMenuScreen
from ui.screens.party_screen import PartyScreen
from ui.screens.start_screen import StartScreen


class ScreenFactory:
    def __init__(self, ui_manager: UIManager):
        self.ui_manager = ui_manager

    def create_screen(self, screen_type: ScreenType):
        def create_start_screen():
            return StartScreen(
                self.ui_manager,
                lambda: start_game(
                    self.ui_manager, self.create_screen(ScreenType.MAIN_MENU)
                ),
            )

        def create_main_menu_screen():
            return MainMenuScreen(
                self.ui_manager,
                main_menu_screen_callbacks(
                    self.ui_manager, self.create_screen(ScreenType.VIEW_PARTY)
                ),
            )

        def create_party_screen():
            return PartyScreen(
                self.ui_manager,
                lambda: go_back(
                    self.ui_manager, self.create_screen(ScreenType.MAIN_MENU)
                ),
            )

        screen_dict = {
            ScreenType.START: create_start_screen,
            ScreenType.MAIN_MENU: create_main_menu_screen,
            ScreenType.VIEW_PARTY: create_party_screen,
        }

        create_screen_func = screen_dict.get(screen_type)
        if create_screen_func:
            return create_screen_func()
        else:
            raise ValueError(f"Unknown screen type: {screen_type}")
