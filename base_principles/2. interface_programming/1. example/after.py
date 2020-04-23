# Класс Cat зависит не от реализации, а от абстракции


class Food:
    def get_nutrution(self):
        raise NotImplementedError('The method `get_nutrution()` is not implemented')


class Sausage(Food):
    def get_nutrution(self):
        pass

    def get_color(self):
        pass


class Cat:
    def __init__(self):
        self.energy = 60

    def eat(self, s: Food) -> None:
        self.energy += s.get_nutrution()
