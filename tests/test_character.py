from classes.character.character import Character


def test_character_initialization():
    character = Character("Hero")
    assert character.name == "Hero"
    assert character.xp == 0


def test_add_xp():
    character = Character("Hero")
    character.add_xp(50)
    assert character.xp == 50
    character.add_xp(25)
    assert character.xp == 75


def test_reset_xp():
    character = Character("Hero", xp=100)
    character.reset_xp()
    assert character.xp == 0


def test_level_up():
    character = Character("Hero")
    character.level_up()
    assert character.level == 2
    character.level_up()
    assert character.level == 3


def test_reset_level():
    character = Character("Hero", level=5)
    character.reset_level()
    assert character.level == 1


def test_character_str():
    character = Character("Hero", xp=100)
    assert str(character) == "Character(name=Hero, xp=100)"
