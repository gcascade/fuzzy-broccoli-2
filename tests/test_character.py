from classes.character.character import Character
from classes.job.novice import Novice
from classes.job.student import Student


def test_character_initialization():
    character = Character("Hero", Novice())
    assert character.name == "Hero"
    assert character.xp == 0


def test_add_xp():
    character = Character("Hero", Novice())
    character.add_xp(50)
    assert character.xp == 50
    character.add_xp(25)
    assert character.xp == 75


def test_reset_xp():
    character = Character("Hero", Novice(), xp=100)
    character.reset_xp()
    assert character.xp == 0


def test_level_up():
    character = Character("Hero", Novice())
    character.level_up()
    assert character.level == 2
    character.level_up()
    assert character.level == 3


def test_reset_level():
    character = Character("Hero", Novice(), level=5)
    character.reset_level()
    assert character.level == 1


def test_character_str():
    character = Character("Hero", Novice(), xp=100)
    assert str(character) == "Character(name=Hero, xp=100)"


def test_change_job():
    character = Character("Hero", Novice())
    character.change_job(Student())
    assert character.current_job.name == "Student"
