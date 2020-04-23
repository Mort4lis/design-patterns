# Проблему разрастания иерархии классов можно решить с помощью композиции
#
# Преимущество 1: Вместо того, чтобы объекты сами реализовывали то или иное поведение,
# они могут делегировать его другим объектам.
#
# Преимущество 2: Можно заменять объекты композиции прямо во время выполнения
# программы (например, подставив в объект транспорта другой объект двигателя)


class Engine:
    def move(self):
        raise NotImplementedError


class CombustionEngine(Engine):
    def move(self):
        pass


class ElectricEngine(Engine):
    def move(self):
        pass


class Driver:
    def navigate(self):
        raise NotImplementedError


class Robot(Driver):
    def navigate(self):
        pass


class Human(Driver):
    def navigate(self):
        pass


class Transport:
    def __init__(self, engine: Engine, driver: Driver):
        self.engine = engine
        self.driver = driver

    def deliver(self, destination, cargo):
        pass


combustion = CombustionEngine()
electric = ElectricEngine()
car = Transport(combustion, Human())

# ....

car.engine = electric
