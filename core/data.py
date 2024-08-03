from classes.character.character import Character
from classes.job.novice import Novice
from classes.job.student import Student
from core.config import Config


def get_initial_characters():
    return [
        Character(
            name="Elaine",
            level=1,
            current_job=Novice(),
            xp=0,
            image_path=f"{Config.IMAGE_PATH}/characters/female_adventurer_1.png",
            unlocked_jobs=[Novice(), Student()],
        ),
        Character(
            name="Arianne",
            level=1,
            current_job=Student(),
            xp=0,
            image_path=f"{Config.IMAGE_PATH}/characters/female_adventurer_2.png",
            unlocked_jobs=[Novice(), Student()],
        ),
        Character(
            name="Magnus",
            level=1,
            current_job=Novice(),
            xp=0,
            image_path=f"{Config.IMAGE_PATH}/characters/male_adventurer_1.png",
            unlocked_jobs=[Novice(), Student()],
        ),
        Character(
            name="Roland",
            level=1,
            current_job=Student(),
            xp=0,
            image_path=f"{Config.IMAGE_PATH}/characters/male_adventurer_2.png",
            unlocked_jobs=[Novice(), Student()],
        ),
    ]
