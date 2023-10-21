"""Реализация класса, наследующегося от list"""


class CustomList(list):
    """Класс, наследующийся от list"""

    def __add__(self, other):
        result = CustomList(self)
        count = 0

        for element in other:
            count += 1

            if count < len(result):
                result[count] += element
            else:
                result.append(element)

        return result

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        result = CustomList(self)
        count = 0

        for element in other:
            count += 1

            if count < len(result):
                result[count] -= element
            else:
                result.append(-element)

        return result

    def neg(self):
        """Changing the sign of all elements"""
        for index, element in enumerate(self):
            self[index] = -element

        return self

    def __rsub__(self, other):
        return (self - other).neg()

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __str__(self):
        return f"{list(self)} (Сумма: {sum(self)})"
