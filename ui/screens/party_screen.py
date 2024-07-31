from typing import Callable

from classes.character.character import Character
from classes.job.novice import Novice
from classes.job.student import Student
from ui.components.button import Button
from ui.components.character_summary import CharacterSummary
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

        character_size = (200, 200)
        character_number = 4
        character_gap = (0.9 * width - character_size[0] * character_number) / (
            character_number - 1
        )
        character_space = int(character_gap + character_size[0])
        x = int(5 / 100 * width)
        y = int(2.5 / 12 * height)

        self.title_label = Label(
            ui_manager=ui_manager,
            position=title_position,
            size=title_size,
            text="Party",
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
            message="This is the party screen!\nHere you can view your party members.",
        )

        character_1 = Character(
            name="Elaine",
            level=99,
            current_job=Novice(),
            xp=0,
            image_path="assets/images/characters/female_adventurer_1.png",
        )

        character_2 = Character(
            name="Arianne",
            level=1,
            current_job=Student(),
            xp=0,
            image_path="assets/images/characters/female_adventurer_2.png",
        )

        character_3 = Character(
            name="Magnus",
            level=1,
            current_job=Student(),
            xp=0,
            image_path="assets/images/characters/male_adventurer_1.png",
        )

        character_4 = Character(
            name="Roland",
            level=1,
            current_job=Novice(),
            xp=0,
            image_path="assets/images/characters/male_adventurer_2.png",
        )

        self.character_1_summary = CharacterSummary(
            character=character_1,
            ui_manager=ui_manager,
            position=(x, y),
            size=character_size,
        )

        self.character_2_summary = CharacterSummary(
            character=character_2,
            ui_manager=ui_manager,
            position=(x + character_space, y),
            size=character_size,
        )

        self.character_3_summary = CharacterSummary(
            character=character_3,
            ui_manager=ui_manager,
            position=(x + 2 * character_space, y),
            size=character_size,
        )

        self.character_4_summary = CharacterSummary(
            character=character_4,
            ui_manager=ui_manager,
            position=(x + 3 * character_space, y),
            size=character_size,
        )

        self.elements.append(self.title_label)
        self.elements.append(self.back_button)
        self.elements.append(self.message_box)
        self.elements.append(self.character_1_summary)
        self.elements.append(self.character_2_summary)
        self.elements.append(self.character_3_summary)
        self.elements.append(self.character_4_summary)
