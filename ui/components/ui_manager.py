from typing import Optional

import pygame
import pygame_gui
from pygame.event import Event

from core.config import Config
from ui.screens.screen import Screen


class UIManager:
    """
    A class to manage UI elements in the game.
    """

    def __init__(self, width: int, height: int):
        """
        Initialize the UIManager with a given screen width and height.

        :param width: The width of the screen.
        :param height: The height of the screen.
        """
        self.manager: pygame_gui.UIManager = pygame_gui.UIManager(
            (width, height), theme_path=Config.THEME_FILENAME
        )
        self.width: int = width
        self.height: int = height
        self.active_screen: Optional[Screen] = None

    def clear_screen(self) -> None:
        """
        Kill all UI elements managed by the manager.
        """
        self.manager.get_root_container().clear()

    def set_active_screen(self, screen: Screen):
        """
        Set the active screen

        :param screen: The screen to activate
        """
        if self.active_screen is not None:
            self.active_screen.clear()
        self.active_screen = screen
        if self.active_screen is not None:
            self.active_screen.activate()

    def draw_ui(self, screen: pygame.Surface) -> None:
        """
        Draw the UI elements on the screen.

        :param screen: The Pygame display surface.
        """
        self.manager.draw_ui(screen)

    def update(self, time_delta: float) -> None:
        """
        Update the UI elements.

        :param time_delta: The time since the last update.
        """
        self.manager.update(time_delta)

    def process_event(self, event: Event) -> None:
        """
        Process UI events.

        :param event: The event to process.
        """
        self.manager.process_events(event)
        if self.active_screen is not None:
            self.active_screen.handle_event(event)

    def get_instance(self) -> pygame_gui.UIManager:
        """
        Get the underlying pygame_gui.UIManager.

        :return: The pygame_gui.UIManager instance.
        """
        return self.manager

    def get_height(self) -> int:
        """
        Get the height of the screen.

        :return: The height of the screen.
        """
        return self.height

    def get_width(self) -> int:
        """
        Get the width of the screen.

        :return: The width of the screen.
        """
        return self.width
