"""Модуль с реализацией метакласса"""


class CustomMeta(type):
    """Метакласс для изменения названий"""
    def _new_setattr(cls, attr_name, attr_value):
        if not attr_name.startswith("__") and not attr_name.endswith("__"):
            attr_name = "custom_" + attr_name

        cls.__class__.__base__.__setattr__(cls, attr_name, attr_value)

    def __new__(mcs, name, bases, attrs):
        new_attrs = {}

        for attr_name, attr_value in attrs.items():
            if not attr_name.startswith("__") and not attr_name.endswith("__"):
                new_attrs["custom_" + attr_name] = attr_value
            else:
                new_attrs[attr_name] = attr_value

        new_attrs["__setattr__"] = mcs._new_setattr

        return super().__new__(mcs, name, bases, new_attrs)

    def __setattr__(cls, attr_name, attr_value):
        if not attr_name.startswith("__") and not attr_name.endswith("__"):
            attr_name = "custom_" + attr_name

        super().__setattr__(attr_name, attr_value)
