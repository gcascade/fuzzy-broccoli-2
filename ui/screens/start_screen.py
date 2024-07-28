from typing import Callable

from pygame.event import Event

from ui.components.button import Button
from ui.components.label import Label
from ui.components.ui_manager import UIManager
from ui.screens.screen import Screen


class StartScreen(Screen):
    """
    A class to represent the start screen of the game.
    """

    def __init__(
        self,
        ui_manager: UIManager,
        start_game_callback: Callable[[], None],
    ):
        """
        Initialize the start screen elements.

        :param ui_manager: The UIManager instance managing this screen.
        :param start_game_callback: The function to call when the start button is clicked.
        """
        super().__init__(ui_manager)
        width = ui_manager.get_width()
        height = ui_manager.get_height()
        self.title_label = Label(
            ui_manager=ui_manager,
            position=(int(5 / 16 * width), int(1 / 6 * height)),
            size=(int(3 / 8 * width), int(1 / 12 * height)),
            text="Fuzzy Broccoli 2",
        )

        self.start_button = Button(
            ui_manager=ui_manager,
            text="Start Game",
            position=(int(7 / 16 * width), int(11 / 24 * height)),
            size=(int(1 / 8 * width), int(1 / 12 * height)),
            callback=start_game_callback,
        )

    def clear(self) -> None:
        """
        Hide all elements of the start screen.
        """
        self.title_label.hide()
        self.start_button.hide()

    def handle_event(self, event: Event) -> None:
        """
        Handle an event by passing it to the start button.

        :param event: The event to handle.
        """
        self.start_button.handle_event(event)

    def activate(self) -> None:
        """
        Activate elements in the screen
        """
        self.title_label.show()
        self.start_button.show()
