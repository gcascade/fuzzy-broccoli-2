import os
import sys

import pygame

from ui.logic.screen_factory import ScreenFactory
from ui.screen_type import ScreenType

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)  # noqa: E402

from ui.components.ui_manager import UIManager  # noqa: E402


def game_loop(screen, clock):
    """
    The main game loop.

    :param screen: The Pygame display surface.
    :param clock: The Pygame clock.
    """

    width = screen.get_width()
    height = screen.get_height()
    ui_manager = UIManager(width, height)

    running = True

    screen_factory = ScreenFactory(ui_manager)
    start_screen = screen_factory.create_screen(ScreenType.START)
    ui_manager.set_active_screen(start_screen)
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            ui_manager.process_event(event)

        ui_manager.update(time_delta)

        screen.fill((0, 0, 0))
        ui_manager.draw_ui(screen)
        pygame.display.update()

    pygame.quit()
    sys.exit()
