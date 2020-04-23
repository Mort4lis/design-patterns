from abc import ABC, abstractmethod


class Notificator(ABC):
    """
    Абстрактный класс оповещений.

    Базовый интерфейс Компонента определяет поведение, которое изменяется декораторами.
    """

    @abstractmethod
    def send(self, message=''):
        pass


class EmailNotificator(Notificator):
    """
    Класс опововещений по электронной почте.

    Класс конкретного компонента. Предоставляет реализацию поведения по умолчанию.
    """

    def send(self, message=''):
        print('Отправлено сообщение с тексом "{0}" по почте'.format(message))


class BaseNotifyDecorator(Notificator):
    """
    Базовый класс декоратора оповещений.

    Базовый класс Декоратора следует тому же интерфейсу, что и другие компоненты. Основная
    цель данного класса - определить интерфейс обертки всех конкретных декораторов. Содержит
    ссылку на оборачиваемый компонент. Реализация по умолчанию может включать себя делегирование
    всей работы обернутому компоненту.
    """

    def __init__(self, component: Notificator):
        self._component = component

    @property
    def component(self):
        return self._component

    def send(self, message=''):
        """Декоратор делегирует всю работу обёрнутому компоненту."""
        self.component.send(message)


class SMSNotificator(BaseNotifyDecorator):
    """
    Конкретные Декораторы вызывают обёрнутый объект и изменяют его результат
    некоторым образом.
    """

    def send(self, message=''):
        """
        Декораторы могут вызывать родительскую реализацию операции, вместо того,
        чтобы вызвать обёрнутый объект напрямую. Такой подход упрощает
        расширение классов декораторов.
        """
        super().send(message)
        print('Отправлено сообщение с тексом "{0}" по SMS'.format(message))


class FacebookNotificator(BaseNotifyDecorator):
    def send(self, message=''):
        super().send(message)
        print('Отправлено сообщение с тексом "{0}" на Facebook'.format(message))


class SlackNotificator(BaseNotifyDecorator):
    def send(self, message=''):
        super().send(message)
        print('Отправлено сообщение с тексом "{0}" на Slack'.format(message))


def client_code(notificator: Notificator):
    """
    Клиентский код работает со всеми объектами, используя интерфейс Компонента.
    Таким образом, он остаётся независимым от конкретных классов компонентов, с
    которыми работает.
    """
    notificator.send('Hello, world!')


if __name__ == '__main__':
    n1 = EmailNotificator()
    n2 = SMSNotificator(n1)

    # Отправить сообщение по эл. почте и SMS
    client_code(n2)

    print('-' * 75)

    # Отправить сообщение по эл. почте, SMS и Facebook
    n3 = FacebookNotificator(n2)
    client_code(n3)
