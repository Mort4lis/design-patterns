from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    """
    Интерфейс обработчиков.

    Чаще всего содержит один метод обработки, но также может содержать setter -
    установки следующего обработчика (для построения цепочки).
    """

    @abstractmethod
    def handle(self):
        pass


class BaseHandler(Handler):
    """
    Базовый обработчик (опциональный класс).

    Реализует поведение по умолчанию
    (позволяет избавиться от дублирующего кода в конкретных обработчиках).
    Имеет поле, которое содержит ссылку на объект следующего обработчика. Клиент связывает
    обработчики в цепь, через setter, определенный здесь. Здесь можно реализовать и метод обработки,
    который бы перенаправлял запрос следующему объекту, проверив его наличие.
    """

    def __init__(self):
        self._next: Optional[Handler] = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value: Handler):
        self._next = value

    def handle(self):
        if self.next is not None:
            self.next.handle()


class ConcreteHandlerA(BaseHandler):
    """
    Класс конкретного обработчика.

    Все Конкретные Обработчики могут либо обрабатать запрос, либо передать его
    следующему обработчику в цепочке.
    """

    def handle(self):
        print('Обработчик А')
        super().handle()


class ConcreteHandlerB(BaseHandler):
    def handle(self):
        print('Обработчик В')
        super().handle()


class ConcreteHandlerC(BaseHandler):
    def handle(self):
        print('Обработчик C')
        super().handle()


def create_first_chain() -> Handler:
    elem1 = ConcreteHandlerA()
    elem2 = ConcreteHandlerB()
    elem3 = ConcreteHandlerC()

    elem1.next = elem2
    elem2.next = elem3

    return elem1


def create_second_chain() -> Handler:
    elem1 = ConcreteHandlerA()
    elem2 = ConcreteHandlerB()
    elem3 = ConcreteHandlerC()

    elem2.next = elem1
    elem1.next = elem3

    return elem2


def client_code(chain: Handler):
    """
    Обычно клиентский код приспособлен для работы с единственным обработчиком. В
    большинстве случаев клиенту даже неизвестно, что этот обработчик является
    частью цепочки.
    """
    chain.handle()


if __name__ == '__main__':
    chain1 = create_first_chain()
    chain2 = create_second_chain()
    client_code(chain1)
    client_code(chain2)
