from unittest import TestCase
from hw4_1 import CustomMeta

class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"

class TestCustomMeta(TestCase):
    def TestTrue(self):
        self.assertTrue(CustomClass.custom_x == 50)
        self.assertTrue(CustomClass.custom_val == 99)
        self.assertTrue(CustomClass.custom_line() == 100)
        self.assertTrue(str(CustomClass) == "Custom_by_metaclass")