# Метод сохранения в подклассе ReadOnlyDocument выбросит исключение, если
# кто-то попытается вызвать его метод сохранения. Базовый метод не имеет
# такого ограничения (нарушение п.3).
#
# Соотвественно клиентскому коду нужно постоянно проверять
# тип документа при сохранении документов, а следовательно вытекает еще одно
# нарушение - open/close принципа, т.к клиентский код начинает зависеть от конкретного класса.
# И в случае, если появится еще один тип документа, то клиентский код придется
# дописывать дополнительными условиями на проверки нового типа документа.


from typing import List


class Document:
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename

    def load(self):
        pass

    def save(self):
        pass


class ReadOnlyDocument(Document):
    def save(self):
        raise PermissionError('Can not save read-only document')


# Клиентский код
class Project:
    def __init__(self, documents: List[Document]):
        self.documents = documents

    def load_all(self):
        for document in self.documents:
            document.load()

    def save_all(self):
        for document in self.documents:
            # Нарушение open/close принципа
            if not isinstance(document, ReadOnlyDocument):
                document.save()
