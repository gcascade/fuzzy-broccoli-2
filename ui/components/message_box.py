from typing import Tuple

import pygame
import pygame_gui

from ui.components.element import Element
from ui.components.ui_manager import UIManager


class MessageBox(Element):
    """
    A class to create and manage a message box in the game.
    """

    def __init__(
        self,
        ui_manager: UIManager,
        position: Tuple[int, int],
        size: Tuple[int, int],
        message: str,
    ):
        """
        Initialize a new MessageBox.

        :param ui_manager: The UI manager for managing the message box.
        :param position: The (x, y) position of the top-left corner of the message box.
        :param size: The (width, height) size of the message box.
        :param message: The message to display in the message box.
        """
        super().__init__(ui_manager)
        self.position = position
        self.size = size
        self.message = message
        rect = pygame.Rect(position, size)
        self.message_box = pygame_gui.elements.UITextBox(
            relative_rect=rect, html_text=message, manager=ui_manager.get_instance()
        )
        self.message_box.hide()

    def get_instance(self):
        """
        Get the underlying pygame_gui UITextBox instance.

        :return: The UITextBox instance.
        """
        return self.message_box

    def show(self) -> None:
        """
        Show the message box.
        """
        self.message_box.show()

    def hide(self) -> None:
        """
        Hide the message box.
        """
        self.message_box.hide()

    def set_message(self, message: str) -> None:
        """
        Set a new message for the message box.

        :param message: The new message to display.
        """
        self.message = message
        self.message_box.set_text(message)

    def handle_event(self, event):
        """
        Handle events for the message box. Message boxes do not respond to events.

        :param event: The event to handle.
        """
        pass
