from abc import ABC
from typing import TYPE_CHECKING, List

from pygame.event import Event

if TYPE_CHECKING:
    from ui.components.element import Element
    from ui.components.ui_manager import UIManager


class Screen(ABC):
    """
    A base class to represent a generic screen in the game.

    Attributes:
    ui_manager (UIManager): The UIManager instance managing this screen.
    """

    def __init__(self, ui_manager: "UIManager"):
        """
        Initialize the base screen.

        :param ui_manager: The UIManager instance managing this screen.
        """
        self.ui_manager = ui_manager
        self.elements: List["Element"] = []

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

    def update(self, time_delta: float) -> None:
        """
        Update the screen elements.

        :param time_delta: The time since the last update.
        """
        for element in self.elements:
            element.update(time_delta)
