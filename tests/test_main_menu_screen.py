from unittest.mock import Mock

import pygame
import pygame_gui
import pytest

from ui.components.ui_manager import UIManager
from ui.screens.main_menu_screen import MainMenuScreen


@pytest.fixture
def setup_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    manager = UIManager(800, 600)
    yield screen, manager
    pygame.quit()


def test_main_menu_screen_initialization(setup_pygame):
    screen, manager = setup_pygame
    callbacks = {
        "play": Mock(),
        "view_party": Mock(),
        "settings": Mock(),
        "quit": Mock(),
    }
    main_menu_screen = MainMenuScreen(
        ui_manager=manager,
        width=800,
        height=600,
        callbacks=callbacks,
    )

    assert main_menu_screen.play_button.get_instance().text == "Play"
    assert main_menu_screen.view_party_button.get_instance().text == "View Party"
    assert main_menu_screen.settings_button.get_instance().text == "Settings"
    assert main_menu_screen.quit_button.get_instance().text == "Quit"


def test_main_menu_screen_clear(setup_pygame):
    screen, manager = setup_pygame
    callbacks = {
        "play": Mock(),
        "view_party": Mock(),
        "settings": Mock(),
        "quit": Mock(),
    }
    main_menu_screen = MainMenuScreen(
        ui_manager=manager,
        width=800,
        height=600,
        callbacks=callbacks,
    )
    main_menu_screen.activate()
    main_menu_screen.clear()

    assert not main_menu_screen.play_button.get_instance().visible
    assert not main_menu_screen.view_party_button.get_instance().visible
    assert not main_menu_screen.settings_button.get_instance().visible
    assert not main_menu_screen.quit_button.get_instance().visible


def test_main_menu_screen_activate(setup_pygame):
    screen, manager = setup_pygame
    callbacks = {
        "play": Mock(),
        "view_party": Mock(),
        "settings": Mock(),
        "quit": Mock(),
    }
    main_menu_screen = MainMenuScreen(
        ui_manager=manager,
        width=800,
        height=600,
        callbacks=callbacks,
    )
    main_menu_screen.activate()

    assert main_menu_screen.play_button.get_instance().visible
    assert main_menu_screen.view_party_button.get_instance().visible
    assert main_menu_screen.settings_button.get_instance().visible
    assert main_menu_screen.quit_button.get_instance().visible


def test_main_menu_screen_handle_event(setup_pygame):
    screen, manager = setup_pygame
    callbacks = {
        "play": Mock(),
        "view_party": Mock(),
        "settings": Mock(),
        "quit": Mock(),
    }
    main_menu_screen = MainMenuScreen(
        ui_manager=manager,
        width=800,
        height=600,
        callbacks=callbacks,
    )
    main_menu_screen.activate()

    play_event = pygame.event.Event(
        pygame_gui.UI_BUTTON_PRESSED,
        {"ui_element": main_menu_screen.play_button.get_instance()},
    )
    main_menu_screen.handle_event(play_event)
    callbacks["play"].assert_called_once()

    view_party_event = pygame.event.Event(
        pygame_gui.UI_BUTTON_PRESSED,
        {"ui_element": main_menu_screen.view_party_button.get_instance()},
    )
    main_menu_screen.handle_event(view_party_event)
    callbacks["view_party"].assert_called_once()

    settings_event = pygame.event.Event(
        pygame_gui.UI_BUTTON_PRESSED,
        {"ui_element": main_menu_screen.settings_button.get_instance()},
    )
    main_menu_screen.handle_event(settings_event)
    callbacks["settings"].assert_called_once()

    quit_event = pygame.event.Event(
        pygame_gui.UI_BUTTON_PRESSED,
        {"ui_element": main_menu_screen.quit_button.get_instance()},
    )
    main_menu_screen.handle_event(quit_event)
    callbacks["quit"].assert_called_once()
