import pygame
import pygame_gui
import pytest

from scripts.ui import create_main_menu, create_start_screen, create_ui_manager


@pytest.fixture
def setup_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    manager = create_ui_manager(800, 600)
    yield screen, manager
    pygame.quit()


def test_create_ui_manager(setup_pygame):
    screen, manager = setup_pygame
    assert isinstance(manager, pygame_gui.UIManager)


def test_create_start_screen(setup_pygame):
    screen, manager = setup_pygame
    title_label, start_button = create_start_screen(manager)

    assert title_label.text == "Fuzzy Broccoli 2"
    assert start_button.text == "Start Game"
    assert title_label.relative_rect.topleft == (250, 100)
    assert start_button.relative_rect.topleft == (350, 275)


def test_create_main_menu(setup_pygame):
    screen, manager = setup_pygame
    menu_buttons = create_main_menu(manager)

    assert menu_buttons["play"].text == "Play"
    assert menu_buttons["view_party"].text == "View Party"
    assert menu_buttons["settings"].text == "Settings"
    assert menu_buttons["quit"].text == "Quit"

    assert menu_buttons["play"].relative_rect.topleft == (350, 200)
    assert menu_buttons["view_party"].relative_rect.topleft == (350, 275)
    assert menu_buttons["settings"].relative_rect.topleft == (350, 350)
    assert menu_buttons["quit"].relative_rect.topleft == (350, 425)

    # Ensure buttons are initially invisible
    assert not menu_buttons["play"].visible
    assert not menu_buttons["view_party"].visible
    assert not menu_buttons["settings"].visible
    assert not menu_buttons["quit"].visible

    # Make buttons visible and check again
    for button in menu_buttons.values():
        button.show()

    assert menu_buttons["play"].visible
    assert menu_buttons["view_party"].visible
    assert menu_buttons["settings"].visible
    assert menu_buttons["quit"].visible
