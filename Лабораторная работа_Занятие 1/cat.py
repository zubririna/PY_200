import doctest


class Kitty:
    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта "Котя"
        :param name: Кличка коти
        :param age: Возраст коти
        Примеры:
        >>> kitty = Kitty("Dulsinea", 5)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Кличка коти должна быть типа str")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст коти должен быть типа int")
        if age <= 0 or age >= 25:
            raise ValueError("Недопустимый возраст для коти")
        self.age = age
        self.weight = None
        self.init_weight()

    def eat_norm(self, min_eat: int, max_eat: int, fact_eat: int) -> bool:
        """
        Функция, которая проверяет, нормально ли ест котя
        :param min_eat: Минимальная норма еды
        :param max_eat: Максимальная норма еды
        :param fact_eat: Фактическое потребление еды котом
        :return: Ест ли кот нормально
        Примеры:
        >>> kitty = Kitty("Dulsinea", 5)
        >>> kitty.eat_norm(60, 120, 80)
        True
        """
        if min_eat < fact_eat < max_eat:
            return True

    def init_weight(self) -> None:
        """
        Добавление атрибута "Вес коти"
        :return: None
        Примеры:
        >>> kitty = Kitty("Dulsinea", 5)
        >>> kitty.init_weight()
        """
        self.weight = 3500



if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации