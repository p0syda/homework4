class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grades_sum = sum(sum(grades) for grades in self.grades.values())
        grades_count = sum(len(grades) for grades in self.grades.values())
        average_grade = grades_sum / grades_count if grades_count > 0 else 0
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {average_grade}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def average_grade(self):
        grades_sum = sum(sum(grades) for grades in self.grades.values())
        grades_count = sum(len(grades) for grades in self.grades.values())
        return grades_sum / grades_count if grades_count > 0 else 0

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        return False

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return False

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return total / count

    def __str__(self):
        average_grade = self.average_grade()
        return (f"{super().__str__()}\n"
                f"Средняя оценка за лекции: {average_grade}")

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()
        return False

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return False

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def average_grade_students(students, course):
    grades_sum = sum(sum(student.grades[course]) for student in students if course in student.grades)
    grades_count = sum(len(student.grades[course]) for student in students if course in student.grades)
    return grades_sum / grades_count if grades_count > 0 else 0

# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def average_grade_lecturers(lecturers, course):
    grades_sum = sum(sum(lecturer.grades[course]) for lecturer in lecturers if course in lecturer.grades)
    grades_count = sum(len(lecturer.grades[course]) for lecturer in lecturers