"""Тестирование LRU-кэш"""
import unittest
from hw5 import LRUCache


class TestCustomList(unittest.TestCase):
    """Класс тестирования"""
    def test_1(self):
        """Первый тест (удаление элемента с ключом k3)"""
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        assert cache.get("k3") is None
        assert cache.get("k2") == "val2"
        assert cache.get("k1") == "val1"

        cache.set("k3", "val3")

        assert cache.get("k3") == "val3"
        assert cache.get("k2") is None
        assert cache.get("k1") == "val1"

    def test_2(self):
        """Второй тест (удаление элемента с ключом 1)"""
        cache = LRUCache(2)

        cache.set(1, "one")
        cache.set(2, "two")

        cache.get(1)
        cache.get(2)

        cache.set(3, "three")

        self.assertIsNone(cache.get(1))

    def test_3(self):
        """Третий тест (обновление элемента с ключом 1)"""
        cache = LRUCache(2)

        cache.set(1, "one")
        cache.set(2, "two")

        cache.set(1, "updated one")

        self.assertEqual(cache.get(1), "updated one")

    def test_4(self):
        """Второй тест (удаление элемента с ключом k3)"""
        cache = LRUCache(4)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")
        cache.set("k4", "val4")

        assert cache.get("k5") is None
        assert cache.get("k3") == "val3"
        assert cache.get("k4") == "val4"
        assert cache.get("k2") == "val2"
        assert cache.get("k1") == "val1"

        cache.set("k5", "val5")

        assert cache.get("k5") == "val5"
        assert cache.get("k3") is None
        assert cache.get("k1") == "val1"
        assert cache.get("k2") == "val2"
        assert cache.get("k4") == "val4"


if __name__ == '__main__':
    unittest.main()
