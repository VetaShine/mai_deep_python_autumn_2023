"""Память, профилирование"""
import time
from random import choice
import weakref
import cProfile
import pstats
import io


class Student:
    """Класс с обычными атрибутами"""
    def __init__(self, student_name=None, gpa=None, faculty=None, course=None):
        self.name = Name(self, student_name)
        self.assessment = Assessment(self, gpa)
        self.studies = Information(self, faculty, course)


class Name:
    """Имя студента"""
    def __init__(self, student, student_name):
        self.student = student
        self.student_name = student_name


class Assessment:
    """Средний балл студента"""
    def __init__(self, student, gpa):
        self.student = student
        self.gpa = gpa


class Information:
    """Информация о факультете и курсе"""
    def __init__(self, student, faculty, course):
        self.student = student
        self.faculty = faculty
        self.course = course


class StudentSlots:
    """Класс со слотами"""
    __slots__ = ("name", "assessment", "studies")

    def __init__(self, student_name=None, gpa=None, faculty=None, course=None):
        self.name = Name(self, student_name)
        self.assessment = Assessment(self, gpa)
        self.studies = Information(self, faculty, course)


class NameSlots:
    """Имя студента"""
    __slots__ = ("student", "student_name")

    def __init__(self, student, student_name):
        self.student = student
        self.student_name = student_name


class AssessmentSlots:
    """Средний балл студента"""
    __slots__ = ("student", "gpa")

    def __init__(self, student, gpa):
        self.student = student
        self.gpa = gpa


class InformationSlots:
    """Информация о факультете и курсе"""
    __slots__ = ("student", "course", "faculty")

    def __init__(self, student, course, faculty):
        self.student = student
        self.faculty = faculty
        self.course = course


class StudentWeakref:
    """Класс с атрибутами weakref"""
    def __init__(self, student_name=None, gpa=None, faculty=None, course=None):
        self.name = Name(self, student_name)
        self.assessment = Assessment(self, gpa)
        self.studies = Information(self, faculty, course)


class NameWeakref:
    """Имя студента"""
    def __init__(self, student, student_name):
        self.student = weakref.ref(student)
        self.student_name = student_name


class AssessmentWeakref:
    """Средний балл студента"""
    def __init__(self, student, gpa):
        self.student = weakref.ref(student)
        self.gpa = gpa


class InformationWeakref:
    """Информация о факультете и курсе"""
    def __init__(self, student, faculty, course):
        self.student = weakref.ref(student)
        self.faculty = faculty
        self.course = course


NAMES = ["Минеева", "Журавлев", "Катин", "Русаков", "Куликова",
         "Меркулов", "Шукайло", "Куликова", "Арбузов", "Павлов"]
ASSESSMENTS = ["5.0", "4.6", "4.7", "3.4", "4.0", "3.6", "3.7",
               "4.4", "3.0", "4.1", "4.9", "3.1"]
STUDIES = ["Прикладная математика", "Прикладная математика и информатика",
           "Графический дизайн", "Экономика", "Юриспруденция",
           "Дирижирование", "История", "Культурология"]


def random_word(words):
    """Возврат случайного слова"""
    return choice(words)


A = 1_000_000

names = [random_word(NAMES) for i in range(A)]
assessments = [random_word(ASSESSMENTS) for i in range(A)]
studies = [random_word(STUDIES) for i in range(A)]


def simple_class(n):
    """Создание списка объектов"""
    university_students = [Student(names[i], assessments[i], studies[i])
                           for i in range(n)]
    return university_students


def slots_class(n):
    """Создание списка объектов"""
    university_students_slots = [StudentSlots(names[i],
                                 assessments[i], studies[i]) for i in range(n)]
    return university_students_slots


def weakref_class(n):
    """Создание списка объектов"""
    university_students_weakref = [StudentWeakref(names[i],
                                   assessments[i], studies[i])
                                   for i in range(n)]
    return university_students_weakref


start_cpu_time = time.process_time()
start_wall_time = time.time()

students = simple_class(A)

end_cpu_time = time.process_time()
end_wall_time = time.time()

print('Time of simple_class:')
cpu_time = end_cpu_time - start_cpu_time
print('CPU time:', cpu_time, 's')

wall_time = end_wall_time - start_wall_time
print('Wall time:', wall_time, 's')


start_cpu_time = time.process_time()
start_wall_time = time.time()

students_slots = slots_class(A)

end_cpu_time = time.process_time()
end_wall_time = time.time()

print('Time of slots_class:')
cpu_time = end_cpu_time - start_cpu_time
print('CPU time:', cpu_time, 's')

wall_time = end_wall_time - start_wall_time
print('Wall time:', wall_time, 's')


start_cpu_time = time.process_time()
start_wall_time = time.time()

students_weakref = weakref_class(A)

end_cpu_time = time.process_time()
end_wall_time = time.time()

print('Time of weakref_class:')
cpu_time = end_cpu_time - start_cpu_time
print('CPU time:', cpu_time, 's')

wall_time = end_wall_time - start_wall_time
print('Wall time:', wall_time, 's')


def simple_class_get(n):
    """Получение среднего балла для каждого студента"""
    for i in range(n):
        _ = students[i].assessment.gpa


def slots_class_get(n):
    """Получение среднего балла для каждого студента"""
    for i in range(n):
        _ = students_slots[i].assessment.gpa


def weakref_class_get(n):
    """Получение среднего балла для каждого студента"""
    for i in range(n):
        _ = students_weakref[i].assessment.gpa


def simple_class_change(n):
    """Изменение среднего балла для каждого студента"""
    for i in range(n):
        students[i].assessment.gpa += " for 2022"


def slots_class_change(n):
    """Изменение среднего балла для каждого студента"""
    for i in range(n):
        students_slots[i].assessment.gpa += " for 2022"


def weakref_class_change(n):
    """Изменение среднего балла для каждого студента"""
    for i in range(n):
        students_weakref[i].assessment.gpa += " for 2022"


def simple_class_del(n):
    """Удаление факультета для каждого студента"""
    for i in range(n):
        del students[i].studies.faculty


def slots_class_del(n):
    """Удаление факультета для каждого студента"""
    for i in range(n):
        del students_slots[i].studies.faculty


def weakref_class_del(n):
    """Удаление факультета для каждого студента"""
    for i in range(n):
        del students_weakref[i].studies.faculty


start_cpu_time = time.process_time()
start_wall_time = time.time()

simple_class_get(A)

end_cpu_time = time.process_time()
end_wall_time = time.time()

print('Time of simple_class_get:')
cpu_time = end_cpu_time - start_cpu_time
print('CPU time:', cpu_time, 's')

wall_time = end_wall_time - start_wall_time
print('Wall time:', wall_time, 's')


start_cpu_time = time.process_time()
start_wall_time = time.time()

slots_class_get(A)

end_cpu_time = time.process_time()
end_wall_time = time.time()

print('Time of slots_class_get:')
cpu_time = end_cpu_time - start_cpu_time
print('CPU time:', cpu_time, 's')

wall_time = end_wall_time - start_wall_time
print('Wall time:', wall_time, 's')


start_cpu_time = time.process_time()
start_wall_time = time.time()

weakref_class_get(A)

end_cpu_time = time.process_time()
end_wall_time = time.time()

print('Time of weakref_class_get:')
cpu_time = end_cpu_time - start_cpu_time
print('CPU time:', cpu_time, 's')

wall_time = end_wall_time - start_wall_time
print('Wall time:', wall_time, 's')


start_cpu_time = time.process_time()
start_wall_time = time.time()

simple_class_change(A)

end_cpu_time = time.process_time()
end_wall_time = time.time()

print('Time of simple_class_change:')
cpu_time = end_cpu_time - start_cpu_time
print('CPU time:', cpu_time, 's')

wall_time = end_wall_time - start_wall_time
print('Wall time:', wall_time, 's')


start_cpu_time = time.process_time()
start_wall_time = time.time()

slots_class_change(A)

end_cpu_time = time.process_time()
end_wall_time = time.time()

print('Time of slots_class_change:')
cpu_time = end_cpu_time - start_cpu_time
print('CPU time:', cpu_time, 's')

wall_time = end_wall_time - start_wall_time
print('Wall time:', wall_time, 's')


start_cpu_time = time.process_time()
start_wall_time = time.time()

weakref_class_change(A)

end_cpu_time = time.process_time()
end_wall_time = time.time()

print('Time of weakref_class_change:')
cpu_time = end_cpu_time - start_cpu_time
print('CPU time:', cpu_time, 's')

wall_time = end_wall_time - start_wall_time
print('Wall time:', wall_time, 's')


start_cpu_time = time.process_time()
start_wall_time = time.time()

simple_class_del(A)

end_cpu_time = time.process_time()
end_wall_time = time.time()

print('Time of simple_class_del:')
cpu_time = end_cpu_time - start_cpu_time
print('CPU time:', cpu_time, 's')

wall_time = end_wall_time - start_wall_time
print('Wall time:', wall_time, 's')


start_cpu_time = time.process_time()
start_wall_time = time.time()

slots_class_del(A)

end_cpu_time = time.process_time()
end_wall_time = time.time()

print('Time of slots_class_del:')
cpu_time = end_cpu_time - start_cpu_time
print('CPU time:', cpu_time, 's')

wall_time = end_wall_time - start_wall_time
print('Wall time:', wall_time, 's')


start_cpu_time = time.process_time()
start_wall_time = time.time()

weakref_class_del(A)

end_cpu_time = time.process_time()
end_wall_time = time.time()

print('Time of weakref_class_del:')
cpu_time = end_cpu_time - start_cpu_time
print('CPU time:', cpu_time, 's')

wall_time = end_wall_time - start_wall_time
print('Wall time:', wall_time, 's')


def profile_deco(func):
    """Декоратор для профилирования"""
    prof = cProfile.Profile()
    stats = io.StringIO()
    counter = 0

    def wrapper(*args, **kwargs):
        """Функция-обёртка"""
        nonlocal counter, stats, prof
        counter += 1
        print(f"Число вызовов функции {func.__name__} =", counter)
        prof.enable()
        result = func(*args, **kwargs)
        prof.disable()
        return result

    def print_statisctic():
        """Отображение статистики профилирования"""
        sortby = 'cumulative'
        ps = pstats.Stats(prof, stream=stats).sort_stats(sortby)
        ps.print_stats()
        print(stats.getvalue())

    wrapper.print_stat = print_statisctic
    return wrapper


@profile_deco
def simple(n):
    """Создание списка студентов"""
    _ = [Student(names[i], assessments[i], studies[i]) for i in range(n)]


@profile_deco
def slots(n):
    """Создание списка студентов"""
    _ = [Student(names[i], assessments[i], studies[i]) for i in range(n)]


@profile_deco
def weakrefs(n):
    """Создание списка студентов"""
    _ = [Student(names[i], assessments[i], studies[i]) for i in range(n)]


simple(A)
simple.print_stat()


slots(A)
slots.print_stat()


weakrefs(A)
weakrefs.print_stat()


@profile_deco
def simple_get(n):
    """Получение среднего балла для каждого студента"""
    for i in range(n):
        _ = students[i].assessment.gpa


@profile_deco
def slots_get(n):
    """Получение среднего балла для каждого студента"""
    for i in range(n):
        _ = students_slots[i].assessment.gpa


@profile_deco
def weakref_get(n):
    """Получение среднего балла для каждого студента"""
    for i in range(n):
        _ = students_weakref[i].assessment.gpa


for _ in range(100):
    simple_get(A)
simple_get.print_stat()


for _ in range(100):
    slots_get(A)
slots_get.print_stat()


for _ in range(100):
    weakref_get(A)
weakref_get.print_stat()


@profile_deco
def simple_change(n):
    """Изменение среднего балла для каждого студента"""
    for i in range(n):
        students[i].assessment.gpa += " for 2022"


@profile_deco
def slots_change(n):
    """Изменение среднего балла для каждого студента"""
    for i in range(n):
        students_slots[i].assessment.gpa += " for 2022"


@profile_deco
def weakref_change(n):
    """Изменение среднего балла для каждого студента"""
    for i in range(n):
        students_weakref[i].assessment.gpa += " for 2022"


for _ in range(10):
    simple_change(A)
simple_change.print_stat()


for _ in range(10):
    slots_change(A)
slots_change.print_stat()


for _ in range(10):
    weakref_change(A)
weakref_change.print_stat()


@profile_deco
def simple_del(n):
    """Удаление факультета для каждого студента"""
    for i in range(n):
        del students[i].assessment.gpa


@profile_deco
def slots_del(n):
    """Удаление факультета для каждого студента"""
    for i in range(n):
        del students_slots[i].assessment.gpa


@profile_deco
def weakref_del(n):
    """Удаление факультета для каждого студента"""
    for i in range(n):
        del students_weakref[i].assessment.gpa


simple_del(A)
simple_del.print_stat()

slots_del(A)
slots_del.print_stat()

weakref_del(A)
weakref_del.print_stat()
