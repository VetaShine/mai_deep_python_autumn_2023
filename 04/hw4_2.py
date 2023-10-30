"""Дескрипторы с проверками типов и значений данных"""
class ArtTypeDescriptor:
    """Дескриптор вида произведения искусства"""
    def __get__(self, instance, owner):
        return instance._art_type

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Art type should be a string")
        allowed_types = ["painting", "sculpture", "architecture"]
        if value not in allowed_types:
            raise ValueError("Invalid art type")
        instance._art_type = value


class ArtYearDescriptor:
    """Дескриптор года создания произведения искусства"""
    def __get__(self, instance, owner):
        return instance._art_year

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Art year should be an integer")
        if value < 0 or value > 2023:
            raise ValueError("Invalid art year")
        instance._art_year = value


class ArtNameDescriptor:
    """Дескриптор названия произведения искусства"""
    def __get__(self, instance, owner):
        return instance._art_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Art name should be a string")
        if len(value) > 256:
            raise ValueError("Art name is too long")
        instance._art_name = value
