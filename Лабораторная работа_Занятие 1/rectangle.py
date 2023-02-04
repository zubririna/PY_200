import doctest
from typing import Union

class Rectangle:
    def __init__(self, length: Union[int, float], width: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Прямоугольник"
        :param length: длина стороны прямоугольника
        :param width: ширина стороны прямоугольника
        Примеры:
        >>> rectangle = Rectangle(60, 10)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина прямоугольника должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина прямоугольника должна быть больше нуля")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина прямоугольника должна быть типа int или float")
        if width < 0:
            raise ValueError("Ширина прямоугольника должна быть больше нуля")
        self.width = width


    def rectangle_area(self) -> Union[int, float]:
        """
        Функция, которая считает площадь прямоугольника
        :return: Площадь прямоугольника
        Примеры:
        >>> rectangle = Rectangle(60, 10)
        600
        """
        rectangle_area_ = rectangle.length * rectangle.width
        return(rectangle_area_)

    def rectangle_perimeter(self) -> Union[int, float]:
        """
        Функция, которая считает периметр прямоугольника
        :return: Периметр прямоугольника
        Примеры:
        >>> rectangle = Rectangle(60, 10)
        140
        """
        rectangle_perimeter_ = (rectangle.length + rectangle.width) * 2
        return (rectangle_perimeter_)



if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
