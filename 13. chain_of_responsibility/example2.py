from abc import ABC, abstractmethod
from typing import List


class HelpfulTextHandler(ABC):
    """Интерфейс обработчиков, определяющий единственный метод показа подсказки."""

    @abstractmethod
    def show_helpful_text(self):
        pass


class Component(HelpfulTextHandler):
    """
    Базовый класс всех компонентов (как простых, так и составных).

    Содержит базовое поведение показа подсказки. В случае, если она есть - вывести ее в консоль,
    иначе - передать вывод подсказки контейнеру.

    Контейнер - составной объект, который может содержать внутри себя как простые компоненты, так
    и подобные ему (составные).
    """

    def __init__(self, *, helpful_text=None):
        self._container = None
        self.helpful_text = helpful_text

    @property
    def container(self):
        return self._container

    @container.setter
    def container(self, value: 'Container'):
        self._container = value

    def show_helpful_text(self):
        if self.helpful_text is not None:
            print('Вывод подсказки: "{0}"'.format(self.helpful_text))
        elif self.container is not None:
            self.container.show_helpful_text()


class Button(Component):
    """
    Класс конкретного простого компонента Кнопки.

    Он полностью наследует свое поведение от базового класса.
    """
    pass


class Container(Component):
    """
    Базовый класс компонентов-контейнеров.

    Полностью наследует поведение базового класса Компонента. Также реализует метод
    добавления потомков в свою коллекцию.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.children: List[Component] = []

    def add(self, element: Component):
        self.children.append(element)
        element.container = self


class Dialog(Container):
    """Классы конкретных Компонентов-контейнеров."""
    pass


class Panel(Container):
    pass


def click_element(element: HelpfulTextHandler):
    """
    Клиентский код, который кликает по компоненту.

    Клиенту можно подсунуть абсолютно любой компонент (не обязательно первый в цепочке).
    """
    element.show_helpful_text()


if __name__ == '__main__':
    dialog = Dialog(helpful_text='Клик на диалог приложения')

    panel1 = Panel(helpful_text='Клик на панель 1')
    panel2 = Panel(helpful_text='Клик на панель 2')

    btn1 = Button(helpful_text='Клик на кнопку 1')
    btn2 = Button(helpful_text='Клик на кнопку 2')

    panel1.add(btn1)
    panel1.add(btn2)
    dialog.add(panel1)
    dialog.add(panel2)

    click_element(btn1)
