"""Реализация LRU-кэш"""


class LRUCache:
    """LRU-кэш"""
    def __init__(self, limit=42):
        """Инициализация"""
        self.limit = limit
        self.cache = {}
        self.order = []

    def get(self, key):
        """Получение значения по ключу"""
        if key not in self.cache:
            return None
        self.order.remove(key)
        self.order.insert(0, key)
        return self.cache[key]

    def set(self, key, value):
        """Добавление ключа и значения"""
        if key not in self.cache:
            if len(self.cache) >= self.limit:
                removed_key = self.order.pop()
                del self.cache[removed_key]
            self.cache[key] = value
            self.order.insert(0, key)
        else:
            self.cache[key] = value
            self.order.remove(key)
            self.order.insert(0, key)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)
