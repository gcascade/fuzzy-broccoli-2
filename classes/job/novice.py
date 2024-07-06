from classes.job.job import Job


class Novice(Job):
    """
    A class to represent a Novice job.

    Attributes:
    name (str): The name of the job.
    xp (int): The experience points of the job. Defaults to 0.
    level (int): The level of the job. Defaults to 1.
    """

    def __init__(self):
        super().__init__("Novice")
        self.__doc__ = Job.__doc__ + "\n" + self.__doc__

    def description(self):
        return "A beginner job for new adventurers."
