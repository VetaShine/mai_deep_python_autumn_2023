"""Тестированиe парсинга и сериализации json"""
import json
import unittest
import cjson


class CJsonTestCase(unittest.TestCase):
    """Класс тестирования парсинга и сериализации json"""
    def test_loads(self):
        """Тестирования создания словаря по строке JSON"""
        json_str = '{"apple": 30, "orange": 5, "lime": 16, "bowl": "ceramics"}'
        expected = {"apple": 30, "orange": 5, "lime": 16, "bowl": "ceramics"}
        result = cjson.loads(json_str)
        self.assertEqual(result, expected)

    def test_dumps(self):
        """Тестирования создания строки JSON по словарю"""
        json_dict = {"apple": 30, "orange": 5, "lime": 16, "bowl": "ceramics"}
        expected = '{"apple": 30, "orange": 5, "lime": 16, "bowl": "ceramics"}'
        result = cjson.dumps(json_dict)
        self.assertEqual(result, expected)

    def test_validity(self):
        """Тестирования создания словаря по строке JSON"""
        json_str = '{"apple": 30, "orange": 5, "lime": 16, "bowl": "ceramics"}'
        json_doc = json.loads(json_str)
        cjson_doc = cjson.loads(json_str)
        assert json_doc == cjson_doc

    def test_errors(self):
        """Тестирование вызова ошибок"""
        with self.assertRaises(TypeError):
            cjson.loads(5)

        with self.assertRaises(ValueError):
            cjson.loads('30')

        with self.assertRaises(ValueError):
            cjson.loads('orange')


if __name__ == "__main__":
    unittest.main()
