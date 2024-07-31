from typing import Tuple

import pygame
import pygame_gui
import pygame_gui.elements
from pygame.event import Event

from ui.components.element import Element
from ui.components.ui_manager import UIManager


class Label(Element):
    """
    A class to create and manage a label in the game.
    """

    def __init__(
        self,
        ui_manager: UIManager,
        text: str,
        position: Tuple[int, int],
        size: Tuple[int, int],
    ):
        """
        Initialize a new Label.

        :param ui_manager: The UIManager instance managing this label.
        :param text: The text to display on the label.
        :param position: The (x, y) position of the top-left corner of the label.
        :param size: The (width, height) size of the label.
        """
        super().__init__(ui_manager)
        self.ui_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(position, size),
            text=text,
            manager=ui_manager.get_instance(),
            visible=0,
        )

    def get_instance(self) -> pygame_gui.elements.UILabel:
        """
        Get the underlying pygame_gui UILabel instance.

        :return: The UILabel instance.
        """
        return self.ui_label

    def hide(self) -> None:
        """
        Hide the label.
        """
        self.ui_label.hide()

    def show(self) -> None:
        """
        Show the label.
        """
        self.ui_label.show()

    def handle_event(self, event: Event) -> None:
        """
        Handle an event. (Labels typically don't handle events, so this might be a pass.)

        :param event: The event to handle.
        """
        pass
