from unittest.mock import patch

import pygame
import pytest

from core.config import Config
from core.game_initializer import initialize_game


@pytest.fixture
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()


def test_initialize_game_screen(setup_pygame):
    with (
        patch("pygame.display.set_mode") as mock_set_mode,
        patch("pygame.display.set_caption") as mock_set_caption,
        patch("pygame.time.Clock") as mock_clock,
    ):
        mock_screen = mock_set_mode.return_value
        mock_clock_instance = mock_clock.return_value

        screen, clock = initialize_game()

        mock_set_mode.assert_called_once_with(
            (Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT)
        )
        mock_set_caption.assert_called_once_with("Fuzzy Broccoli 2")
        assert screen == mock_screen
        assert clock == mock_clock_instance


def test_initialize_game_calls_pygame_init(setup_pygame):
    with patch("pygame.init") as mock_pygame_init:
        initialize_game()
        mock_pygame_init.assert_called_once()
