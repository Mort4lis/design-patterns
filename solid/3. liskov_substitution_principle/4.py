# Метод подкласса не должен ослаблять пост условия


class Database:
    def open(self):
        pass

    def close(self):
        pass


class ClientModel:
    def __init__(self, db: Database):
        self.db = db

    def do_something(self):
        # ... payload
        self.db.close()


class SubClientModel(ClientModel):
    def do_something(self):
        # ... payload
        # не вызвал self.db.close() ---> ослабление пост условий
        pass
