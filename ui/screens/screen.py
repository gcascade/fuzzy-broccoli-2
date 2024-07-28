from abc import ABC, abstractmethod

from pygame.event import Event


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

    @abstractmethod
    def clear(self) -> None:
        """
        Hide all elements of the screen.
        """
        pass

    @abstractmethod
    def handle_event(self, event: Event) -> None:
        """
        Handle an event by passing it to the screen's components.

        :param event: The event to handle.
        """
        pass

    @abstractmethod
    def activate(self) -> None:
        """
        Activate elements in the screen
        """
        pass
