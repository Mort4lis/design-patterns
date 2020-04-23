# Типы параметров переопределенного метода в подклассе должны совпадать
# или быть более абстрактными, чем типы параметров базового метода.


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


class Feeder:
    def feed(self, cat: Cat):
        pass


# Хорошо:
class GoodFeeder(Feeder):
    def feed(self, cat: Animal):
        pass


# Плохо:
class BadFeeder(Feeder):
    def feed(self, cat: BengalCat):
        pass


def client_code(feeder, cat):
    feeder.feed(cat)


# Наш базовый клиентский код
instance = Cat()
client_code(Feeder(), instance)

# Если мы передадим в GoodFeeder кота, то все отработает.
# Т.к GoodFeeder может накормить любое животное, в том числе и кота
client_code(GoodFeeder(), instance)

# А в этом случае, клиентский код может поломаться, т.к BadFeeder может
# накормить только бенгалов, а мы передаем абстратного кота
client_code(BadFeeder(), instance)
