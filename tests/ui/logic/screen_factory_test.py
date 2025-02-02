from unittest import mock
from unittest.mock import MagicMock, patch

import pygame_gui
import pytest

from ui.components.ui_manager import UIManager
from ui.logic.screen_factory import ScreenFactory
from ui.screen_type import ScreenType


@pytest.fixture
def ui_manager():
    ui_manager_mock = MagicMock(spec=UIManager)
    ui_manager_mock.get_width.return_value = 800
    ui_manager_mock.get_height.return_value = 600
    ui_manager_mock.get_instance.return_value = MagicMock(spec=pygame_gui.UIManager)
    return ui_manager_mock


@pytest.fixture
def screen_factory(ui_manager):
    return ScreenFactory(ui_manager)


def test_create_start_screen(screen_factory):
    with patch("ui.logic.screen_factory.StartScreen") as MockStartScreen:
        mock_screen_instance = MagicMock()
        MockStartScreen.return_value = mock_screen_instance

        screen = screen_factory.create_screen(ScreenType.START)

        assert screen == mock_screen_instance
        MockStartScreen.assert_called_once_with(
            screen_factory.ui_manager,
            mock.ANY,
        )


def test_create_main_menu_screen(screen_factory):
    with patch("ui.logic.screen_factory.MainMenuScreen") as MockMainMenuScreen:
        with patch("ui.logic.screen_factory.PartyScreen") as MockPartyScreen:
            with patch("ui.logic.screen_factory.SettingsScreen") as MockSettingsScreen:
                mock_screen_instance = MagicMock()
                MockMainMenuScreen.return_value = mock_screen_instance

                screen = screen_factory.create_screen(ScreenType.MAIN_MENU)

                assert screen == mock_screen_instance
                MockMainMenuScreen.assert_called_once_with(
                    screen_factory.ui_manager,
                    mock.ANY,
                )
                MockPartyScreen.assert_called_once_with(
                    screen_factory.ui_manager,
                    mock.ANY,
                )
                MockSettingsScreen.assert_called_once_with(
                    screen_factory.ui_manager,
                    mock.ANY,
                )


def test_create_party_screen(screen_factory):
    with patch("ui.logic.screen_factory.PartyScreen") as MockPartyScreen:
        mock_screen_instance = MagicMock()
        MockPartyScreen.return_value = mock_screen_instance

        screen = screen_factory.create_screen(ScreenType.VIEW_PARTY)

        assert screen == mock_screen_instance
        MockPartyScreen.assert_called_once_with(
            screen_factory.ui_manager,
            mock.ANY,
        )


def test_create_screen_invalid_type(screen_factory):
    with pytest.raises(ValueError, match="Unknown screen type: INVALID_TYPE"):
        screen_factory.create_screen("INVALID_TYPE")
