class Character:
    """
    A class to represent a character in the game.
    """

    def __init__(self, name, xp=0, level=1):
        """
        Initialize a new character.

        :param name: The name of the character.
        :param xp: The experience points of the character, defaults to 0.
        :param level: The level of the character, defaults to 1.
        """
        self.name = name
        self.xp = xp
        self.level = level

    def add_xp(self, amount):
        """
        Add experience points to the character.

        :param amount: The amount of experience points to add.
        """
        self.xp += amount

    def reset_xp(self):
        """
        Reset the character's experience points to 0.
        """
        self.xp = 0

    def level_up(self):
        """
        Level up the character.
        """
        self.level += 1

    def reset_level(self):
        """
        Reset the character's level to 1.
        """
        self.level = 1

    def __str__(self):
        """
        Return a string representation of the character.
        """
        return f"Character(name={self.name}, xp={self.xp})"
