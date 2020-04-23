# Проблему можно решить, выделив операцию печати в отдельный класс


class Employee:
    def __init__(self, name):
        self.name = name


class TimeSheetReport:
    def print(self, employee: Employee):
        pass
