import pygame
import pygame_gui
import pytest

from ui.components.ui_manager import UIManager
from ui.screens.screen import Screen


class MockScreen(Screen):
    def clear(self):
        pass

    def handle_event(self, event):
        pass

    def activate(self):
        pass


@pytest.fixture
def setup_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    manager = UIManager(800, 600)
    yield screen, manager
    pygame.quit()


def test_ui_manager_initialization(setup_pygame):
    screen, manager = setup_pygame
    assert isinstance(manager.get_instance(), pygame_gui.UIManager)
    assert manager.width == 800
    assert manager.height == 600
    assert manager.active_screen is None


def test_ui_manager_clear_screen(setup_pygame):
    screen, manager = setup_pygame
    pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((100, 100), (200, 50)),
        text="Test Label",
        manager=manager.get_instance(),
    )
    manager.clear_screen()
    assert len(manager.get_instance().get_root_container().elements) == 0


def test_ui_manager_set_active_screen(setup_pygame):
    screen, manager = setup_pygame
    mock_screen = MockScreen(manager, 800, 600)
    mock_screen2 = MockScreen(manager, 800, 600)
    manager.set_active_screen(mock_screen)
    assert manager.active_screen == mock_screen
    manager.set_active_screen(mock_screen2)
    assert manager.active_screen == mock_screen2


def test_ui_manager_draw_ui(setup_pygame):
    screen, manager = setup_pygame
    manager.draw_ui(screen)
    # No exception means it passed


def test_ui_manager_update(setup_pygame):
    screen, manager = setup_pygame
    manager.update(0.016)
    # No exception means it passed


def test_ui_manager_process_event(setup_pygame):
    screen, manager = setup_pygame
    mock_screen = MockScreen(manager, 800, 600)
    manager.set_active_screen(mock_screen)
    event = pygame.event.Event(pygame.USEREVENT, {})
    manager.process_event(event)
    # No exception means it passed


def test_get_instance(setup_pygame):
    screen, manager = setup_pygame

    assert isinstance(manager.get_instance(), pygame_gui.UIManager)
