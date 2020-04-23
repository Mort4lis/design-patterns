# В данном примере высокоуровневый класс формирования бюджетных отчетов
# напрямую использует класс БД для загрузки с сохранения своей информации.


class MySQLDatabase:
    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class BudgetReport:
    def __init__(self, db: MySQLDatabase):
        self.db = db

    def open(self, date):
        pass

    def save(self):
        pass
