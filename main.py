# Тестированию подвергается второй из приведенных классов, "Transport"

class Pet:
    """Базовый класс Питомец"""
    def __init__(self, name: str, owner: str):
        self._name = name
        self._owner = owner

    @property
    def name(self)   -> str:
        """Возвращает имя питомца"""
        return self._name

    @property
    def owner(self)  -> str:
        """Возвращает имя владельца"""
        return self._owner

    @owner.setter
    def owner(self, owner_: str)   -> str:
        """Устанавливает имя владельца"""
        if not isinstance(owner_, str):
            raise TypeError('Имя хозяина должно быть типа str')
        self._owner = owner_


class Cat(Pet):
    """Дочерний класс Кот"""
    def __init__(self, name: str, owner: str, kittens: int, feed: str):
        super().__init__(name, owner)
        self._kittens = kittens
        self._feed = feed

    @property
    def kittens(self) -> int:
        """Возвращает количество котят у кошки"""
        return self._kittens

    @kittens.setter
    def kittens(self, kittens_: int):
        """Устанавливает количество котят у кошки"""
        if not isinstance(kittens_, int):
            raise TypeError('Количество котят должно быть типа int')
        if kittens_ < 0:
            raise ValueError('Количество котят должно быть больше нуля')
        self._kittens = kittens_

    @property
    def feed(self) -> str:
        """Возвращает наименование корма"""
        return self._feed

    @feed.setter
    def feed(self, feed_: str):
        """Устанавливает наименование корма"""
        if not isinstance(feed_, str):
            raise TypeError('Наименование корма должно быть типа str')
        self._feed = feed_


class Dog(Pet):
    """Дочерний класс Собака"""
    def __init__(self, name: str, owner: str, in_family: int, breed: str):
        super().__init__(name, owner)
        self._in_family = in_family
        self._breed = breed

    @property
    def in_family(self) -> int:
        """Возвращает количество лет в семье"""
        return self._in_family

    @in_family.setter
    def in_family(self, in_family_: int):
        """Устанавливает количество лет в семье"""
        if not isinstance(in_family_, int):
            raise TypeError('Количество лет в семье должно быть типа int')
        if in_family_ < 0:
            raise ValueError('Количество лет в семье должно быть больше нуля')
        self._in_family = in_family_

    @property
    def breed(self) -> str:
        """Возвращает наименование породы"""
        return self._breed

    @breed.setter
    def breed(self, breed_: str):
        """Устанавливает наименование породы"""
        if not isinstance(breed_, str):
            raise TypeError('Наименование породы должно быть типа str')
        self._breed = breed_


class Transport:
    """Базовый класс Транспорт"""
    class_name = 'Transport'
    def __init__(self, year_production: int, model:str):
        self._year_production = year_production
        self._model = model

    @property
    def year_production(self) -> int:
        """Возвращает год выпуска ТС"""
        return self._year_production

    @property
    def model(self) -> str:
        """Возвращает выпуска ТС"""
        return self._model

    @classmethod
    def name_upper(cls):
        return cls.class_name.upper()


class Auto(Transport):
    """Дочерний класс Автомобиль"""
    def __init__(self, year_production: int, model: str, old_mileage: int, new_mileage: int):
        super().__init__(year_production, model)
        self._old_mileage = old_mileage
        self._new_mileage = new_mileage

    @property
    def old_mileage(self) -> int:
        """Возвращает пробег до приобретения автомобиля"""
        return self._old_mileage

    @old_mileage.setter
    def old_mileage(self, old_mileage_: int):
        """Устанавливает пробег до приобретения автомобиля"""
        if not isinstance(old_mileage_, int):
            raise TypeError('Пробег должен быть типа int')
        if old_mileage_ < 0:
            raise ValueError('Пробег должен быть больше нуля')
        self._old_mileage = old_mileage_

    @property
    def new_mileage(self) -> int:
        """Возвращает пробег до приобретения автомобиля"""
        return self._new_mileage

    @new_mileage.setter
    def new_mileage(self, new_mileage_: int):
        """Устанавливает пробег после приобретения автомобиля"""
        if not isinstance(new_mileage_, int):
            raise TypeError('Пробег должен быть типа int')
        if new_mileage_ < 0:
            raise ValueError('Пробег должен быть больше нуля')
        self._new_mileage = new_mileage_

    def mileage(self):
        """Расчет пробега у текущего хозяина"""
        self.mileage_ = self.new_mileage - self.old_mileage
        return(f'Текущий владелец проехал на автомобиле {self.mileage_} км')

class Bus(Transport):
    """Дочерний класс Автобус"""
    def __init__(self, year_production: int, model: str, fuel_consumption: int, volume_of_tank: int):
        super().__init__(year_production, model)
        self._fuel_consumption = fuel_consumption
        self._volume_of_tank = volume_of_tank

    @property
    def fuel_consumption(self) -> int:
        """Возвращает расход бензина на 100 км"""
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, fuel_consumption_: int):
        """Устанавливает расход бензина на 100 км"""
        if not isinstance(fuel_consumption_, int):
            raise TypeError('Расход должен быть типа int')
        if fuel_consumption_ < 0:
            raise ValueError('Расход должен быть больше нуля')
        self._fuel_consumption = fuel_consumption_

    @property
    def volume_of_tank(self) -> int:
        """Возвращает объем бензобака"""
        return self._volume_of_tank

    @volume_of_tank.setter
    def volume_of_tank(self, volume_of_tank_: int):
        """Устанавливает объем бензобака"""
        if not isinstance(volume_of_tank_, int):
            raise TypeError('Объем бензобака должен быть типа int')
        if volume_of_tank_ < 0:
            raise ValueError('Объем бензобака должен быть больше нуля')
        self._volume_of_tank = volume_of_tank_

    def fuel_reserve(self):
        """Определяет запас хода на полном баке"""
        self.fuel_reserve_ = self.volume_of_tank // self.fuel_consumption * 100
        return(f'Запас хода на полном баке около {self.fuel_reserve_} км')

    def tank_cost(self, fuel_cost: float):
        """Определяет стоимость бака бензина"""
        self.tank_cost_ = self.volume_of_tank * fuel_cost
        return(f'Бак бензина стоит {self.tank_cost_} руб')

    @staticmethod
    def are_autos_equal(auto1: Auto, auto2: Auto):
        return (auto1.model == auto2.model) and (auto1.year_production == auto2.year_production)


if __name__ == "__main__":
    auto_1 = Auto(2012, 'Rio', 35000, 102000)
    auto_2 = Auto(2015, 'Sorento', 5700, 164000)
    bus_1 = Bus(2022, 'СитиРитм', 27, 200)
    bus_2 = Bus(2020, 'Курсор', 27, 220)

    print(bus_1.tank_cost(55))
    print(auto_2.mileage())
    print(Bus.are_autos_equal(auto_1, auto_2))