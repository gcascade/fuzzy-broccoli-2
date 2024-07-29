from typing import Callable

from pygame.event import Event

from ui.components.button import Button
from ui.components.label import Label
from ui.components.message_box import MessageBox
from ui.components.ui_manager import UIManager
from ui.screens.screen import Screen


class PartyScreen(Screen):
    """
    A class to represent the party screen of the game.
    """

    def __init__(self, ui_manager: UIManager, back_button_callback: Callable[[], None]):
        """
        Initialize the party screen elements.

        :param ui_manager: The UIManager instance managing this screen.
        :param back_button_callback: The function to call when the back button is clicked.
        """
        super().__init__(ui_manager)
        width = ui_manager.get_width()
        height = ui_manager.get_height()
        self.title_label = Label(
            ui_manager=ui_manager,
            position=(int(width // 2 - (3 / 8 * width) // 2), int(1 / 12 * height)),
            size=(int(3 / 8 * width), int(1 / 12 * height)),
            text="Party",
        )

        self.back_button = Button(
            ui_manager=ui_manager,
            text="Back",
            position=(int(15 / 16 * width) - int(1 / 8 * width), int(1 / 12 * height)),
            size=(int(1 / 8 * width), int(1 / 12 * height)),
            callback=back_button_callback,
        )

        self.message_box = MessageBox(
            ui_manager=ui_manager,
            position=(int(width // 2 - (9 / 10 * width) // 2), int(2 / 3 * height)),
            size=(int(9 / 10 * width), int(1 / 4 * height)),
            message="This is the party screen!\nHere you can view your party members.",
        )

    def clear(self) -> None:
        """
        Hide all elements of the party screen.
        """
        self.title_label.hide()
        self.back_button.hide()
        self.message_box.hide()

    def handle_event(self, event: Event) -> None:
        """
        Handle an event by passing it to the back button.

        :param event: The event to handle.
        """
        self.back_button.handle_event(event)

    def activate(self) -> None:
        """
        Show all elements of the party screen.
        """
        self.title_label.show()
        self.back_button.show()
        self.message_box.show()
