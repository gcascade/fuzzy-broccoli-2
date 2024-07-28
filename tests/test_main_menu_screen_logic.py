from unittest.mock import patch

from ui.logic.main_menu_screen_logic import main_menu_screen_callbacks


def test_main_menu_screen_callbacks():
    callbacks = main_menu_screen_callbacks()

    assert "play" in callbacks
    assert "view_party" in callbacks
    assert "settings" in callbacks
    assert "quit" in callbacks

    assert callable(callbacks["play"])
    assert callable(callbacks["view_party"])
    assert callable(callbacks["settings"])
    assert callable(callbacks["quit"])


def test_play_game_callback(capsys):
    callbacks = main_menu_screen_callbacks()
    play_game_callback = callbacks["play"]

    play_game_callback()

    captured = capsys.readouterr()
    assert "Play button clicked!" in captured.out


def test_view_party_callback(capsys):
    callbacks = main_menu_screen_callbacks()
    view_party_callback = callbacks["view_party"]

    view_party_callback()

    captured = capsys.readouterr()
    assert "View Party button clicked!" in captured.out


def test_settings_callback(capsys):
    callbacks = main_menu_screen_callbacks()
    settings_callback = callbacks["settings"]

    settings_callback()

    captured = capsys.readouterr()
    assert "Settings button clicked!" in captured.out


def test_quit_game_callback():
    callbacks = main_menu_screen_callbacks()
    quit_game_callback = callbacks["quit"]

    with patch("sys.exit") as mock_sys_exit, patch("pygame.quit") as mock_pygame_quit:
        quit_game_callback()

        mock_pygame_quit.assert_called_once()
        mock_sys_exit.assert_called_once()
