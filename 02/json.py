"""Работа со строками json"""
import json

def keyword_callback(keyword, field):
    """Вывод результата на экран"""
    print('Ключевое имя "' + keyword + '" найдено в поле "' + field + '".')

def parse_json(json_str: str, required_fields=None, keywords=None, callback=None):
    """Парсер строки json"""
    json_doc = json.loads(json_str)

    if required_fields is None:
        required_fields = []

    if keywords is None:
        keywords = []

    for key, value in json_doc.items():
        if key in required_fields:
            for keyword in keywords:
                if keyword in value:
                    callback(keyword, key)

JSON_STRINGS = '{"key1": "Word1 word2", "key2": "word2 word3"}'
fields = ["key1", "key2"]
keynames = ["word2", "word3"]
parse_json(JSON_STRINGS, fields, keynames, keyword_callback)
