import pytest

# Import these from your actual Python file.
# Example:
# from classroom import Classroom, Person, Teacher, Student, TooManyStudents

from source.school import Classroom, Person, Teacher, Student, TooManyStudents


# ============================================================
# HOGWARTS FIXTURES
# ============================================================

@pytest.fixture
def harry():
    return Student("Harry Potter")


@pytest.fixture
def hermione():
    return Student("Hermione Granger")


@pytest.fixture
def ron():
    return Student("Ron Weasley")


@pytest.fixture
def snape():
    return Teacher("Severus Snape")


@pytest.fixture
def dumbledore():
    return Teacher("Albus Dumbledore")


@pytest.fixture
def hogwarts_students():
    return [
        Student("Harry Potter"),
        Student("Hermione Granger"),
        Student("Ron Weasley"),
    ]


@pytest.fixture
def potions_class(snape, hogwarts_students):
    return Classroom(
        teacher=snape,
        students=hogwarts_students,
        course_title="Potions"
    )


@pytest.fixture
def empty_classroom(dumbledore):
    return Classroom(
        teacher=dumbledore,
        students=[],
        course_title="Defense Against the Dark Arts"
    )


# ============================================================
# PERSON TESTS
# ============================================================

@pytest.mark.hogwarts
def test_student_is_created_correctly(harry):
    assert harry.name == "Harry Potter"


@pytest.mark.hogwarts
def test_teacher_is_created_correctly(snape):
    assert snape.name == "Severus Snape"


# ============================================================
# ADD STUDENT TESTS
# ============================================================

@pytest.mark.students
def test_add_student(empty_classroom, harry):
    empty_classroom.add_student(harry)

    assert len(empty_classroom.students) == 1
    assert empty_classroom.students[0].name == "Harry Potter"


@pytest.mark.students
@pytest.mark.parametrize(
    "student_name",
    [
        "Harry Potter",
        "Hermione Granger",
        "Ron Weasley",
        "Draco Malfoy",
        "Luna Lovegood",
        "Neville Longbottom",
    ]
)
def test_different_students_can_be_added(empty_classroom, student_name):
    student = Student(student_name)

    empty_classroom.add_student(student)

    assert student in empty_classroom.students


@pytest.mark.students
def test_ten_students_can_join_class(dumbledore):
    students = [
        Student(f"Hogwarts Student {number}")
        for number in range(10)
    ]

    classroom = Classroom(
        teacher=dumbledore,
        students=students,
        course_title="Transfiguration"
    )

    assert len(classroom.students) == 10


# ============================================================
# TOO MANY STUDENTS
# ============================================================

@pytest.mark.students
def test_too_many_students_raises_exception(dumbledore):
    students = [
        Student(f"Hogwarts Student {number}")
        for number in range(11)
    ]

    classroom = Classroom(
        teacher=dumbledore,
        students=students,
        course_title="Charms"
    )

    with pytest.raises(TooManyStudents):
        classroom.add_student(Student("Extra Student"))


# ============================================================
# KNOWN BUG TEST
# ============================================================

@pytest.mark.students
@pytest.mark.xfail(
    reason="Classroom.add_student() incorrectly allows the 11th student",
    strict=True
)
def test_eleven_students_should_not_be_allowed(dumbledore):
    students = [
        Student(f"Hogwarts Student {number}")
        for number in range(10)
    ]

    classroom = Classroom(
        teacher=dumbledore,
        students=students,
        course_title="Defense Against the Dark Arts"
    )

    # The 11th student should be rejected.
    with pytest.raises(TooManyStudents):
        classroom.add_student(Student("Draco Malfoy"))


# ============================================================
# REMOVE STUDENT TESTS
# ============================================================

@pytest.mark.students
def test_remove_student(potions_class):
    potions_class.remove_student("Harry Potter")

    assert len(potions_class.students) == 2
    assert all(
        student.name != "Harry Potter"
        for student in potions_class.students
    )


@pytest.mark.students
@pytest.mark.parametrize(
    "student_name",
    [
        "Harry Potter",
        "Hermione Granger",
        "Ron Weasley",
    ]
)
def test_remove_different_students(potions_class, student_name):
    potions_class.remove_student(student_name)

    assert all(
        student.name != student_name
        for student in potions_class.students
    )


@pytest.mark.students
def test_remove_nonexistent_student_does_nothing(potions_class):
    original_count = len(potions_class.students)

    potions_class.remove_student("Lord Voldemort")

    assert len(potions_class.students) == original_count


# ============================================================
# CHANGE TEACHER TESTS
# ============================================================

@pytest.mark.teachers
def test_change_teacher(potions_class, dumbledore):
    potions_class.change_teacher(dumbledore)

    assert potions_class.teacher.name == "Albus Dumbledore"


@pytest.mark.teachers
@pytest.mark.parametrize(
    "teacher_name",
    [
        "Albus Dumbledore",
        "Minerva McGonagall",
        "Severus Snape",
        "Remus Lupin",
    ]
)
def test_change_to_different_teachers(empty_classroom, teacher_name):
    teacher = Teacher(teacher_name)

    empty_classroom.change_teacher(teacher)

    assert empty_classroom.teacher.name == teacher_name


# ============================================================
# CLASSROOM INFORMATION
# ============================================================

@pytest.mark.hogwarts
def test_potions_class_information(potions_class):
    assert potions_class.course_title == "Potions"
    assert potions_class.teacher.name == "Severus Snape"
    assert len(potions_class.students) == 3