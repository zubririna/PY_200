import hashlib
from random import uniform, choice
from typing import Union

# Список продуктов, которые можно купить в автомобильном магазине
prod_list = ['Тормозные колодки задние', 'Тормозные колодки передние', 'Барабан тормозной', 'Диск тормозной задний',
             'Диск тормозной передний', 'Сайлентблок задней балки ', 'Сайлентблок переднего рычага',
             'Амортизатор передний', 'Амортизатор задний', 'Стекло заднее', 'Стекло лобовое',
             'Фара левая', 'Фара правая', 'Датчик кондиционера', 'Радиатор основной', 'Барабан АКПП',
             'Диск сцепления', 'Ступица задняя', 'Ступица передняя', 'Генератор', 'Замок зажигания']

class IdCounter:
    """Класс, хранящий генератор значений id"""

    def __init__(self):
        """Создание и подготовка к работе объекта id"""
        self._id = 0

    def get_id(self):
        """Функция, возвращающая следующее значение id"""
        self._id += 1
        return self.id

    @property
    def id(self):
        """Возвращает текущее значение id"""
        return self._id


class Password:
    """Класс, выдающий хэш-значения пароля и проверяющий пароль с его хэш-значением"""

    def __init__(self, password):
        """Создание и подготовка к работе объекта password"""
        self.hash_password = self.get_hash(password)

    def password_valid(self, password):
        """Проверка правильности создания пароля (состоит из цифр и букв, размер - не менее 8 символов"""
        password_list = []
        for x in password:
            if not x.isalpha() and not x.isdigit():
                raise TypeError("Пароль должен состоять из букв и цифр")
            password_list.append(x)
        if len(password_list) < 8:
            raise ValueError("Длина пароля не менее 8 символов")

    def get_hash(self, password):
        """Выдача хэш-значения пароля с использованием модуля hashlib"""
        self.password_valid(password)
        return hashlib.sha256(password.encode()).hexdigest()

    def check_hash(self, password):
        """Поверка соотношения передаваемого пароля с хэш-значением"""
        if self.hash_password == self.get_hash(password):
            return True
        else:
            return False


class Product:
    """Класс, хранящий информацию о продукте"""
    _id_counter = IdCounter()   #id определяется при инициализации

    def __init__(self, name: str, price: Union [float, int], rating: Union [float, int]):
        """Создание и подготовка к работе объекта product"""
        self._name = name
        self._id = self._id_counter.get_id()
        self.price = price
        self.rating = rating

    def __str__(self):
        return f"id: {self._id}, Товар: {self._name}"

    def __repr__(self):
        return f"Product(id: {self._id}, Товар: {self._name}, Цена: {self.price}, Рейтинг: {self.rating})"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


class Cart:
    """Класс, хранящий информацию о корзине"""

    def __init__(self, cart=None):
        """Создание и подготовка к работе объекта корзина с проверками"""
        if cart is None:
            cart = []
        if not isinstance(cart, list):
            raise TypeError("В корзине не список")
        self.cart = cart

    def get_cart(self):
        return self.cart

    def add_in_cart(self, new_product):
        """Добавление товара в корзину"""
        self.cart.append(new_product)

    def del_from_cart_by_index(self, index):
        """Удаление товара из корзины"""
        del self.cart[index-1]


class User:
    """Класс, хранящий информацию о покупателе"""
    _id_counter = IdCounter()    #id определяется при инициализации

    def __init__(self, username, password):
        """Создание и подготовка к работе объекта User"""
        self._user_id = self._id_counter.get_id()
        self._username = username
        self._password = Password(password).get_hash(password)
        self._user_cart = Cart().get_cart()
        self.check_username(username)

    def __str__(self):
        return f"id: {self._user_id}, Логин: {self._username}"

    def __repr__(self):
        return f"User(id: {self._user_id}, Логин: {self._username}, Пароль: password1, Корзина: {self._user_cart})"

    @property
    def user_cart(self):
        return self._user_cart

    def check_username(self, username):
        """Проверка имени пользователя"""
        for x in username:
            if not x.isalpha():
                TypeError("Имя должно состоять из букв")

    def get_username(self):
        return self._username


class Store:
    """Класс, описывающий сам магазин"""
    _id_counter = IdCounter()

    def __init__(self, new_username: str, new_password):
        """Создание и подготовка к работе объекта Store с введением имени и пароля через консоль"""
        if new_username is None:
            new_username = input("Введите имя пользователя: ")
        if new_password is None:
            new_password = input("Введите пароль: ")

        self.password = Password(new_password).get_hash(new_password)
        del new_password
        self.user = User(new_username, self.password).get_username()
        self.cart = Cart().get_cart()   #для просмотра корзины пользвователя

    def add_random(self, y=1):
        """Добавление случайного товара в корзину"""
        for x in range(y):
            prod = Product(choice(prod_list), str(round(uniform(1, 100), 2)) + 'руб.', round(uniform(0, 5), 2))
            self.cart.append(prod)


if __name__ == '__main__':

    prod_1 = Product("Ступица задняя", "156.0 руб.", 4.68)
    prod_2 = Product("Тормозные колодки передние", "5978.0 руб.", 3.58)

    print("Проверка класс Cart:")
    cart_ = Cart()
    cart_.add_in_cart(prod_1)
    cart_.add_in_cart(prod_2)
    print(cart_.__dict__)
    print()

    print("Проверка класса Store, добавление рандомных товаров в корзину (5 позиций):")
    store = Store("Логин", "Пароль000")
    store.add_random(5)
    print(store.cart)
