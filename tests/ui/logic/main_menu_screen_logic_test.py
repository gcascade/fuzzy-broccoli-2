from unittest.mock import MagicMock, patch

import pytest

from ui.components.ui_manager import UIManager
from ui.logic.main_menu_screen_logic import main_menu_screen_callbacks
from ui.screens.party_screen import PartyScreen


@pytest.fixture
def ui_manager():
    return MagicMock(spec=UIManager)


@pytest.fixture
def party_screen():
    return MagicMock(spec=PartyScreen)


def test_main_menu_screen_callbacks(ui_manager, party_screen):
    callbacks = main_menu_screen_callbacks(ui_manager, party_screen)

    assert "play" in callbacks
    assert "view_party" in callbacks
    assert "settings" in callbacks
    assert "quit" in callbacks

    assert callable(callbacks["play"])
    assert callable(callbacks["view_party"])
    assert callable(callbacks["settings"])
    assert callable(callbacks["quit"])


def test_play_game_callback(ui_manager, party_screen, capsys):
    callbacks = main_menu_screen_callbacks(ui_manager, party_screen)
    play_game_callback = callbacks["play"]

    play_game_callback()

    captured = capsys.readouterr()
    assert "Play button clicked!" in captured.out


def test_view_party_callback(ui_manager, party_screen):
    callbacks = main_menu_screen_callbacks(ui_manager, party_screen)
    view_party_callback = callbacks["view_party"]

    view_party_callback()

    ui_manager.set_active_screen.assert_called_once_with(party_screen)


def test_settings_callback(ui_manager, party_screen, capsys):
    callbacks = main_menu_screen_callbacks(ui_manager, party_screen)
    settings_callback = callbacks["settings"]

    settings_callback()

    captured = capsys.readouterr()
    assert "Settings button clicked!" in captured.out


def test_quit_game_callback(ui_manager, party_screen):
    callbacks = main_menu_screen_callbacks(ui_manager, party_screen)
    quit_game_callback = callbacks["quit"]

    with patch("sys.exit") as mock_sys_exit, patch("pygame.quit") as mock_pygame_quit:
        quit_game_callback()

        mock_pygame_quit.assert_called_once()
        mock_sys_exit.assert_called_once()
