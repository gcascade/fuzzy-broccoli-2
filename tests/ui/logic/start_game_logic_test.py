from unittest.mock import MagicMock

import pytest

from ui.components.ui_manager import UIManager
from ui.logic.start_screen_logic import start_game
from ui.screens.main_menu_screen import MainMenuScreen


@pytest.fixture
def ui_manager():
    return MagicMock(spec=UIManager)


@pytest.fixture
def main_menu_screen():
    return MagicMock(spec=MainMenuScreen)


def test_start_game_sets_active_screen(ui_manager, main_menu_screen):
    start_game(ui_manager, main_menu_screen)

    ui_manager.set_active_screen.assert_called_once_with(main_menu_screen)
