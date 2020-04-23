# Мы можем сделать метод получения сотрудников в базовом классе компании - абстрактным,
# а конкретные компании должны будут сами позаботиться о создании
# объектов сотрудников.

# После этого класс компании стал окончательно независим от конкретных классов сотрудников.
# Теперь мы можем добавлять в программу новые виды работников и компаний, не внося
# изменений в основной код базового класса. Данный паттерн называется ФАБРИЧНЫЙ МЕТОД

from typing import List


class Employee:
    def work(self):
        raise NotImplementedError


class Designer(Employee):
    def work(self):
        pass


class Programmer(Employee):
    def work(self):
        pass


class Tester(Employee):
    def work(self):
        pass


class Artist(Employee):
    def work(self):
        pass


class Company:
    def get_employees(self) -> List[Employee]:
        raise NotImplementedError

    def create_software(self):
        employees: List[Employee] = self.get_employees()
        for employee in employees:
            employee.work()


class GameDevCompany(Company):
    def get_employees(self) -> List[Employee]:
        return [
            Designer(),
            Artist()
        ]


class OutsourcingCompany(Company):
    def get_employees(self) -> List[Employee]:
        return [
            Programmer(),
            Programmer()
        ]
