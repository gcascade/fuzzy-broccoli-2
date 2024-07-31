from abc import ABC, abstractmethod

from pygame.event import Event


class Element(ABC):
    """
    A base class to represent a generic element in the game.

    Attributes:
    ui_manager (UIManager): The UIManager instance managing this screen.
    """

    def __init__(self, ui_manager):
        """
        Initialize the base element.

        :param ui_manager: The UIManager instance managing this element.
        """
        self.ui_manager = ui_manager

    @abstractmethod
    def hide(self) -> None:
        """
        Hide the element.
        """
        pass

    @abstractmethod
    def show(self) -> None:
        """
        Show the element.
        """
        pass

    @abstractmethod
    def handle_event(self, event: Event) -> None:
        """
        Handle an event.

        :param event: The event to handle.
        """
        pass
