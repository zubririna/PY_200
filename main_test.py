import unittest
from main import Auto
from main import Bus


class TestTransport(unittest.TestCase):

    auto1_ = Auto (2012, 'Rio', 35000, 102000)
    auto2_ = Auto(2015, 'Sorento', 5700, 164000)
    auto3_ = Auto(2010, 'Cerato', 125090, 193587)
    bus1_ = Bus(2022, 'СитиРитм', 27, 200)
    bus2_ = Bus(2020, 'Курсор', 27, 220)
    bus3_ = Bus(2018, 'Базовые>', 25, 215)

    def test_mileage(self):
        auto1_ = Auto(2012, 'Rio', 35000, 102000)
        auto2_ = Auto(2015, 'Sorento', 5700, 164000)
        auto3_ = Auto(2010, 'Cerato', 125090, 193587)
        print('Проверка mileage')
        self.assertEqual(auto1_.mileage(), f'Текущий владелец проехал на автомобиле 67000 км')
        self.assertEqual(auto2_.mileage(), f'Текущий владелец проехал на автомобиле 158300 км')
        self.assertEqual(auto3_.mileage(), f'Текущий владелец проехал на автомобиле 68497 км')


    def test_fuel_reserve(self):
        bus1_ = Bus(2022, 'СитиРитм', 20, 200)
        bus2_ = Bus(2020, 'Курсор', 22, 220)
        bus3_ = Bus(2018, 'Базовые>', 23, 230)
        print('Проверка fuel_reserve')
        self.assertEqual(bus1_.fuel_reserve(), f'Запас хода на полном баке около 1000 км')
        self.assertEqual(bus2_.fuel_reserve(), f'Запас хода на полном баке около 1000 км')
        self.assertEqual(bus3_.fuel_reserve(), f'Запас хода на полном баке около 1000 км')

    def test_tank_cost(self):
        bus1_ = Bus(2022, 'СитиРитм', 20, 200)
        bus2_ = Bus(2020, 'Курсор', 22, 220)
        bus3_ = Bus(2018, 'Базовые>', 23, 230)
        print('Проверка tank_cost')
        self.assertEqual(bus1_.tank_cost(55), f'Бак бензина стоит 11000 руб')
        self.assertEqual(bus2_.tank_cost(47), f'Бак бензина стоит 10340 руб')
        self.assertEqual(bus3_.tank_cost(59), f'Бак бензина стоит 13570 руб')


    def test_are_autos_equal(self):
        auto1_ = Auto(2012, 'Rio', 35000, 102000)
        auto2_ = Auto(2015, 'Sorento', 5700, 164000)
        auto3_ = Auto(2010, 'Cerato', 125090, 193587)
        auto4_ = Auto(2012, 'Rio', 37000, 102000)
        print('Проверка are_autos_equal')
        self.assertEqual(Bus.are_autos_equal(auto1_, auto2_), False)
        self.assertEqual(Bus.are_autos_equal(auto2_, auto3_), False)
        self.assertEqual(Bus.are_autos_equal(auto1_, auto4_), True)



if __name__ == '__main__':
    unittest.main()
