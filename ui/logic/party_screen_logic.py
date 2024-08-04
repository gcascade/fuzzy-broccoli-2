from classes.character.character import Character
from ui.components.message_box import MessageBox
from ui.components.ui_manager import UIManager
from ui.screens.main_menu_screen import MainMenuScreen


def go_back(ui_manager: UIManager, main_menu_screen: MainMenuScreen):
    """
    Go back to the main menu by setting the active screen to the main menu screen.

    :param ui_manager: The UIManager instance.
    :param main_menu_screen: The MainMenuScreen instance.
    """
    ui_manager.set_active_screen(main_menu_screen)


def on_character_hover(message_box: MessageBox, character: Character):
    """
    Show the character summary when the character is hovered over.

    :param message_box: The MessageBox instance.
    :param character: The Character instance.
    """
    message_box.set_message(
        f"Open {character.get_name()} summary.\nNot implemented yet."
    )


def on_character_click(ui_manager: UIManager, character: Character):
    """
    Not implemented yet.

    :param ui_manager: The UIManager instance.
    :param character: The Character instance.
    """
    print(f"Character {character.get_name()} clicked!")
