import os
import sys

import pygame

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)  # noqa: E402

from ui.components.ui_manager import UIManager  # noqa: E402
from ui.screens.main_menu_screen import MainMenuScreen  # noqa: E402
from ui.screens.start_screen import StartScreen  # noqa: E402


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

    def play_game():
        print("Play button clicked!")

    def view_party():
        print("View Party button clicked!")

    def settings():
        print("Settings button clicked!")

    def quit_game():
        nonlocal running
        running = False

    main_menu_screen_callbacks = {
        "play": play_game,
        "view_party": view_party,
        "settings": settings,
        "quit": quit_game,
    }

    main_menu_screen = MainMenuScreen(
        ui_manager, width, height, main_menu_screen_callbacks
    )

    def start_game():
        ui_manager.set_active_screen(main_menu_screen)

    start_screen = StartScreen(ui_manager, width, height, start_game)
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
