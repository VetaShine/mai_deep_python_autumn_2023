"""Тестирование хэш-таблицы"""
import unittest
from hw8 import HashTable


class HashTableTestCase(unittest.TestCase):
    """Класс тестирования хэш-таблицы"""
    def setUp(self):
        """Создание пустой хэш-таблицы"""
        self.table = HashTable()

    def test_put_and_get(self):
        """Проверка вставки элемента и получения его значения"""
        self.table.put("key1", "value1")
        self.assertEqual(self.table.get("key1"), "value1")

    def test_put_existing_key(self):
        """Проверка замены значения ключа"""
        self.table.put("key1", "value1")
        self.table.put("key1", "value2")
        self.assertEqual(self.table.get("key1"), "value2")

    def test_put_multiple_items(self):
        """Проверка вставки нескольких элементов и получения их значений"""
        self.table.put("key1", "value1")
        self.table.put("key2", "value2")
        self.table.put("key3", "value3")
        self.assertEqual(self.table.get("key1"), "value1")
        self.assertEqual(self.table.get("key2"), "value2")
        self.assertEqual(self.table.get("key3"), "value3")

    def test_get_non_existing_key(self):
        """Проверка получения значения по несуществующему ключу"""
        with self.assertRaises(KeyError):
            self.table.get("key1")

    def test_get_size(self):
        """Проверка размера хэш-таблицы"""
        self.assertEqual(len(self.table), 0)
        self.table.put("key1", "value1")
        self.assertEqual(len(self.table), 1)
        self.table.put("key2", "value2")
        self.assertEqual(len(self.table), 2)
        for index in range(100):
            self.table.put(str(index), index)
        self.assertEqual(len(self.table), 102)


if __name__ == "__main__":
    unittest.main()
