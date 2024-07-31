from typing import Tuple

import pygame
import pygame_gui
from pygame.event import Event

from ui.components.element import Element
from ui.components.ui_manager import UIManager


class Image(Element):
    """
    A class to create and display a simple image in the game.
    """

    def __init__(
        self,
        ui_manager: UIManager,
        image_path: str,
        position: Tuple[int, int],
        size: Tuple[int, int],
    ):
        """
        Initialize a new SimpleImage.

        :param ui_manager: The UIManager instance managing this image.
        :param image_path: The path to the image file.
        :param position: The (x, y) position of the top-left corner of the image.
        :param size: The (width, height) size of the image.
        """
        super().__init__(ui_manager)
        self.ui_image = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect(position, size),
            image_surface=pygame.image.load(image_path).convert_alpha(),
            manager=ui_manager.get_instance(),
            visible=0,
        )

    def get_instance(self) -> pygame_gui.elements.UIImage:
        """
        Get the underlying pygame_gui UIImage instance.

        :return: The UIImage instance.
        """
        return self.ui_image

    def hide(self) -> None:
        """
        Hide the image.
        """
        self.ui_image.hide()

    def show(self) -> None:
        """
        Show the image.
        """
        self.ui_image.show()

    def handle_event(self, event: Event) -> None:
        """
        Handle an event. Images do not respond to events.

        :param event: The event to handle
        :return:
        """
        pass
