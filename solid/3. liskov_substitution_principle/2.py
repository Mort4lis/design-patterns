class Animal:
    def __init__(self):
        self.energy = 50

    def eat(self):
        pass


class Cat(Animal):
    def eat(self):
        pass


class BengalCat(Cat):
    def eat(self):
        pass


class Shop:
    def buy_cat(self) -> Cat:
        pass


# Хорошо:
class GoodShop(Shop):
    def buy_cat(self) -> BengalCat:
        pass


# Плохо
class BadShop(Shop):
    def buy_cat(self) -> Animal:
        pass


def client_code(shop: Shop):
    instance = shop.buy_cat()

    class Bag:
        def put(self, cat: Cat):
            pass

    Bag().put(instance)


# Наш базовый клиентский код:
client_code(Shop())

# Метод `buy_cat` класса GoodShop возвращает бенгальского кота.
# Т.к базовый код работает с котом, то и бенгальским котом все должно работать
client_code(GoodShop())

# Здесь клиентский код может сломаться, т.к метод `buy_cat` возвращает абстрактное животное,
# это может быть "крокодил", который не влезет в сумку для кота
client_code(BadShop())
