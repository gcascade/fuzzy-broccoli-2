from abc import ABC, abstractmethod


class Job(ABC):
    """
    A class to represent a character's job or class in the game.

    Attributes:
    name (str): The name of the job.
    xp (int): The experience points of the job. Defaults to 0.
    level (int): The level of the job. Defaults to 1.
    """

    def __init__(self, name, xp=0, level=1):
        """
        Initialize a new Job.

        Parameters:
        name (str): The name of the job.
        xp (int): The experience points of the job. Defaults to 0.
        level (int): The level of the job. Defaults to 1.
        """
        self.name = name
        self.xp = xp
        self.level = level

    def add_xp(self, amount):
        """
        Add experience points to the job.

        Parameters:
        amount (int): The amount of experience points to add.
        """
        self.xp += amount

    def reset_xp(self):
        """
        Reset the job's experience points to 0.
        """
        self.xp = 0

    def level_up(self):
        """
        Level up the job by increasing its level by 1.
        """
        self.level += 1

    def reset_level(self):
        """
        Reset the job's level to 1.
        """
        self.level = 1

    @abstractmethod
    def description(self):
        """
        Return the description of the job.
        """
        pass
