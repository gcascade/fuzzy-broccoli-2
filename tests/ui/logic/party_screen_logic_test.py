from unittest.mock import MagicMock

from classes.character.character import Character
from ui.components.ui_manager import UIManager
from ui.logic.party_screen_logic import go_back, on_character_click, on_character_hover
from ui.screens.main_menu_screen import MainMenuScreen


def test_go_back():
    ui_manager_mock = MagicMock(spec=UIManager)
    main_menu_screen_mock = MagicMock(spec=MainMenuScreen)

    go_back(ui_manager_mock, main_menu_screen_mock)

    ui_manager_mock.set_active_screen.assert_called_once_with(main_menu_screen_mock)


def test_on_character_hover():
    ui_manager_mock = MagicMock(spec=UIManager)
    ui_manager_mock.set_message = MagicMock(return_value="mocked value")
    character_mock = MagicMock(spec=Character)

    on_character_hover(ui_manager_mock, character_mock)

    ui_manager_mock.set_message.assert_called_once()


def test_on_character_click(capsys):
    ui_manager_mock = MagicMock(spec=UIManager)
    character_mock = MagicMock(spec=Character)
    character_mock.get_name = MagicMock(return_value="Name")

    on_character_click(ui_manager_mock, character_mock)

    captured = capsys.readouterr()
    assert "Character Name clicked!" in captured.out
