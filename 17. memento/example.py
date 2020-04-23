from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters
from typing import List


def generate_random_str(length: int = 10):
    return ''.join(sample(ascii_letters, length))


class Snapshot(ABC):
    """
    Интерфейс Снимка (Memento).

    Предоставляет абстрактные свойства извлечения метаданных снимка, таких как
    дата создания и название. Однако он не раскрывает состояние Создателя.
    """

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def date(self):
        pass


class Originator:
    """
    Класс Создателя.

    Содержит внутри себя внутреннее состояния, которое может со временем меняться.
    Он также способен делать снимки своего состояния и восстанавливать прошлое состояние, если
    подать в него готовый снимок.
    """
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state

    def do_something(self):
        """
        Бизнес-логика Создателя может повлиять на его внутреннее состояние.
        Поэтому клиент должен выполнить резервное копирование состояния с
        помощью метода save перед запуском методов бизнес-логики.
        """
        self._state = generate_random_str()

    def save(self) -> Snapshot:
        """Сохраняет текущее состояние внутри снимка."""
        return OriginatorSnapshot(self, self._state)

    def restore(self, snapshot: Snapshot):
        """Восстанавливает состояние Создателя из объекта снимка."""
        snapshot: OriginatorSnapshot
        self._state = snapshot.state


class OriginatorSnapshot(Snapshot):
    """
    Конкретный Снимок Создателя (реализация Memento).

    Надежней всего делать объекты снимков неизменяемыми и передавать в них состояние
    через конструктор.
    """

    def __init__(self, originator, state):
        self._originator = originator
        self._state = state
        self._datetime = datetime.now()

    @property
    def state(self):
        """Создатель использует это свойство, когда восстанавливает свое состояние."""
        return self._state

    @property
    def name(self):
        """
        Вывод имени снимка.

        Используется Опекуном для отображения метаданных.
        """
        return '{0} / {1}'.format(self._datetime, self._state)

    @property
    def date(self):
        """
        Вывод даты снимка.

        Используется Опекуном для отображения метаданных.
        """
        return self._datetime


class Caretaker:
    """
    Класс Опекуна.

    Не зависит от конкретного Снимка. Таким образом, он не имеет доступа
    к состоянию создателя, хранящемуся внутри снимка. Он работает со всеми снимками
    через базовый интерфейс Снимка (Snapshot).

    Должен знать, когда делать снимок создателя, и когда его нужно восстанавливать.
    Также хранит историю прошлых состояний создателя в виде списка снимков (работаем с ним как со стеком).
    Если понадобится сделать отмену, он возьмет последний снимок и передаст его создателю для восстановления.
    """

    def __init__(self, originator: Originator) -> None:
        self._originator = originator
        self._snapshots: List[Snapshot] = []

    def backup(self):
        snapshot = self._originator.save()
        self._snapshots.append(snapshot)

    def undo(self):
        if not len(self._snapshots):
            return

        snapshot = self._snapshots.pop()
        self._originator.restore(snapshot)

    def show_history(self):
        for snapshot in self._snapshots:
            print(snapshot.name)


if __name__ == '__main__':
    org = Originator('Hello, world')
    caretaker = Caretaker(org)

    print('Меняем состояние...')
    for _ in range(3):
        caretaker.backup()
        org.do_something()

    print('Выводим историю...')
    caretaker.show_history()

    print('Состояние ДО = {0}'.format(org._state))
    print('Отменяем две последних операций...')
    caretaker.undo()
    caretaker.undo()
    print('Состояние ПОСЛЕ = {0}'.format(org._state))
