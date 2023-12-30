# Память, профилирование

# Проверка корректности и стиля кода с помощью pylint и flake8:
![Image alt](https://github.com/VetaShine/OOPch/blob/main/hw11_1.png)

# Тестирование работы программы:
# 1. Сравнение использования weakref и слотов
# Создание пачки экземпляров:
Классы со слотами и атрибутами weakref имеют лучшие указатели чем обычные ссылки.
![Image alt](https://github.com/VetaShine/OOPch/blob/main/hw11_2.png)
# Доступ к атрибутам:
Классы со слотами имеют значительный отрыв по времени.
![Image alt](https://github.com/VetaShine/OOPch/blob/main/hw11_3.png)
# Изменение атрибутов:
При изменении обычные ссылки показали себя лучше других.
![Image alt](https://github.com/VetaShine/OOPch/blob/main/hw11_4.png)
# Удаление атрибутов:
При удалении обычные ссылки также показали себя лучше других.
![Image alt](https://github.com/VetaShine/OOPch/blob/main/hw11_5.png)
# 2. Профилирование
# Профилирование вызовов:
# 1) Создание пачки экземпляров:
![Image alt](https://github.com/VetaShine/OOPch/blob/main/hw11_6.png)
# 2) Доступ к атрибутам:
![Image alt](https://github.com/VetaShine/OOPch/blob/main/hw11_7.png)
![Image alt](https://github.com/VetaShine/OOPch/blob/main/hw11_7_1.png)
![Image alt](https://github.com/VetaShine/OOPch/blob/main/hw11_7_2.png)
# 3) Изменение атрибутов:
![Image alt](https://github.com/VetaShine/OOPch/blob/main/hw11_8.png)
# 4) Удаление атрибутов:
![Image alt](https://github.com/VetaShine/OOPch/blob/main/hw11_9.png)
# Профилирование памяти:
Классы со слотами значительно экономят память в отличие от других вариантов классов.
![Image alt](https://github.com/VetaShine/OOPch/blob/main/hw11_10.png)
