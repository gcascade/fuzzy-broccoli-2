from classes.job.student import Student


def test_student_initialization():
    student = Student()
    assert student.name == "Student"
    assert student.xp == 0
    assert student.level == 1


def test_add_xp():
    student = Student()
    student.add_xp(50)
    assert student.xp == 50
    student.add_xp(60)
    assert student.xp == 110


def test_reset_xp():
    student = Student()
    student.add_xp(100)
    student.reset_xp()
    assert student.xp == 0


def test_level_up():
    student = Student()
    student.level_up()
    assert student.level == 2
    student.level_up()
    assert student.level == 3


def test_reset_level():
    student = Student()
    student.level_up()
    student.level_up()
    student.reset_level()
    assert student.level == 1


def test_description():
    student = Student()
    assert student.description() == "An aspiring learner who seeks knowledge."
