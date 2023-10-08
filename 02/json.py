import json

def keyword_callback(keyword, field):
    print('Ключевое имя "' + keyword + '" найдено в поле "' + field + '".')

def parse_json(json_str: str, required_fields=None, keywords=None, keyword_callback=None):
    json_doc = json.loads(json_str)

    if required_fields is None:
        required_fields = []

    if keywords is None:
        keywords = []

    for key, value in json_doc.items():
        if key in required_fields:
            for keyword in keywords:
                if keyword in value:
                    keyword_callback(keyword, key)

json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
required_fields = ["key1", "key2"]
keywords = ["word2", "word3"]
parse_json(json_str, required_fields, keywords, keyword_callback)
