import pygame
import pygame_gui
import pytest

from scripts.ui import create_start_screen, create_ui_manager


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
