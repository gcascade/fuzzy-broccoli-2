import pygame
import pygame_gui
import pytest

from ui.components.message_box import MessageBox
from ui.components.ui_manager import UIManager


@pytest.fixture
def setup_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    manager = UIManager(800, 600)
    yield screen, manager
    pygame.quit()


def test_message_box_initialization(setup_pygame):
    screen, manager = setup_pygame
    message_box = MessageBox(
        ui_manager=manager, position=(100, 100), size=(300, 150), message="Test Message"
    )

    assert message_box.message == "Test Message"
    assert message_box.message_box.relative_rect.topleft == (100, 100)
    assert message_box.message_box.relative_rect.size == (300, 150)
    assert not message_box.message_box.visible


def test_message_box_show(setup_pygame):
    screen, manager = setup_pygame
    message_box = MessageBox(
        ui_manager=manager, position=(100, 100), size=(300, 150), message="Test Message"
    )
    message_box.show()
    assert message_box.message_box.visible


def test_message_box_hide(setup_pygame):
    screen, manager = setup_pygame
    message_box = MessageBox(
        ui_manager=manager, position=(100, 100), size=(300, 150), message="Test Message"
    )
    message_box.show()
    message_box.hide()
    assert not message_box.message_box.visible


def test_message_box_set_message(setup_pygame):
    screen, manager = setup_pygame
    message_box = MessageBox(
        ui_manager=manager, position=(100, 100), size=(300, 150), message="Test Message"
    )
    new_message = "New Test Message"
    message_box.set_message(new_message)
    assert message_box.message == new_message
    assert message_box.message_box.html_text == new_message


def test_get_instance(setup_pygame):
    screen, manager = setup_pygame
    message_box = MessageBox(
        ui_manager=manager, position=(100, 100), size=(300, 150), message="Test Message"
    )

    assert isinstance(message_box.get_instance(), pygame_gui.elements.UITextBox)
