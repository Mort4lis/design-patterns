from abc import ABC, abstractmethod


class Dialog(ABC):
    """
    Абстрактный класс дилога (Посредник).

    Интерфейс Посредника опредяет метод, используемый компонентами для уведомления
    посредника о различных событиях. Посредник может реагировать на эти события и передавать
    исполнение другим компонентам.
    """

    @abstractmethod
    def notify(self, component: 'Component', event: str):
        """
        Метод уведомления посредника о произошедшем событии.

        В параметрах этого метода можно передавать детали события: ссылку на компонент, в котором
        оно произошло и любые другие данные.
        """
        pass


class Component:
    """
    Базовый интерфейс компонента.

    Содержит ссылку на объект-посредника (диалога). Работает с ним только
    через абстрактный интерфейс Посредника. Благодаря этому компоненты можно
    повторно использовать в другой программе, связав их с посредником другого типа.

    Компненты не должны общаться напрямую друг с другом. Если в компоненте происходит важное
    событие, он должен оповестить об этом своего посредника. А тот в свою очередь самостоятельно
    передаст вызов другим компонентам, если это потребуется.
    """

    def __init__(self, dialog: Dialog):
        self._dialog = dialog

    @property
    def dialog(self):
        return self._dialog

    def click(self):
        self.dialog.notify(self, 'click')

    def keypress(self):
        self.dialog.notify(self, 'keypress')


"""
Классы конкретных компонентов.

Наследуют поведение базового класса.
"""


class Button(Component):
    pass


class Input(Component):
    pass


class AuthenticationDialog(Dialog):
    """
    Диалог аутентификации (Конкретный посредник).

    Конкретный посредник содержит код взаимодействия нескольких компонентов между собой.
    Объект этого класса создает и хранит ссылки на конкретные компоненты системы.
    """

    def __init__(self):
        self.login_input = Input(self)
        self.password_input = Input(self)
        self.submit_btn = Button(self)

    def notify(self, component: Component, event: str):
        if isinstance(component, Button) and event == 'click':
            print('Попытка пользователя аутентифицироваться!')

        # Другая логика ...


if __name__ == '__main__':
    form = AuthenticationDialog()
    form.submit_btn.click()
