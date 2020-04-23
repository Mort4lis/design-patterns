from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    """
    Интерфейс Стратегий.

    Определяет метод, общий для всех вариаций алгоритма. Контекст использует
    этот интерфейс для вызова алгоритма.

    Для Контекста не важно, какая именно вариация алгоритма будет выбрана, т.к
    все они имеют одинаковый интерфейс.
    """

    @abstractmethod
    def build_route(self, a: int, b: int):
        pass


class Navigator:
    """
    Класс навигатора (Контекст).

    Контекст хранит ссылку на объект конкретной Стратегии, работая с этим
    объектом через общий интерфейс стратегий.
    """

    def __init__(self, strategy: RouteStrategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, value: RouteStrategy):
        self._strategy = value

    def build_route(self, a: int, b: int):
        self.strategy.build_route(a, b)


"""
Конкретные стратегии реализуют различные вариации алгоритма.
"""


class RoadStrategy(RouteStrategy):
    def build_route(self, a: int, b: int):
        print('Строит путь от А к Б по дороге')


class WalkingStrategy(RouteStrategy):
    def build_route(self, a: int, b: int):
        print('Строит путь от А к Б пешком')


class PublicTransportStrategy(RouteStrategy):
    def build_route(self, a: int, b: int):
        print('Строит путь от А к Б общественным транспортом')


if __name__ == '__main__':
    """
    Обычно, клиент должен создать объект конкретной стратегии и передать его в
    контекст: либо через конструктор, либо в какой-то другой решающий момент, используя сеттер.
    Благодаря этому, контекст не знает о том, какая именно стратегия сейчас выбрана.
    """
    nav = Navigator(RoadStrategy())
    nav.build_route(5, 10)

    nav.strategy = WalkingStrategy()
    nav.build_route(5, 10)

    nav.strategy = PublicTransportStrategy()
    nav.build_route(5, 10)
