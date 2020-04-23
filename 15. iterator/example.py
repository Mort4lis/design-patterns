from collections.abc import Iterable, Iterator
from typing import Any, List

"""
Для создания итератора в Python есть два абстрактных класса из встроенного
модуля collections.abc - Iterable, Iterator. Нужно реализовать метод __iter__() в
итерируемом объекте (списке), а метод __next__() в итераторе.
"""


class ListIterator(Iterator):
    """
    Конкретные Итераторы реализуют различные алгоритмы обхода. Эти классы
    постоянно хранят текущее положение обхода.

    Атрибут _position хранит текущее положение обхода. У итератора может быть
    множество других полей для хранения состояния итерации, особенно когда он
    должен работать с определённым типом коллекции.
    """

    def __init__(self, collection: List[Any], reverse=False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> Any:
        """
        Метод __next __() должен вернуть следующий элемент в последовательности.
        При достижении конца коллекции и в последующих вызовах должно вызываться
        исключение StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += - 1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class ListCollection(Iterable):
    """
    Конкретные Коллекции предоставляют один или несколько методов для получения
    новых экземпляров итератора, совместимых с классом коллекции.
    """

    def __init__(self) -> None:
        self._collection: List[Any] = []

    def __iter__(self) -> ListIterator:
        """
        Метод __iter__() возвращает объект итератора, по умолчанию мы возвращаем
        итератор с сортировкой по возрастанию.
        """
        return ListIterator(self._collection)

    def get_reverse_iterator(self) -> ListIterator:
        return ListIterator(self._collection, reverse=True)

    def add(self, *items) -> None:
        for item in items:
            self._collection.append(item)


if __name__ == '__main__':
    list_collection = ListCollection()
    list_collection.add(5, 2, 6, 1, 0, 10)
    for item in list_collection:
        print(item)

    print('-' * 75)

    for item in list_collection.get_reverse_iterator():
        print(item)
