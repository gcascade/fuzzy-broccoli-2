from unittest.mock import Mock

import pygame
import pygame_gui
import pytest

from ui.components.ui_manager import UIManager
from ui.screens.start_screen import StartScreen


@pytest.fixture
def setup_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    manager = UIManager(800, 600)
    yield screen, manager
    pygame.quit()


def test_start_screen_initialization(setup_pygame):
    screen, manager = setup_pygame
    start_game_callback = Mock()
    start_screen = StartScreen(
        ui_manager=manager,
        width=800,
        height=600,
        start_game_callback=start_game_callback,
    )

    assert start_screen.title_label.get_instance().text == "Fuzzy Broccoli 2"
    assert start_screen.start_button.get_instance().text == "Start Game"
    assert start_screen.title_label.get_instance().relative_rect.topleft == (250, 100)
    assert start_screen.start_button.get_instance().relative_rect.topleft == (350, 275)


def test_start_screen_clear(setup_pygame):
    screen, manager = setup_pygame
    start_game_callback = Mock()
    start_screen = StartScreen(
        ui_manager=manager,
        width=800,
        height=600,
        start_game_callback=start_game_callback,
    )
    start_screen.activate()
    start_screen.clear()

    assert not start_screen.title_label.get_instance().visible
    assert not start_screen.start_button.get_instance().visible


def test_start_screen_activate(setup_pygame):
    screen, manager = setup_pygame
    start_game_callback = Mock()
    start_screen = StartScreen(
        ui_manager=manager,
        width=800,
        height=600,
        start_game_callback=start_game_callback,
    )
    start_screen.activate()

    assert start_screen.title_label.get_instance().visible
    assert start_screen.start_button.get_instance().visible


def test_start_screen_handle_event(setup_pygame):
    screen, manager = setup_pygame
    start_game_callback = Mock()
    start_screen = StartScreen(
        ui_manager=manager,
        width=800,
        height=600,
        start_game_callback=start_game_callback,
    )
    start_screen.activate()

    event = pygame.event.Event(
        pygame_gui.UI_BUTTON_PRESSED,
        {"ui_element": start_screen.start_button.get_instance()},
    )
    start_screen.handle_event(event)
    start_game_callback.assert_called_once()
