# Несмотря на то, что каждый класс работников делает разную работу,
# мы можем свести их методы работы к одному интерфейсу
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


# Далее, мы можем применить полиморфизм в классе Company,
# трактуя всех работников через интерфейс Employee

class Company:
    def create_software(self):
        employees: List[Employee] = [
            Designer(),
            Programmer(),
            Tester()
        ]
        for employee in employees:
            employee.work()

# Выглядит лучше, но, класс Company все еще остается жестко привязан к конкретным классам
# работников. Это не очень хорошо, т.к нам может понадобиться реализовать
# несколько видов компаний. Все эти компании будут отличаться тем, какие
# конкретно работники в них нужны.
