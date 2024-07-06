from classes.job.novice import Novice


def test_novice_initialization():
    novice = Novice()
    assert novice.name == "Novice"
    assert novice.xp == 0
    assert novice.level == 1


def test_add_xp():
    novice = Novice()
    novice.add_xp(50)
    assert novice.xp == 50
    novice.add_xp(60)
    assert novice.xp == 110


def test_reset_xp():
    novice = Novice()
    novice.add_xp(100)
    novice.reset_xp()
    assert novice.xp == 0


def test_level_up():
    novice = Novice()
    novice.level_up()
    assert novice.level == 2
    novice.level_up()
    assert novice.level == 3


def test_reset_level():
    novice = Novice()
    novice.level_up()
    novice.level_up()
    novice.reset_level()
    assert novice.level == 1


def test_description():
    novice = Novice()
    assert novice.description() == "A beginner job for new adventurers."
