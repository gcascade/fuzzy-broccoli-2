from typing import Callable

from ui.components.button import Button
from ui.components.label import Label
from ui.components.message_box import MessageBox
from ui.components.ui_manager import UIManager
from ui.screens.screen import Screen


class SettingsScreen(Screen):
    """
    A class to represent the settings screen of the game.
    """

    def __init__(self, ui_manager: UIManager, back_button_callback: Callable[[], None]):
        """
        Initialize the settings screen elements.

        :param ui_manager: The UIManager instance managing this screen.
        :param back_button_callback: The function to call when the back button is clicked.
        """
        super().__init__(ui_manager)
        width = ui_manager.get_width()
        height = ui_manager.get_height()

        # Constants for layout
        title_position = (int(width // 2 - (3 / 8 * width) // 2), int(1 / 12 * height))
        title_size = (int(3 / 8 * width), int(1 / 12 * height))
        back_button_position = (
            int(15 / 16 * width) - int(1 / 8 * width),
            int(1 / 12 * height),
        )
        back_button_size = (int(1 / 8 * width), int(1 / 12 * height))
        message_box_position = (
            int(width // 2 - (9 / 10 * width) // 2),
            int(2 / 3 * height),
        )
        message_box_size = (int(9 / 10 * width), int(1 / 4 * height))

        self.title_label = Label(
            ui_manager=ui_manager,
            position=title_position,
            size=title_size,
            text="Settings",
        )

        self.back_button = Button(
            ui_manager=ui_manager,
            text="Back",
            position=back_button_position,
            size=back_button_size,
            callback=back_button_callback,
        )

        self.message_box = MessageBox(
            ui_manager=ui_manager,
            position=message_box_position,
            size=message_box_size,
            message="Not implemented yet!",
            on_click=back_button_callback,
            blinking_label="Click to continue...",
        )

        self.elements.append(self.title_label)
        self.elements.append(self.back_button)
        self.elements.append(self.message_box)
