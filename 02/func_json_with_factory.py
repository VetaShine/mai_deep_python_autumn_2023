"""Работа со строками json с использованием factory-boy"""
import json
from factory import Factory, Sequence

class JSONFactory(Factory):
    """Генерация теста"""
    class Meta:
        """Задание словаря"""
        model = dict

    key1 = Sequence(lambda n: f"Word{n} word{n+1}")
    key2 = Sequence(lambda n: f"word{n+1} word{n+2}")

def keyword_callback(keyword, field):
    """Вывод результата на экран"""
    print('Ключевое имя "' + keyword + '" найдено в поле "' + field + '".')

def parse_json_strings(json_strings, required_fields=None, keywords=None, callback=None):
    """Парсер строки json"""
    if required_fields is None:
        required_fields = []

    if keywords is None:
        keywords = []

    for json_str in json_strings:
        json_doc = json.loads(json_str)

        for key, value in json_doc.items():
            if key in required_fields:
                for keyword in keywords:
                    if keyword in value:
                        callback(keyword, key)

json_data = JSONFactory.build()
json_string = json.dumps(json_data)

JSON_STRINGS = [json_string]
print(JSON_STRINGS)
fields = ["key1", "key2"]
keynames = ["word2", "word3"]

parse_json_strings(JSON_STRINGS, fields, keynames, keyword_callback)
