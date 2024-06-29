import sys

import pygame
import pygame_gui

from scripts.ui import create_main_menu, create_start_screen, create_ui_manager


def game_loop(screen, clock):
    """
    The main game loop.

    :param screen: The Pygame display surface.
    :param clock: The Pygame clock.
    """
    # Create a UI manager
    manager = create_ui_manager(screen.get_width(), screen.get_height())

    # Create the start screen elements
    title_label, start_button = create_start_screen(manager)
    menu_buttons = create_main_menu(manager)

    running = True
    game_started = False
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    game_started = True
                    title_label.hide()
                    start_button.hide()
                    for button in menu_buttons.values():
                        button.show()
                elif game_started:
                    if event.ui_element == menu_buttons["play"]:
                        print("Play button clicked!")
                    elif event.ui_element == menu_buttons["view_party"]:
                        print("View Party button clicked!")
                    elif event.ui_element == menu_buttons["settings"]:
                        print("Settings button clicked!")
                    elif event.ui_element == menu_buttons["quit"]:
                        running = False

            manager.process_events(event)

        manager.update(time_delta)

        screen.fill((0, 0, 0))
        manager.draw_ui(screen)
        pygame.display.update()

    pygame.quit()
    sys.exit()
