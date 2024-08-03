from abc import ABC, abstractmethod

from classes.job.job_registry import JobRegistry


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

    def get_name(self):
        """
        Get the name of the job.

        Returns:
        str: The name of the job.
        """
        return self.name

    def get_level(self):
        """
        Get the level of the job.

        Returns:
        int: The level of the job.
        """
        return self.level

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

    def to_dict(self):
        """
        Return the job as a dictionary.

        Returns:
        dict: The job as a dictionary.
        """
        return {"name": self.name, "xp": self.xp, "level": self.level}

    @classmethod
    def from_dict(cls, data):
        """
        Create a new Job from a dictionary.

        Parameters:
        data (dict): A dictionary containing the job data.

        Returns:
        Job: A new Job instance.
        """
        job_class = JobRegistry.get_job_class(data["name"])
        return job_class.from_dict(data)
