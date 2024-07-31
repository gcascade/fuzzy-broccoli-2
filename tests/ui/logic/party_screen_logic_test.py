from unittest.mock import MagicMock

from ui.components.ui_manager import UIManager
from ui.logic.party_screen_logic import go_back
from ui.screens.main_menu_screen import MainMenuScreen


def test_go_back():
    ui_manager_mock = MagicMock(spec=UIManager)
    main_menu_screen_mock = MagicMock(spec=MainMenuScreen)

    go_back(ui_manager_mock, main_menu_screen_mock)

    ui_manager_mock.set_active_screen.assert_called_once_with(main_menu_screen_mock)
