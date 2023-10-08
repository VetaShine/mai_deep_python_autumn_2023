"""Тестирование декоратора с помощью mock-объекта"""
import unittest
from unittest.mock import patch
from decorator import call

class TestCallFunction(unittest.TestCase):
    """Класс для тестирования"""
    @patch('builtins.print')
    def test_call_calls(self, mock):
        """Метод вызова функции и проверки введенных значений"""
        for _ in range(10):
            call()

        self.assertEqual(mock.call_count, 10)

if __name__ == '__main__':
    unittest.main()
