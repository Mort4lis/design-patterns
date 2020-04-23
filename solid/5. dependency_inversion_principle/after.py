# Мы можем решить проблему, создав высокоуровневый интерфейс Database
# для загрузки/сохранения данных и привязать к нему класс отчетов.
# Низкоуровневые классы тоже должны следовать этому интерфейсу, чтобы
# их объекты можно было использовать внутри объекта отчетов.

# Таким образом меняется направление зависимости. Если раньше высокий уровень зависел
# от низкого, то сейчас наоборот - низкоуровневые классы зависят от высокоуровневого
# интерфейса.


class Database:
    def insert(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError


class MySQLDatabase(Database):
    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class MongoDB(Database):
    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class BudgetReport:
    def __init__(self, db: Database):
        self.db = db

    def open(self, date):
        pass

    def save(self):
        pass
