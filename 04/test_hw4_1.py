"""Тестирование метакласса CustomMeta"""
import unittest
from hw4_1 import CustomMeta


class CustomClass(metaclass=CustomMeta):
    """Класс для тестирования"""
    x = 50

    def __init__(self, val=99):
        """Инициализация"""
        self.val = val

    def line(self):
        """Метод, возвращающий 100"""
        return 100

    def __str__(self):
        """Строковое представление"""
        return "Custom_by_metaclass"


class TestCustomMeta(unittest.TestCase):
    """Класс тестирования работы метакласса"""
    def test_true(self):
        """Тестирование класса"""
        inst = CustomClass()
        self.assertTrue(inst.custom_x == 50)
        self.assertFalse(inst.custom_x == 30)
        self.assertTrue(inst.custom_val == 99)
        self.assertFalse(inst.custom_val == 100)
        self.assertTrue(inst.custom_line() == 100)
        self.assertFalse(inst.custom_line() == 5)
        self.assertTrue(str(inst) == "Custom_by_metaclass")
        self.assertFalse(str(inst) == "Custom")

    def test_dynamic(self):
        """Тестирование свойства dynamic"""
        CustomClass.dynamic = "added later"
        self.assertTrue(CustomClass.custom_dynamic == "added later")


if __name__ == '__main__':
    unittest.main()
