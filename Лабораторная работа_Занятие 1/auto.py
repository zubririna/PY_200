import doctest


class Auto:
    def __init__(self, auto_brand: str, year_of_issue: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"
        :param auto_brand: Наименование марки автомобиля
        :param year_of_issue: Год выпуска автомобиля
        Примеры:
        >>> auto = Auto("Kia", 2013)  # инициализация экземпляра класса
        """
        if not isinstance(auto_brand, str):
            raise TypeError("Наименование автомобиля должно быть типа str")
        self.auto_brand = auto_brand

        if not isinstance(year_of_issue, int):
            raise TypeError("Год выпуска автомобиля должен быть типа int")
        if not 1990 < year_of_issue < 2023:
            raise ValueError("Такого года выпуска автомобиля не может быть")
        self.year_of_issue = year_of_issue

    def is_korean(self, brand_list: list) -> bool:
        """
        Функция, которая проверяет, является ли автомобиль корейским
        :param brand_list: Перечень корейских автомобилей
        :return: Является ли автомобиль корейским
        Примеры:
        >>> auto = Auto("Kia", 2013)
        >>> auto.is_korean(brand_list)
        True
        """
        self.brand_list = brand_list

        brand_list= ['Kia', 'Hyundai', 'SsangYong', 'Daewoo']
        if self.auto_brand in brand_list:
            print('Производитель автомобиля - Корея')
        else:
            print('Автомобиль произведен не в Корее')



    def need_maintenance(self, auto_mileage: int) -> bool:
        """
        Функция, которая проверяет, нуждается ли автомобиль в техобслуживании
        :param auto_mileage: текущий пробег автомобиля
        :return: Нуждается ли автомобиль в техобслуживании
        Примеры:
        >>> auto = Auto("Kia", 2013)
        >>> auto.need_maintenance(30000)
        True
        """

        if auto_mileage < 0:
            raise ValueError("Пробег автомобиля должен быть положительным числом")
        self.auto_mileage = auto_mileage

        if auto_mileage % 15000 = 0:
            print ('Автомобиль нуждается в техосмотре')
        else:
            print('Автомобиль не нуждается в техосмотре')



if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации