from classes.job.job import Job
from classes.job.job_registry import JobRegistry


class Novice(Job):
    """
    A class to represent a Novice job.

    Attributes:
    name (str): The name of the job.
    xp (int): The experience points of the job. Defaults to 0.
    level (int): The level of the job. Defaults to 1.
    """

    def __init__(self, xp=0, level=1):
        super().__init__(name="Novice")
        self.__doc__ = Job.__doc__ + "\n" + self.__doc__

    def description(self):
        return "A beginner job for new adventurers."

    @classmethod
    def from_dict(cls, data):
        return cls(data["xp"], data["level"])


JobRegistry.register(Novice)
