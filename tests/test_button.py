from unittest.mock import Mock

import pygame
import pygame_gui
import pytest

from ui.components.button import Button
from ui.components.ui_manager import UIManager


@pytest.fixture
def setup_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    manager = UIManager(800, 600)
    yield screen, manager
    pygame.quit()


def test_button_initialization(setup_pygame):
    screen, manager = setup_pygame
    callback = Mock()
    button = Button(
        ui_manager=manager,
        text="Test Button",
        position=(100, 100),
        size=(200, 50),
        callback=callback,
    )

    assert button.ui_button.text == "Test Button"
    assert button.ui_button.relative_rect.topleft == (100, 100)
    assert button.ui_button.relative_rect.size == (200, 50)
    assert not button.ui_button.visible
    assert button.callback == callback


def test_button_show(setup_pygame):
    screen, manager = setup_pygame
    callback = Mock()
    button = Button(
        ui_manager=manager,
        text="Test Button",
        position=(100, 100),
        size=(200, 50),
        callback=callback,
    )
    button.show()
    assert button.ui_button.visible


def test_button_hide(setup_pygame):
    screen, manager = setup_pygame
    callback = Mock()
    button = Button(
        ui_manager=manager,
        text="Test Button",
        position=(100, 100),
        size=(200, 50),
        callback=callback,
    )
    button.show()
    button.hide()
    assert not button.ui_button.visible


def test_button_handle_event(setup_pygame):
    screen, manager = setup_pygame
    callback = Mock()
    button = Button(
        ui_manager=manager,
        text="Test Button",
        position=(100, 100),
        size=(200, 50),
        callback=callback,
    )

    button.show()
    event = pygame.event.Event(
        pygame_gui.UI_BUTTON_PRESSED, {"ui_element": button.ui_button}
    )
    button.handle_event(event)
    callback.assert_called_once()


def test_get_instance(setup_pygame):
    screen, manager = setup_pygame
    callback = Mock()
    button = Button(
        ui_manager=manager,
        text="Test Button",
        position=(100, 100),
        size=(200, 50),
        callback=callback,
    )

    assert isinstance(button.get_instance(), pygame_gui.elements.UIButton)
