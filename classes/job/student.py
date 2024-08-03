from classes.job.job import Job
from classes.job.job_registry import JobRegistry


class Student(Job):
    """
    A class to represent a Student job.

    Attributes:
    name (str): The name of the job.
    xp (int): The experience points of the job. Defaults to 0.
    level (int): The level of the job. Defaults to 1.
    """

    def __init__(self, xp=0, level=1):
        super().__init__(name="Student")
        self.__doc__ = Job.__doc__ + "\n" + self.__doc__

    def description(self):
        return "An aspiring learner who seeks knowledge."

    @classmethod
    def from_dict(cls, data):
        return cls(data["xp"], data["level"])


JobRegistry.register(Student)
