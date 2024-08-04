from unittest.mock import Mock

import pygame
import pytest

from ui.components.ui_manager import UIManager
from ui.screens.settings_screen import SettingsScreen


@pytest.fixture
def setup_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    manager = UIManager(800, 600)
    yield screen, manager
    pygame.quit()


def test_settings_screen_initialization(setup_pygame):
    screen, manager = setup_pygame
    back_button_callback = Mock()
    settings_screen = SettingsScreen(
        ui_manager=manager, back_button_callback=back_button_callback
    )

    assert settings_screen.title_label.get_instance().text == "Settings"
    assert settings_screen.back_button.get_instance().text == "Back"
    assert (
        settings_screen.message_box.get_instance().html_text == "Not implemented yet!"
    )
    assert settings_screen.message_box.blinking_label.text == "Click to continue..."
    assert not settings_screen.title_label.get_instance().visible
    assert not settings_screen.back_button.get_instance().visible
    assert not settings_screen.message_box.get_instance().visible
    assert not settings_screen.message_box.blinking_label.visible


def test_settings_screen_activate(setup_pygame):
    screen, manager = setup_pygame
    back_button_callback = Mock()
    settings_screen = SettingsScreen(
        ui_manager=manager, back_button_callback=back_button_callback
    )
    settings_screen.activate()

    assert settings_screen.title_label.get_instance().visible
    assert settings_screen.back_button.get_instance().visible
    assert settings_screen.message_box.get_instance().visible
    assert settings_screen.message_box.blinking_label.visible


def test_settings_screen_clear(setup_pygame):
    screen, manager = setup_pygame
    back_button_callback = Mock()
    settings_screen = SettingsScreen(
        ui_manager=manager, back_button_callback=back_button_callback
    )
    settings_screen.activate()
    settings_screen.clear()

    assert not settings_screen.title_label.get_instance().visible
    assert not settings_screen.back_button.get_instance().visible
    assert not settings_screen.message_box.get_instance().visible
    assert not settings_screen.message_box.blinking_label.visible


def test_settings_screen_set_message(setup_pygame):
    screen, manager = setup_pygame
    back_button_callback = Mock()
    settings_screen = SettingsScreen(
        ui_manager=manager, back_button_callback=back_button_callback
    )
    new_message = "New settings message"
    settings_screen.message_box.set_message(new_message)

    assert settings_screen.message_box.message == new_message
    assert settings_screen.message_box.get_instance().html_text == new_message


def test_settings_screen_handle_event(setup_pygame):
    screen, manager = setup_pygame
    back_button_callback = Mock()
    settings_screen = SettingsScreen(
        ui_manager=manager, back_button_callback=back_button_callback
    )
    settings_screen.activate()

    click_event = pygame.event.Event(
        pygame.MOUSEBUTTONDOWN,
        {
            "pos": (
                settings_screen.message_box.position[0] + 1,
                settings_screen.message_box.position[1] + 1,
            ),
            "button": 1,
        },
    )
    settings_screen.handle_event(click_event)
    back_button_callback.assert_called_once()
