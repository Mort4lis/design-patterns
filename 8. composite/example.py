from abc import ABC, abstractmethod
from copy import deepcopy
from typing import List


class OrderComponent(ABC):
    """
    Базовый класс Компонент.

    Объявляет общие операции (в данном случае - свойство получении цены)
    как для простых, так и для сложных структур данных
    """

    @property
    @abstractmethod
    def price(self):
        pass


class Phone(OrderComponent):
    """
    Класс телефона.

    Простой компонент (листовой элемент). Не имеет вложенных компонентов.
    """

    @property
    def price(self):
        return 149.90


class Headphones(OrderComponent):
    """Класс наушников."""

    @property
    def price(self):
        return 59.99


class BoxContainer(OrderComponent):
    """
    Класс коробки.

    Является сложным компонентом, т.к содержит ссылки на дочерние компоненты (как простые, так и сложные).
    Обычно объекты контейнера делегируют фактическую работу своим детям, а затем суммируют результат.
    """

    def __init__(self):
        self._children: List[OrderComponent] = []

    """
    Объект контейнера может как добавлять компоненты в свой список вложенных
    компонентов, так и удалять их, как простые, так и сложные.
    """

    def add(self, element: OrderComponent):
        self._children.append(element)

    def remove(self, element: OrderComponent):
        self._children.remove(element)

    @property
    def children(self):
        return deepcopy(self._children)

    @property
    def price(self):
        """
        Контейнер выполняет свою основную логику особым образом. Он проходит
        рекурсивно через всех своих детей, собирая и суммируя их результаты.
        Поскольку потомки контейнера передают эти вызовы своим потомкам и так
        далее, в результате обходится всё дерево объектов.
        """
        total = 0
        for child in self._children:
            total += child.price
        return total


def client_code(component: OrderComponent):
    """
    Клиентский код работает со всеми компонентами через базовый интерфейс.
    """
    print('Order price is', component.price)


if __name__ == '__main__':
    box1 = BoxContainer()
    box1.add(Phone())
    box1.add(Phone())

    box2 = BoxContainer()
    box2.add(Headphones())
    box2.add(Phone())

    box1.add(box2)

    box1.add(Phone())
    client_code(box1)
    client_code(Headphones())
    client_code(box2)
