from abc import ABC, abstractmethod


class DataMiner(ABC):
    """
    Абстрактный класс.

    Определяет шаги алгоритма и содержит шаблонный метод, состоящий из вызова
    этих шагов. Шаги могут быть как абстрактными, так и содержать реализацию
    по умолчанию.
    """

    @staticmethod
    def open_file(path: str):
        return open(path)

    @staticmethod
    def close_file(file):
        file.close()

    @classmethod
    def mine(cls, path):
        """Шаблонный метод определяет скелет алгоритма."""
        file = cls.open_file(path)
        raw_data = cls.extract_data(file)
        data = cls.parse_data(raw_data)
        cls.hook1()
        analysis = cls.analyze_data(data)
        cls.send_report(analysis)
        cls.close_file(file)
        cls.hook2()

    @classmethod
    @abstractmethod
    def extract_data(cls, file) -> list:
        """Шаг алгоритма (абстрактный)."""
        pass

    @classmethod
    @abstractmethod
    def parse_data(cls, raw_data) -> list:
        pass

    @classmethod
    def analyze_data(cls, data) -> list:
        """Шаг алгоритма (с реализацией по умолчанию)."""
        print('Анализ данных...')
        return []

    @classmethod
    def send_report(cls, data) -> None:
        print('Отправка отчета...')

    # Это «хуки». Подклассы могут переопределять их, но это не обязательно,
    # поскольку у хуков уже есть стандартная (но пустая) реализация. Хуки
    # предоставляют дополнительные точки расширения в некоторых критических
    # местах алгоритма.

    @classmethod
    def hook1(cls):
        pass

    @classmethod
    def hook2(cls):
        pass


"""
Конкретные классы определяют некоторые (или все) шаги алгоритма.
Конкретные классы не переопределяют шаблонный метод.
"""


class PdfDataMiner(DataMiner):
    @classmethod
    def extract_data(cls, file) -> list:
        print('Извлечение данных из PDF...')
        return []

    @classmethod
    def parse_data(cls, raw_data) -> list:
        print('Парсинг данных из PDF...')
        return []


class CsvDataMiner(DataMiner):
    @classmethod
    def extract_data(cls, file) -> list:
        print('Извлечение данных из CSV...')
        return []

    @classmethod
    def parse_data(cls, raw_data) -> list:
        print('Парсинг данных из CSV...')
        return []


class DocDataMiner(DataMiner):
    @classmethod
    def extract_data(cls, file) -> list:
        print('Извлечение данных из DOC..')
        return []

    @classmethod
    def parse_data(cls, raw_data) -> list:
        print('Парсинг данных из DOC...')
        return []


if __name__ == '__main__':
    DocDataMiner.mine('file')
    print('-' * 75)
    PdfDataMiner.mine('file')
