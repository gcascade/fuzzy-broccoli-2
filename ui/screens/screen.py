from abc import ABC, abstractmethod

from pygame.event import Event


class Screen(ABC):
    """
    A base class to represent a generic screen in the game.

    Attributes:
    ui_manager (UIManager): The UIManager instance managing this screen.
    width (int): The width of the screen.
    height (int): The height of the screen.
    """

    def __init__(self, ui_manager, width: int, height: int):
        """
        Initialize the base screen.

        :param ui_manager: The UIManager instance managing this screen.
        :param width: The width of the screen.
        :param height: The height of the screen.
        """
        self.ui_manager = ui_manager
        self.width = width
        self.height = height

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
