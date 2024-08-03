from unittest.mock import patch

import pygame
import pytest

from ui.components.image import Image
from ui.components.ui_manager import UIManager


@pytest.fixture
def setup_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    manager = UIManager(800, 600)
    surface = pygame.Surface((800, 600))
    yield screen, manager, surface
    pygame.quit()


def test_image_initialization(setup_pygame):
    screen, manager, surface = setup_pygame
    image_path = "assets/images/sample_image.png"

    with patch("pygame.image.load") as mock_load:
        mock_load.return_value = surface

        image = Image(
            ui_manager=manager,
            image_path=image_path,
            position=(100, 100),
            size=(200, 200),
        )

        assert image.get_instance().relative_rect.topleft == (100, 100)
        assert image.get_instance().relative_rect.size == (200, 200)
        assert image.get_instance().image is not None
        assert image.get_instance().visible == 0


def test_image_show(setup_pygame):
    screen, manager, surface = setup_pygame
    image_path = "assets/images/sample_image.png"

    with patch("pygame.image.load") as mock_load:
        mock_load.return_value = surface

        image = Image(
            ui_manager=manager,
            image_path=image_path,
            position=(100, 100),
            size=(200, 200),
        )
        image.show()

        assert image.get_instance().visible == 1


def test_image_hide(setup_pygame):
    screen, manager, surface = setup_pygame
    image_path = "assets/images/sample_image.png"

    with patch("pygame.image.load") as mock_load:
        mock_load.return_value = surface

        image = Image(
            ui_manager=manager,
            image_path=image_path,
            position=(100, 100),
            size=(200, 200),
        )
        image.hide()

        assert image.get_instance().visible == 0
