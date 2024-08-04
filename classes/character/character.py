from classes.character.stats import Stats
from classes.job.job import Job


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

    def __init__(
        self,
        name,
        current_job,
        image_path,
        stats: Stats,
        unlocked_jobs=None,
        xp=0,
        level=1,
    ):
        """
        Initialize a new character.

        Parameters:
        name (str): The name of the character.
        current_job (Job): The current job of the character.
        image_path (str): The path to the character's image.
        unlocked_jobs (list): A list of jobs unlocked by the character. Defaults to None.
        xp (int): The experience points of the character. Defaults to 0.
        level (int): The level of the character. Defaults to 1.
        """
        self.name = name
        self.current_job = current_job
        if unlocked_jobs is None:
            self.unlocked_jobs = [current_job]
        else:
            self.unlocked_jobs = unlocked_jobs
        self.stats = stats
        self.xp = xp
        self.level = level
        self.image_path = image_path

    def get_name(self):
        """
        Get the name of the character.

        Returns:
        str: The name of the character.
        """
        return self.name

    def get_xp(self):
        """
        Get the experience points of the character.

        Returns:
        int: The experience points of the character.
        """
        return self.xp

    def get_job(self):
        """
        Get the current job of the character.

        Returns:
        Job: The current job of the character.
        """
        return self.current_job

    def get_level(self):
        """
        Get the level of the character.

        Returns:
        int: The level of the character.
        """
        return self.level

    def get_image_path(self):
        """
        Get the path to the character's image.

        Returns:
        str: The path to the character's image.
        """
        return self.image_path

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

    def to_dict(self):
        """
        Return a dictionary representation of the character.

        Returns:
        dict: A dictionary representation of the character.
        """
        return {
            "name": self.name,
            "current_job": self.current_job.to_dict(),
            "unlocked_jobs": [job.to_dict() for job in self.unlocked_jobs],
            "stats": self.stats.to_dict(),
            "xp": self.xp,
            "level": self.level,
            "image_path": self.image_path,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a character from a dictionary.

        Parameters:
        data (dict): A dictionary containing character data.

        Returns:
        Character: A new character created from the dictionary.
        """
        name = data["name"]
        current_job = Job.from_dict(data["current_job"])
        unlocked_jobs = [Job.from_dict(job) for job in data["unlocked_jobs"]]
        stats = Stats.from_dict(data["stats"])
        xp = data["xp"]
        level = data["level"]
        image_path = data["image_path"]
        return cls(name, current_job, image_path, stats, unlocked_jobs, xp, level)
