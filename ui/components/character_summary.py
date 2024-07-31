from typing import Tuple

from pygame.event import Event

from ui.components.element import Element
from ui.components.image import Image
from ui.components.label import Label
from ui.components.ui_manager import UIManager


class CharacterSummary(Element):
    """
    A class to display a character summary including an image and text labels.
    """

    def __init__(
        self,
        character,
        ui_manager: UIManager,
        position: Tuple[int, int],
        size: Tuple[int, int],
    ):
        """
        Initialize the character summary.

        :param character: The character instance.
        :param ui_manager: The UIManager instance managing this summary.
        :param position: The (x, y) position of the top-left corner of the summary.
        :param size: The (width, height) size of the image.
        """
        super().__init__(ui_manager)
        self.character = character
        self.image = Image(ui_manager, character.get_image_path(), position, size)

        label_width = size[0]
        label_height = 24
        x, y = position

        self.character_name = Label(
            ui_manager,
            character.get_name(),
            (x, y + size[1] + 5),
            (label_width, label_height),
        )
        self.character_level = Label(
            ui_manager,
            f"Level: {character.get_level()}",
            (x, y + size[1] + 5 + label_height),
            (label_width, label_height),
        )
        self.character_job = Label(
            ui_manager,
            f"Job: {character.get_job().get_name()}",
            (x, y + size[1] + 5 + 2 * label_height),
            (label_width, label_height),
        )
        self.character_job_level = Label(
            ui_manager,
            f"Job Level: {character.get_job().get_level()}",
            (x, y + size[1] + 5 + 3 * label_height),
            (label_width, label_height),
        )
        self.elements = [
            self.image,
            self.character_name,
            self.character_level,
            self.character_job,
            self.character_job_level,
        ]

    def hide(self):
        """
        Hide all elements of the character summary.
        """
        for element in self.elements:
            element.hide()

    def show(self):
        """
        Show all elements of the character summary.
        """
        for element in self.elements:
            element.show()

    def handle_event(self, event: Event) -> None:
        """
        Handle an event for the character summary.

        :param event: The event to handle.
        """
        for element in self.elements:
            element.handle_event(event)
