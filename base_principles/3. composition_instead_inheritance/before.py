# Развитие классов в нескольких плоскостях
# (тип груза * тип двигателя * тип навигации)
# приводит к комбинаторному взрыву
#
# Проблема 1. Разрастание классов
# Проблема 2. Дублирование кода, т.к подклассы не могут
# наследовать нескольких родителей одновременно (относится к стандартным ООЯП)


class Transport:
    pass


class Truck(Transport):
    pass


class Car(Transport):
    pass


class ElectricTruck(Truck):
    pass


class CombustionEngineTruck(Truck):
    pass


class ElectricCar(Car):
    pass


class CombustionEngineCar(Car):
    pass


class AutopilotElectricTruck(ElectricTruck):
    pass


class AutopilotCombustionEngineTruck(CombustionEngineTruck):
    pass


class AutopilotElectricCat(ElectricCar):
    pass


class AutopilotCombustionEngineCar(CombustionEngineCar):
    pass
