from typing import Callable, Optional, Tuple

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
        on_click: Optional[Callable[[], None]] = None,
        blinking_label: Optional[str] = None,
    ):
        """
        Initialize a new MessageBox.

        :param ui_manager: The UI manager for managing the message box.
        :param position: The (x, y) position of the top-left corner of the message box.
        :param size: The (width, height) size of the message box.
        :param message: The message to display in the message box.
        :param on_click: The function to call when the message box is clicked.
        """
        super().__init__(ui_manager)
        self.position = position
        self.size = size
        self.message = message
        self.on_click = on_click
        self.blinking = False
        self.blink_interval = 500  # milliseconds
        self.blink_time_accumulator = 0
        self.last_blink_time = pygame.time.get_ticks()
        self.has_blinking_label = blinking_label is not None

        rect = pygame.Rect(position, size)
        self.message_box = pygame_gui.elements.UITextBox(
            relative_rect=rect, html_text=message, manager=ui_manager.get_instance()
        )
        self.message_box.hide()

        if blinking_label:
            font = pygame.font.Font(None, 24)
            offset = (25, 10)
            text_width, text_height = font.size(blinking_label)
            label_position = (
                position[0] + size[0] - text_width - offset[0],
                position[1] + size[1] - text_height - offset[1],
            )
            label_size = (text_width + offset[0], text_height + offset[1])
            self.blinking_label = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect(label_position, label_size),
                text=blinking_label,
                manager=ui_manager.get_instance(),
            )
            self.blinking_label.hide()

    def get_instance(self):
        """
        Get the underlying pygame_gui UITextBox instance.

        :return: The UITextBox instance.
        """
        return self.message_box

    def show(self) -> None:
        """
        Show the message box and the blinking label.
        """
        self.message_box.show()
        if self.has_blinking_label:
            self.blinking_label.show()
            self.blinking = True

    def hide(self) -> None:
        """
        Hide the message box and the blinking label.
        """
        self.message_box.hide()
        if self.has_blinking_label:
            self.blinking_label.hide()
            self.blinking = False

    def set_message(self, message: str) -> None:
        """
        Set a new message for the message box.

        :param message: The new message to display.
        """
        self.message = message
        self.message_box.set_text(message)

    def set_blinking_label(self, label: str | None) -> None:
        """
        Set a new blinking label for the message box.

        :param label: The new label to display.
        """
        if label is None:
            self.blinking_label.hide()
            self.blinking = False
            self.has_blinking_label = False
        else:
            self.blinking_label.set_text(label)

    def handle_event(self, event):
        """
        Handle events for the message box. Triggers the callback on click.

        :param event: The event to handle.
        """
        if (
            event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
        ):  # Left mouse button
            if self.message_box.relative_rect.collidepoint(event.pos):
                if self.on_click:
                    self.on_click()

    def update(self, time_delta: float) -> None:
        """
        Update the state of the message box. Used for blinking the label.

        :param time_delta: Time passed since the last frame.
        """
        if self.blinking:
            self.blink_time_accumulator += int(
                time_delta * 1000
            )  # convert to milliseconds
            if self.blink_time_accumulator >= self.blink_interval:
                if self.blinking_label.visible:
                    self.blinking_label.hide()
                else:
                    self.blinking_label.show()
                self.blink_time_accumulator = 0
