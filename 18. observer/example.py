from abc import ABC, abstractmethod
from collections import defaultdict
from datetime import datetime
from typing import List, Optional, TextIO
from time import sleep


class EventListener(ABC):
    """
    Интерфейс Подписчиков.

    Определяет интерфейс, которым пользуется Издатель для отправки сообщения.
    В большинстве случаев, достаточно одного метода.
    """

    @abstractmethod
    def update(self, filename: str):
        pass


class EventManager:
    """
    Базовый класс Издатель.

    Содержит коллекцию Подписчиков, а также логику добавления и удаления
    подписчиков на определенные события. Содержит метод уведомления
    всех подписчиков о произошедшем событии.
    """

    def __init__(self):
        self._subscribers: defaultdict[str, List[EventListener]] = defaultdict(list)

    def subscribe(self, event: str, subscriber: EventListener):
        self._subscribers[event].append(subscriber)

    def unsubscribe(self, event: str, subscriber: EventListener):
        items = self._subscribers[event]
        for i, item in enumerate(items):
            if item is subscriber:
                return items.pop(i)

    def notify(self, event: str, data):
        for subscribers in self._subscribers[event]:
            subscribers.update(data)


class Editor:
    """
    Конкретный класс Издетель (текстовый редактор).

    Содержит интересную для других компонентов бизнес-логику. Мы могли бы сделать его
    прямым потомком от `EventManager`, но в реальной жизни это не всегда возможно
    (например, если у класса уже есть родитель, и ЯП не поддерживает множественное наследование,
    но с языком Python можно такое сделать). Поэтому здесь продемонстрирован механизм подписки
    при помощи композиции.
    """

    def __init__(self, filename):
        self.filename = filename

        self._file: Optional[TextIO] = None
        self._event_manager: Optional[EventManager] = None

    @property
    def event_manager(self):
        return self._event_manager

    @event_manager.setter
    def event_manager(self, value: EventManager):
        self._event_manager = value

    def open(self):
        """
        Метод открытия файла.

        Метод бизнес-логики, который оповещает подписчиков об изменении.
        """
        self._file = open(self.filename)
        if self.event_manager is not None:
            self.event_manager.notify('open', self.filename)

    def close(self):
        """
        Метод закрытия файла.

        Метод бизнес-логики, который оповещает подписчиков об изменении.
        """
        self._file.close()
        if self.event_manager is not None:
            self.event_manager.notify('close', self.filename)


"""
Набор конкретных подписчиков. Они реализуют добавочную функциональность, реагируя на извещения
Издателя.
"""


class EmailEventListener(EventListener):
    def __init__(self, message=''):
        self.message = message

    def update(self, filename: str):
        message = self.message.format(filename)
        print('Дата {0}, Уведомление по почте: {1}'.format(datetime.now(), message))


class LoggingEventListener(EventListener):
    def __init__(self, message=''):
        self.message = message

    def update(self, filename: str):
        message = self.message.format(filename)
        print('Дата {0}, Логирование: {1}'.format(datetime.now(), message))


if __name__ == '__main__':
    editor = Editor('file')
    manager = EventManager()

    message_open = 'Файл {0} был открыт'
    message_close = 'Файл {0} был закрыт'

    editor.event_manager = manager

    open_email_listener = EmailEventListener(message_open)
    editor.event_manager.subscribe('open', LoggingEventListener(message_open))
    editor.event_manager.subscribe('open', open_email_listener)

    editor.event_manager.subscribe('close', LoggingEventListener(message_close))
    editor.event_manager.subscribe('close', EmailEventListener(message_close))

    editor.open()
    sleep(5)
    editor.close()

    editor.event_manager.unsubscribe('open', open_email_listener)
    sleep(5)
    editor.open()
