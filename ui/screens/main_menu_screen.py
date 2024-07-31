from typing import Callable

from ui.components.button import Button
from ui.components.ui_manager import UIManager
from ui.screens.screen import Screen


class MainMenuScreen(Screen):
    """
    A class to represent the main menu screen of the game.
    """

    def __init__(
        self,
        ui_manager: UIManager,
        callbacks: dict[str, Callable[[], None]],
    ):
        """
        Initialize the main menu screen elements.

        :param ui_manager: The UIManager instance managing this screen.
        :param callbacks: A dictionary of callbacks for the buttons.
        """
        super().__init__(ui_manager)
        height = ui_manager.get_height()
        width = ui_manager.get_width()

        button_width = int(1 / 8 * width)
        button_height = int(1 / 12 * height)

        num_buttons = 4
        total_button_height = num_buttons * button_height
        min_spacing = 10
        available_height = height - total_button_height
        calculated_spacing = max(min_spacing, available_height // (num_buttons + 1))

        start_y = (
            height - total_button_height - (calculated_spacing * (num_buttons - 1))
        ) // 2
        start_x = (width - button_width) // 2

        self.play_button = Button(
            ui_manager=ui_manager,
            text="Play",
            position=(start_x, start_y),
            size=(button_width, button_height),
            callback=callbacks["play"],
        )

        self.view_party_button = Button(
            ui_manager=ui_manager,
            text="View Party",
            position=(start_x, start_y + button_height + calculated_spacing),
            size=(button_width, button_height),
            callback=callbacks["view_party"],
        )

        self.settings_button = Button(
            ui_manager=ui_manager,
            text="Settings",
            position=(start_x, start_y + 2 * (button_height + calculated_spacing)),
            size=(button_width, button_height),
            callback=callbacks["settings"],
        )

        self.quit_button = Button(
            ui_manager=ui_manager,
            text="Quit",
            position=(start_x, start_y + 3 * (button_height + calculated_spacing)),
            size=(button_width, button_height),
            callback=callbacks["quit"],
        )

        self.elements.append(self.play_button)
        self.elements.append(self.view_party_button)
        self.elements.append(self.settings_button)
        self.elements.append(self.quit_button)
