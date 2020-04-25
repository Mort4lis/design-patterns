from abc import ABC, abstractmethod
from typing import List


class Visitor(ABC):
    """
    Интерфейс Посетителя.

    Описывает общий интерфейс для всех типов посетителей. Он объявляет набор методов, которые
    принимают различные классы компонентов в качестве параметров. В языках, поддерживающих
    перегрузку методов (Java, C#), эти методы могут иметь одинаковые имена, но типы их
    параметров должны отличаться.
    """

    @abstractmethod
    def visit_dot(self, instance: 'Dot'):
        pass

    @abstractmethod
    def visit_circle(self, instance: 'Circle'):
        pass

    @abstractmethod
    def visit_rectangle(self, instance: 'Rectangle'):
        pass


class XMLExportVisitor(Visitor):
    """
    Посетитель экспорта в XML (Конкретные Посетители).

    Реализует какое-то особенное поведение для всех типов компонентов, которые
    можно подать через методы интерфейса Посетителя.
    """

    def visit_dot(self, instance: 'Dot'):
        print('Экспорт в XML точки')

    def visit_circle(self, instance: 'Circle'):
        print('Экспорт в XML круга')

    def visit_rectangle(self, instance: 'Rectangle'):
        print('Экспорт в XML треугольника')


class Shape(ABC):
    """
    Интерфейс Фигур (Интерфейс Компонента).

    Объявляет метод accept (метод принятия Посетителя),
    который в качестве аргумента принимает любой объект,
    реализующий интерфейс Посетителя.
    """

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def accept(self, v: Visitor):
        pass


"""
Конкретные компоненты.

Реализуют методы принятия посетителя. Цель этого метода - 
вызвать нужный метод посещения, который соответствует типу этого
компонента. Так Посетитель узнает, с каким именно компонентом он работает.
"""


class Dot(Shape):
    def draw(self):
        print('Рендеринг точки...')

    def accept(self, v: Visitor):
        v.visit_dot(self)


class Circle(Shape):
    def draw(self):
        print('Рендеринг круга...')

    def accept(self, v: Visitor):
        v.visit_circle(self)


class Rectangle(Shape):
    def draw(self):
        print('Рендеринг треугольника...')

    def accept(self, v: Visitor):
        v.visit_rectangle(self)


def client_code(components: List[Shape], visitor: Visitor):
    """
   Клиентский код может выполнять операции посетителя над любым набором
   элементов, не выясняя их конкретных классов. Операция принятия направляет
   вызов к соответствующей операции в объекте посетителя.
   """
    for component in components:
        component.accept(visitor)


if __name__ == '__main__':
    shapes = [Dot(), Rectangle(), Circle()]
    client_code(shapes, XMLExportVisitor())
