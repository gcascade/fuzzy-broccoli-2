import sys

import pygame
import pygame_gui

from scripts.ui import create_start_screen, create_ui_manager


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

    running = True
    game_started = False
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    game_started = True

            manager.process_events(event)

        manager.update(time_delta)

        # Render to screen
        screen.fill((0, 0, 0))

        if game_started:
            # Main game screen
            font = pygame.font.Font(None, 74)
            text = font.render("Game Started!", True, (255, 255, 255))
            screen.blit(text, (250, 250))
        else:
            # Start screen
            manager.draw_ui(screen)

        pygame.display.update()

    pygame.quit()
    sys.exit()
