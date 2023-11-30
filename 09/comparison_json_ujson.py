"""Тестирование производительности json и ujson"""
import time
import json
import ujson


def test_json_performance(file):
    """Функция тестирования производительности json и ujson"""
    with open(file, encoding="utf-8") as f:
        json_data = f.read()

    start = time.time()

    for _ in range(100):
        json.loads(json_data)

    end = time.time()
    json_time = (end - start) * 1000
    start = time.time()

    for _ in range(100):
        ujson.loads(json_data)
    end = time.time()

    ujson_time = (end - start) * 1000
    print(f"json loads time: {json_time}")
    print(f"ujson loads time: {ujson_time}")


JSON_FILE = "/Users/macbookpro/Desktop/500kb.json"
test_json_performance(JSON_FILE)
