from typing import List


class Document:
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename

    def load(self):
        pass


class WritableDocument(Document):
    def save(self):
        pass


# Клиентский код
class Project:
    def __init__(self, documents: List[Document], writable_documents: List[WritableDocument]):
        self.documents = documents
        self.writable_documents = writable_documents

    def load_all(self):
        for document in self.documents:
            document.load()

    def save_all(self):
        for document in self.writable_documents:
            document.save()
