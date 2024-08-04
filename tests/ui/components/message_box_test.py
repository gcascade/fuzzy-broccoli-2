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
    assert message_box.has_blinking_label is False


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


def test_message_box_with_blinking_label_initialization(setup_pygame):
    screen, manager = setup_pygame
    message_box = MessageBox(
        ui_manager=manager,
        position=(100, 100),
        size=(300, 150),
        message="Test Message",
        blinking_label="click to continue...",
    )

    assert message_box.message == "Test Message"
    assert message_box.message_box.relative_rect.topleft == (100, 100)
    assert message_box.message_box.relative_rect.size == (300, 150)
    assert not message_box.message_box.visible
    assert message_box.blinking_label.text == "click to continue..."
    assert not message_box.blinking_label.visible
    assert message_box.has_blinking_label is True


def test_message_box_blinking_label_show(setup_pygame):
    screen, manager = setup_pygame
    message_box = MessageBox(
        ui_manager=manager,
        position=(100, 100),
        size=(300, 150),
        message="Test Message",
        blinking_label="click to continue...",
    )
    message_box.show()
    assert message_box.message_box.visible
    assert message_box.blinking_label.visible


def test_message_box_blinking_label_hide(setup_pygame):
    screen, manager = setup_pygame
    message_box = MessageBox(
        ui_manager=manager,
        position=(100, 100),
        size=(300, 150),
        message="Test Message",
        blinking_label="click to continue...",
    )
    message_box.show()
    message_box.hide()
    assert not message_box.message_box.visible
    assert not message_box.blinking_label.visible


def test_message_box_set_blinking_label(setup_pygame):
    screen, manager = setup_pygame
    message_box = MessageBox(
        ui_manager=manager,
        position=(100, 100),
        size=(300, 150),
        message="Test Message",
        blinking_label="click to continue...",
    )
    new_label = "New Label"
    message_box.set_blinking_label(new_label)
    assert message_box.blinking_label.text == new_label


def test_message_box_set_blinking_label_without_label(setup_pygame):
    screen, manager = setup_pygame
    message_box = MessageBox(
        ui_manager=manager,
        position=(100, 100),
        size=(300, 150),
        message="Test Message",
        blinking_label="click to continue...",
    )
    message_box.set_blinking_label(None)
    assert message_box.blinking_label.visible == 0
    assert message_box.has_blinking_label is False
    assert message_box.blinking is False


def test_message_box_update(setup_pygame):
    screen, manager = setup_pygame
    message_box = MessageBox(
        ui_manager=manager,
        position=(100, 100),
        size=(300, 150),
        message="Test Message",
        blinking_label="click to continue...",
    )
    message_box.show()
    message_box.update(500)
    assert message_box.message_box.visible == 1
    assert message_box.blinking_label.visible == 0
    message_box.update(500)
    assert message_box.message_box.visible == 1
    assert message_box.blinking_label.visible == 1
