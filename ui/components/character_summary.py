from typing import Tuple

from ui.components.image import Image
from ui.components.label import Label
from ui.components.ui_manager import UIManager


class CharacterSummary:
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
        self.character = character
        self.ui_manager = ui_manager
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

    def hide(self):
        """
        Hide all elements of the character summary.
        """
        self.image.hide()
        self.character_name.hide()
        self.character_level.hide()
        self.character_job.hide()
        self.character_job_level.hide()

    def show(self):
        """
        Show all elements of the character summary.
        """
        self.image.show()
        self.character_name.show()
        self.character_level.show()
        self.character_job.show()
        self.character_job_level.show()
