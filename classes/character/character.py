class Character:
    """
    A class to represent a character in the game.

    Attributes:
    name (str): The name of the character.
    current_job (Job): The current job of the character.
    unlocked_jobs (list): A list of jobs unlocked by the character.
    xp (int): The experience points of the character. Defaults to 0.
    level (int): The level of the character. Defaults to 1.
    """

    def __init__(self, name, current_job, unlocked_jobs=[], xp=0, level=1):
        """
        Initialize a new character.

        Parameters:
        name (str): The name of the character.
        current_job (Job): The current job of the character.
        unlocked_jobs (list): A list of jobs unlocked by the character. Defaults to an empty list.
        xp (int): The experience points of the character. Defaults to 0.
        level (int): The level of the character. Defaults to 1.
        """
        self.name = name
        self.current_job = current_job
        self.unlocked_jobs = unlocked_jobs
        self.xp = xp
        self.level = level

    def add_xp(self, amount):
        """
        Add experience points to the character.

        Parameters:
        amount (int): The amount of experience points to add.
        """
        self.xp += amount

    def reset_xp(self):
        """
        Reset the character's experience points to 0.
        """
        self.xp = 0

    def level_up(self):
        """
        Level up the character by increasing its level by 1.
        """
        self.level += 1

    def reset_level(self):
        """
        Reset the character's level to 1.
        """
        self.level = 1

    def change_job(self, new_job):
        """
        Change the character's job to a new job.

        Parameters:
        new_job (Job): The new job to change to.
        """
        self.current_job = new_job

    def __str__(self):
        """
        Return a string representation of the character.

        Returns:
        str: A string representation of the character.
        """
        return f"Character(name={self.name}, xp={self.xp})"
