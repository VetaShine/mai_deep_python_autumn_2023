"""Тестирование класса CustomList"""
import unittest
from hw3 import CustomList


class TestCustomList(unittest.TestCase):
    """Класс тестирования"""
    def test_add(self):
        """Тестирование сложения экземпляров, списков"""
        self.assertEqual(
            CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7]), [6, 3, 10, 7])
        self.assertEqual(CustomList([1]) + [2, 5], [3, 5])
        self.assertEqual([2, 5] + CustomList([1]), [3, 5])

    def test_sub(self):
        """Тестирование вычитания экземпляров, списков"""
        self.assertEqual(
            CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7]), [4, -1, -4, 7])
        self.assertEqual(CustomList([1]) - [2, 5], [-1, -5])
        self.assertEqual([2, 5] - CustomList([1]), [1, 5])

    def test_eq(self):
        """Тестирование равенства экземпляров"""
        self.assertEqual(
            CustomList([5, 1, 3, 7]) == CustomList([1, 2, 7]), False)
        self.assertEqual((CustomList([1]) + [2, 5]) == [3, 5], True)
        self.assertEqual(CustomList([1]) == CustomList([1]), True)

    def test_ne(self):
        """Тестирование неравенства экземпляров"""
        self.assertEqual(
            CustomList([5, 1, 3, 7]) != CustomList([1, 2, 7]), True)
        self.assertEqual((CustomList([1]) + [2, 5]) != [3, 5], False)
        self.assertEqual(CustomList([1]) != CustomList([1]), False)

    def test_gt(self):
        """Тестирование сравнения "больше" экземпляров"""
        self.assertEqual(
            CustomList([5, 1, 3, 7]) > CustomList([1, 2, 7]), True)
        self.assertEqual((CustomList([1]) + [2, 5]) > [3, 5], False)
        self.assertEqual(CustomList([1, 2]) > CustomList([1]), True)

    def test_ge(self):
        """Тестирование сравнения "больше или равно" экземпляров"""
        self.assertEqual(
            CustomList([5, 1, 3, 7]) >= CustomList([1, 2, 7]), True)
        self.assertEqual((CustomList([1]) + [2, 5]) >= [3, 5], True)
        self.assertEqual(CustomList([0]) >= CustomList([1]), False)

    def test_lt(self):
        """Тестирование сравнения "меньше" экземпляров"""
        self.assertEqual(
            CustomList([5, 1, 3, 7]) < CustomList([1, 2, 7]), False)
        self.assertEqual((CustomList([1]) + [2, 5]) < [3, 5], False)
        self.assertEqual(CustomList([0]) < CustomList([1]), True)

    def test_le(self):
        """Тестирование сравнения "меньше или равно" экземпляров"""
        self.assertEqual(
            CustomList([5, 1, 3, 7]) <= CustomList([1, 2, 7]), False)
        self.assertEqual((CustomList([1]) + [2, 5]) <= [3, 5], True)
        self.assertEqual(CustomList([0]) <= CustomList([1]), True)


if __name__ == '__main__':
    unittest.main()
