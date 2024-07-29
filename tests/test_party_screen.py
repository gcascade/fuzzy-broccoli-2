from unittest.mock import Mock

import pygame
import pygame_gui
import pytest

from ui.components.ui_manager import UIManager
from ui.screens.party_screen import PartyScreen


@pytest.fixture
def setup_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    manager = UIManager(800, 600)
    yield screen, manager
    pygame.quit()


def test_party_screen_initialization(setup_pygame):
    screen, manager = setup_pygame
    back_button_callback = Mock()
    party_screen = PartyScreen(
        ui_manager=manager, back_button_callback=back_button_callback
    )

    assert party_screen.title_label.get_instance().text == "Party"
    assert party_screen.back_button.get_instance().text == "Back"
    assert (
        party_screen.message_box.get_instance().html_text
        == "This is the party screen!\nHere you can view your party members."
    )


def test_party_screen_clear(setup_pygame):
    screen, manager = setup_pygame
    back_button_callback = Mock()
    party_screen = PartyScreen(
        ui_manager=manager, back_button_callback=back_button_callback
    )
    party_screen.activate()
    party_screen.clear()

    assert not party_screen.title_label.get_instance().visible
    assert not party_screen.back_button.get_instance().visible
    assert not party_screen.message_box.get_instance().visible


def test_party_screen_activate(setup_pygame):
    screen, manager = setup_pygame
    back_button_callback = Mock()
    party_screen = PartyScreen(
        ui_manager=manager, back_button_callback=back_button_callback
    )
    party_screen.activate()

    assert party_screen.title_label.get_instance().visible
    assert party_screen.back_button.get_instance().visible
    assert party_screen.message_box.get_instance().visible


def test_party_screen_handle_event(setup_pygame):
    screen, manager = setup_pygame
    back_button_callback = Mock()
    party_screen = PartyScreen(
        ui_manager=manager, back_button_callback=back_button_callback
    )
    party_screen.activate()

    back_event = pygame.event.Event(
        pygame_gui.UI_BUTTON_PRESSED,
        {"ui_element": party_screen.back_button.get_instance()},
    )
    party_screen.handle_event(back_event)
    back_button_callback.assert_called_once()
