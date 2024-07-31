import pygame
import pygame_gui
import pytest

from ui.components.label import Label
from ui.components.ui_manager import UIManager


@pytest.fixture
def setup_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    manager = UIManager(800, 600)
    yield screen, manager
    pygame.quit()


def test_label_initialization(setup_pygame):
    screen, manager = setup_pygame
    label = Label(
        ui_manager=manager, text="Test Label", position=(100, 100), size=(200, 50)
    )

    assert label.ui_label.text == "Test Label"
    assert label.ui_label.relative_rect.topleft == (100, 100)
    assert label.ui_label.relative_rect.size == (200, 50)
    assert not label.ui_label.visible


def test_label_show(setup_pygame):
    screen, manager = setup_pygame
    label = Label(
        ui_manager=manager, text="Test Label", position=(100, 100), size=(200, 50)
    )
    label.show()
    assert label.ui_label.visible


def test_label_hide(setup_pygame):
    screen, manager = setup_pygame
    label = Label(
        ui_manager=manager, text="Test Label", position=(100, 100), size=(200, 50)
    )
    label.show()
    label.hide()
    assert not label.ui_label.visible


def test_get_instance(setup_pygame):
    screen, manager = setup_pygame
    label = Label(
        ui_manager=manager, text="Test Label", position=(100, 100), size=(200, 50)
    )

    assert isinstance(label.get_instance(), pygame_gui.elements.UILabel)
