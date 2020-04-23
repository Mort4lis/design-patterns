# Класс Cat жестко зависит от класса Sausage.


class Sausage:
    def get_nutrution(self) -> int:
        pass

    def get_color(self) -> str:
        pass


class Cat:
    def __init__(self):
        self.energy = 60

    def eat(self, s: Sausage) -> None:
        self.energy += s.get_nutrution()
