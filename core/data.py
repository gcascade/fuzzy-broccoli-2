from classes.character.character import Character
from classes.character.stats import Stats
from classes.job.novice import Novice
from classes.job.student import Student
from core.config import Config

initial_stats = Stats(
    hp=100,
    mp=50,
    strength=10,
    intelligence=10,
    dexterity=10,
    physical_defense=5,
    magical_resistance=5,
    accuracy=0,
    evasion=0,
    luck=5,
    wisdom=10,
    bravery=10,
    faith=10,
    charisma=10,
)


def get_initial_characters():
    return [
        Character(
            name="Elaine",
            level=1,
            current_job=Novice(),
            stats=initial_stats,
            xp=0,
            image_path=f"{Config.IMAGE_PATH}/characters/female_adventurer_1.png",
            unlocked_jobs=[Novice(), Student()],
        ),
        Character(
            name="Arianne",
            level=1,
            current_job=Student(),
            stats=initial_stats,
            xp=0,
            image_path=f"{Config.IMAGE_PATH}/characters/female_adventurer_2.png",
            unlocked_jobs=[Novice(), Student()],
        ),
        Character(
            name="Magnus",
            level=1,
            current_job=Novice(),
            stats=initial_stats,
            xp=0,
            image_path=f"{Config.IMAGE_PATH}/characters/male_adventurer_1.png",
            unlocked_jobs=[Novice(), Student()],
        ),
        Character(
            name="Roland",
            level=1,
            current_job=Student(),
            stats=initial_stats,
            xp=0,
            image_path=f"{Config.IMAGE_PATH}/characters/male_adventurer_2.png",
            unlocked_jobs=[Novice(), Student()],
        ),
    ]
