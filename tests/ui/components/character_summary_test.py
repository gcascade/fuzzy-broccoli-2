from unittest.mock import MagicMock, patch

import pygame
import pytest

from classes.character.character import Character
from ui.components.character_summary import CharacterSummary
from ui.components.ui_manager import UIManager


@pytest.fixture
def setup_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    manager = UIManager(800, 600)
    surface = pygame.Surface((800, 600))
    yield screen, manager, surface
    pygame.quit()


@pytest.fixture
def character():
    character = MagicMock(spec=Character)
    character.get_name.return_value = "Test Character"
    character.get_level.return_value = 10
    character.get_job.return_value.get_name.return_value = "Warrior"
    character.get_job.return_value.get_level.return_value = 5
    character.get_image_path.return_value = "assets/images/test_image.png"
    return character


def empty_character_function(character: Character):
    pass


def empty_function():
    pass


def test_character_summary_initialization(setup_pygame, character):
    screen, manager, surface = setup_pygame
    position = (100, 100)
    size = (200, 200)

    with patch("pygame.image.load") as mock_load:
        mock_load.return_value = surface

        summary = CharacterSummary(
            character,
            manager,
            position,
            size,
            empty_character_function,
            empty_character_function,
            empty_function,
        )

        assert summary.character == character
        assert summary.image.get_instance().relative_rect.topleft == position
        assert summary.image.get_instance().relative_rect.size == size
        assert summary.character_name.get_instance().text == "Test Character"
        assert summary.character_level.get_instance().text == "Level: 10"
        assert summary.character_job.get_instance().text == "Job: Warrior"
        assert summary.character_job_level.get_instance().text == "Job Level: 5"


def test_character_summary_show(setup_pygame, character):
    screen, manager, surface = setup_pygame
    position = (100, 100)
    size = (200, 200)

    with patch("pygame.image.load") as mock_load:
        mock_load.return_value = surface

        summary = CharacterSummary(
            character,
            manager,
            position,
            size,
            empty_character_function,
            empty_character_function,
            empty_function,
        )
        summary.show()

        assert summary.image.get_instance().visible == 1
        assert summary.character_name.get_instance().visible == 1
        assert summary.character_level.get_instance().visible == 1
        assert summary.character_job.get_instance().visible == 1
        assert summary.character_job_level.get_instance().visible == 1


def test_character_summary_hide(setup_pygame, character):
    screen, manager, surface = setup_pygame
    position = (100, 100)
    size = (200, 200)

    with patch("pygame.image.load") as mock_load:
        mock_load.return_value = surface

        summary = CharacterSummary(
            character,
            manager,
            position,
            size,
            empty_character_function,
            empty_character_function,
            empty_function,
        )
        summary.hide()

        assert summary.image.get_instance().visible == 0
        assert summary.character_name.get_instance().visible == 0
        assert summary.character_level.get_instance().visible == 0
        assert summary.character_job.get_instance().visible == 0
        assert summary.character_job_level.get_instance().visible == 0
