"""Тестирование дескрипторов"""
import unittest
from hw4_2 import ArtTypeDescriptor, ArtYearDescriptor, ArtNameDescriptor

class Artwork:
    """Класс произведения искусства"""
    art_type = ArtTypeDescriptor()
    art_year = ArtYearDescriptor()
    art_name = ArtNameDescriptor()

    def __init__(self, art_type, art_year, art_name):
        """Инициализация"""
        self.art_type = art_type
        self.art_year = art_year
        self.art_name = art_name

    def print_variables(self):
        """Вывод переменных класса"""
        print(f"Art Type: {self.art_type}")
        print(f"Art Year: {self.art_year}")
        print(f"Art Name: {self.art_name}")

    def is_year_correct(self, check):
        """Проверка года создания"""
        return self.art_year == check


class TestCustomMeta(unittest.TestCase):
    """Класс тестирования работы дескрипторов"""
    def test_art_type(self):
        """Класс тестирования дескриптора вида искусства"""
        first_artwork = Artwork("painting", 1882, "Girl in the forest")
        second_artwork = Artwork("painting", 1862, "Hunting trophy")
        third_artwork = Artwork("sculpture", 2019, "Build bridges")

        self.assertTrue(first_artwork.art_type == "painting")
        self.assertFalse(third_artwork.art_type == "painting")
        self.assertTrue(first_artwork.art_type == second_artwork.art_type)
        self.assertFalse(third_artwork.art_type == second_artwork.art_type)

    def test_art_year(self):
        """Класс тестирования дескриптора года создания"""
        first_artwork = Artwork("painting", 1882, "Girl in the forest")
        second_artwork = Artwork("painting", 1862, "Hunting trophy")
        third_artwork = Artwork("sculpture", 2019, "Build bridges")

        self.assertTrue(first_artwork.art_year == 1882)
        self.assertTrue(second_artwork.art_year == 1862)
        self.assertFalse(third_artwork.art_year == 2020)
        self.assertFalse(first_artwork.art_year == second_artwork.art_year)
        self.assertFalse(third_artwork.art_year == second_artwork.art_year)

    def test_art_name(self):
        """Класс тестирования дескриптора названия произведения искусства"""
        first_artwork = Artwork("painting", 1882, "Girl in the forest")
        second_artwork = Artwork("painting", 1862, "Hunting trophy")
        third_artwork = Artwork("sculpture", 2019, "Build bridges")

        self.assertTrue(first_artwork.art_name == "Girl in the forest")
        self.assertFalse(third_artwork.art_name == "Girl in the forest")
        self.assertTrue(third_artwork.art_name == "Build bridges")
        self.assertFalse(first_artwork.art_name == second_artwork.art_name)
        self.assertFalse(third_artwork.art_name == second_artwork.art_name)


if __name__ == '__main__':
    unittest.main()
