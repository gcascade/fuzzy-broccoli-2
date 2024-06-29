import pygame
import pygame_gui


def create_ui_manager(screen_width, screen_height):
    """
    Create and return a UI manager.

    :param screen_width: The width of the screen.
    :param screen_height: The height of the screen.
    :return: The UI manager.
    """
    return pygame_gui.UIManager((screen_width, screen_height))


def create_start_screen(manager):
    """
    Create the start screen elements.

    :param manager: The UI manager.
    :return: A tuple containing the title label and start button.
    """
    title_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((250, 100), (300, 50)),
        text="Fuzzy Broccoli 2",
        manager=manager,
    )

    start_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((350, 275), (100, 50)),
        text="Start Game",
        manager=manager,
    )

    return title_label, start_button


def create_main_menu(manager):
    """
    Create the main menu elements.

    :param manager: The UI manager.
    :return: A dictionary of the menu buttons.
    """
    menu_buttons = {
        "play": pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((350, 200), (100, 50)),
            text="Play",
            manager=manager,
            visible=0,
        ),
        "view_party": pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((350, 275), (100, 50)),
            text="View Party",
            manager=manager,
            visible=0,
        ),
        "settings": pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((350, 350), (100, 50)),
            text="Settings",
            manager=manager,
            visible=0,
        ),
        "quit": pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((350, 425), (100, 50)),
            text="Quit",
            manager=manager,
            visible=0,
        ),
    }
    return menu_buttons
