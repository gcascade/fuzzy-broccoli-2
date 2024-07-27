from typing import Callable, Tuple

import pygame
import pygame_gui

from ui.components.ui_manager import UIManager


class Button:
    """
    A class to create and manage a button in the game.
    """

    def __init__(
        self,
        ui_manager: UIManager,
        text: str,
        position: Tuple[int, int],
        size: Tuple[int, int],
        callback: Callable[[], None],
    ):
        """
        Initialize a new Button.

        :param ui_manager: The UIManager instance managing this button.
        :param text: The text to display on the button.
        :param position: The (x, y) position of the top-left corner of the button.
        :param size: The (width, height) size of the button.
        :param callback: The function to call when the button is clicked.
        """
        self.ui_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(position, size),
            text=text,
            manager=ui_manager.get_instance(),
            visible=0,
        )
        self.callback = callback

    def get_instance(self) -> pygame_gui.elements.UIButton:
        """
        Get the underlying pygame_gui UIButton instance.

        :return: The UIButton instance.
        """
        return self.ui_button

    def hide(self) -> None:
        """
        Hide the button.
        """
        self.ui_button.hide()

    def show(self) -> None:
        """
        Show the button.
        """
        self.ui_button.show()

    def handle_event(self, event) -> None:
        """
        Handle an event and invoke the callback if the button is clicked.

        :param event: The event to handle.
        """
        if (
            event.type == pygame_gui.UI_BUTTON_PRESSED
            and event.ui_element == self.ui_button
        ):
            self.callback()
