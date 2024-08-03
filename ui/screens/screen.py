from abc import ABC
from typing import List

from pygame.event import Event

from ui.components.element import Element


class Screen(ABC):
    """
    A base class to represent a generic screen in the game.

    Attributes:
    ui_manager (UIManager): The UIManager instance managing this screen.
    """

    def __init__(self, ui_manager):
        """
        Initialize the base screen.

        :param ui_manager: The UIManager instance managing this screen.
        """
        self.ui_manager = ui_manager
        self.elements: List[Element] = []

    def clear(self) -> None:
        """
        Hide all elements of the screen.
        """
        for element in self.elements:
            element.hide()

    def handle_event(self, event: Event) -> None:
        """
        Handle an event by passing it to the screen's components.

        :param event: The event to handle.
        """
        for element in self.elements:
            element.handle_event(event)

    def activate(self) -> None:
        """
        Activate elements in the screen.
        """
        for element in self.elements:
            element.show()
