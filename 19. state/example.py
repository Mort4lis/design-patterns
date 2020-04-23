from abc import ABC, abstractmethod


class State(ABC):
    """
    Интерфейс Состояния.

    Определяет методы, которые должны реализовать Конкретные Состояния, а также
    предоставляет обратную ссылку на объект-Контекст, связанный с Состоянием. Эта
    обратная ссылка может использоваться, для того, чтобы изменить состояние Контекста.
    """

    def __init__(self, document: 'Document'):
        self._document = document

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def publish(self):
        pass


class Document:
    """
    Класс Контекста.

    Хранит ссылку на объект Состояния и делегирует ему работу, зависящую от внутреннего состояния.
    Контекст работает с Состоянием через общий интерфейс, за счет этого, можно подменять (изменять)
    объекты состояний прямо во время выполнения программы. Контекст должен иметь метод для присваивания
    ему нового состояния.
    """

    def __init__(self):
        self._state = Draft(self)

    def change_state(self, state: State):
        self._state = state

    def render(self):
        return self._state.render()

    def publish(self):
        self._state.publish()


"""
Классы конкретных состояний.

Реализуют поведения, связанные с определенным состоянием контекста.
Состояние может иметь обратную ссылку на объект контекста. Через нее
не только удобно получать из контекста нужную информацию, но и осуществлять 
смену его состояния.
"""


class Draft(State):
    def render(self):
        return 'Вывод документа в состоянии Черновик'

    def publish(self):
        self._document.change_state(Moderation(self._document))


class Moderation(State):
    def render(self):
        return 'Вывод документа в состоянии На Модарации'

    def publish(self):
        self._document.change_state(Published(self._document))


class Published(State):
    def render(self):
        return 'Вывод документа в состоянии Опубликовано'

    def publish(self):
        print('The document has already published')


if __name__ == '__main__':
    doc = Document()

    print(doc.render())
    doc.publish()
    print(doc.render())
