# Класс Employee имеет несколько причин для изменения:
# 1. Управление данными сотрудника
# 2. Формирование отчета для печати


class Employee:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def print_time_sheet_reports(self):
        pass
