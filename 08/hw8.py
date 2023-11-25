"""Реализация собственной хэш-таблицы"""


class HashTable:
    """Класс хэш-таблицы"""
    def __init__(self, initial_capacity=10, load_factor=0.7):
        """Инициализация хэш-таблицы"""
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [None] * self.capacity

    def __hash_function(self, key):
        """Получение хэш-значения для заданного ключа"""
        return hash(key) % self.capacity

    def __rehash(self):
        """Перехэширование таблицы"""
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0
        for item in old_table:
            if item is not None:
                self.__insert(item[0], item[1])

    def __insert(self, key, value):
        """Вставка пары ключ-значение"""
        index = self.__hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.capacity
        self.table[index] = (key, value)
        self.size += 1

    def __expand(self):
        """Проверка необходимости расширения хэш-таблицы"""
        if self.size / self.capacity >= self.load_factor:
            self.__rehash()

    def put(self, key, value):
        """Добавление пары ключ-значение в хэш-таблицу"""
        self.__expand()
        self.__insert(key, value)

    def get(self, key):
        """Получение значения по заданному ключу"""
        index = self.__hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.capacity
        raise KeyError(key)

    def __len__(self):
        """Получение текущего размера хэш-таблицы"""
        return self.size
