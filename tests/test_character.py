from classes.character.character import Character
from classes.job.novice import Novice
from classes.job.student import Student


def test_character_initialization():
    character = Character("Hero", Novice(), "path")
    assert character.get_name() == "Hero"
    assert character.get_xp() == 0
    assert character.get_image_path() == "path"
    assert character.get_level() == 1


def test_add_xp():
    character = Character("Hero", Novice(), "path")
    character.add_xp(50)
    assert character.get_xp() == 50
    character.add_xp(25)
    assert character.get_xp() == 75


def test_reset_xp():
    character = Character("Hero", Novice(), "path", xp=100)
    character.reset_xp()
    assert character.get_xp() == 0


def test_level_up():
    character = Character("Hero", Novice(), "path")
    character.level_up()
    assert character.get_level() == 2
    character.level_up()
    assert character.get_level() == 3


def test_reset_level():
    character = Character("Hero", Novice(), "path", level=5)
    character.reset_level()
    assert character.get_level() == 1


def test_character_str():
    character = Character("Hero", Novice(), "path", xp=100)
    assert str(character) == "Character(name=Hero, xp=100)"


def test_change_job():
    character = Character("Hero", Novice(), "path")
    character.change_job(Student())
    assert character.current_job.get_name() == "Student"
