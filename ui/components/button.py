from typing import Callable, Optional, Tuple

import pygame
import pygame_gui

from ui.components.element import Element
from ui.components.ui_manager import UIManager


class Button(Element):
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
        on_hover: Optional[Callable[[], None]] = None,
        on_hover_out: Optional[Callable[[], None]] = None,
        image_path: Optional[str] = None,
    ):
        """
        Initialize a new Button.

        :param ui_manager: The UIManager instance managing this button.
        :param text: The text to display on the button.
        :param position: The (x, y) position of the top-left corner of the button.
        :param size: The (width, height) size of the button.
        :param callback: The function to call when the button is clicked.
        :param on_hover: The function to call when the mouse hovers over the button.
        :param on_hover_out: The function to call when the mouse leaves the button.
        """
        super().__init__(ui_manager)
        self.ui_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(position, size),
            text=text,
            manager=ui_manager.get_instance(),
            visible=0,
        )
        if image_path:
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, size)
            self.ui_button.normal_image = image
            self.ui_button.hovered_image = image
            self.ui_button.selected_image = image
            self.ui_button.disabled_image = image
            self.ui_button.set_image(image)
            self.ui_button.rebuild()
        self.callback = callback
        self.on_hover = on_hover
        self.on_hover_out = on_hover_out
        self.hovering = False

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
        elif event.type == pygame.MOUSEMOTION:
            if self.ui_button.relative_rect.collidepoint(event.pos):
                if not self.hovering and self.on_hover:
                    self.on_hover()
                    self.hovering = True
            else:
                if self.hovering and self.on_hover_out:
                    self.on_hover_out()
                self.hovering = False

    def update(self, time_delta):
        """
        Update the button.
        :param time_delta: The time since the last update.
        """
        pass
