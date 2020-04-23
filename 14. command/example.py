from abc import ABC, abstractmethod


class Command(ABC):
    """
    Описывает общий интерфейс Команды.

    Обычно здесь описан всего один метод для запуска команды.
    """

    @abstractmethod
    def execute(self):
        pass


class SimpleCommand(Command):
    """
    Простая команда.

    Некоторые команды способны выполнять простые операции самостоятельно.
    """

    def __init__(self, payload: str):
        self._payload = payload

    def execute(self):
        print('Выполнение простой команды: "{0}"'.format(self._payload))


class ComplexCommand(Command):
    """
    Составная команда.

    Есть команды, которые делегируют более сложные операции другим объектам,
    называемые "получатели" (receivers). Параметры, с которыми команда обращается
    к получателю, следует хранить в виде полей. В большинстве случаев, объекты команд
    можно сделать неизменяемым, предавая в них все необходимые параметры только через конструктор.
    """

    def __init__(self, receiver: 'Receiver', params: list):
        self._receiver = receiver
        self._params = params

    def execute(self):
        print('Выполнение сложной команды, делегирующая свое выполнение объекту-получателю (бизнес-логике)')
        self._receiver.operation(self._params)


class Invoker:
    """
    Класс Отправителя.

    Содержит ссылку на объект команды и обращается к нему, когда нужно выполнить
    какое-то действие. Отправитель работает с Командами только через их общий интерфейс.
    Он не знает, какую конкретно команду использует, т.к получает готовый объект команды
    от клиента.
    """

    def __init__(self):
        self._command = None

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, value: Command):
        self._command = value

    def do_something(self):
        if self.command is not None:
            self.command.execute()


class Receiver:
    """
    Класс Получателя.

    Содержит некую важную бизнес-логику. Он умеет выполнять все виды операций,
    связанных с выполнением запроса. Фактически, любой класс может выступать
    Получателем.
    """

    def operation(self, params):
        print('Вызов объекта получателя с параметрами {0}'.format(params))


def client_code(invoker: Invoker):
    invoker.do_something()


if __name__ == '__main__':
    app = Invoker()
    backend = Receiver()

    app.command = SimpleCommand('Hello, world!')
    client_code(app)

    print('-' * 75)

    app.command = ComplexCommand(backend, ['params1', 'params2', 'params3'])
    client_code(app)
