from abc import ABC, abstractmethod


# Конкретные продукты создаются соответствующими Конкретными Фабриками.

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_click(self, func):
        pass


class WindowButton(Button):
    def render(self):
        print('Кнопка в стиле Windows')

    def on_click(self, func):
        func()
        print('Клик по кнопке в стиле Windows')


class MacOSButton(Button):
    def render(self):
        print('Кнопка в стиле MacOS')

    def on_click(self, func):
        func()
        print('Клик по кнопке в стиле MacOS')


class CheckBox(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_change(self, func):
        pass


class WindowCheckBox(CheckBox):
    def render(self):
        print('Чекбокс в стиле Windows')

    def on_change(self, func):
        func()
        print('Изменен флажок чекбокса в стиле Window')


class MacOSCheckBox(CheckBox):
    def render(self):
        print('Чекбокс в стиле MacOS')

    def on_change(self, func):
        func()
        print('Изменен флажок чекбокса в стиле MacOS')


class GUIFactory(ABC):
    """
    Интерфейс абстрактной фабрики. Объявляет набор методов, которые возвращают
    различные абстрактные продукты (кнопки, чекбоксы, инпуты и т.д). Эти продукты
    называются семейством (семейство Windows, MacOS, Linux и т.д).
    """

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        pass


class WindowGUIFactory(GUIFactory):
    """
    Конкретная Фабрика производит семейство продуктов (кнопки, чекбоксы) одного
    семейства Windows. Стоит обратить внимание, что сигнатуры методов конкретной фабрики
    возвращают абстрактный продукт, в то время как внутри метода создается экземпляр
    освновного продукта.
    """

    def create_button(self) -> Button:
        return WindowButton()

    def create_checkbox(self) -> CheckBox:
        return WindowCheckBox()


class MacOSGUIFactory(GUIFactory):
    """
    Конкретная Фабрика производит семейство продуктов (кнопки, чекбоксы) одного
    семейства MacOS.
    """

    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> CheckBox:
        return MacOSCheckBox()


def client_code(factory: GUIFactory):
    """
    Клиентский код работает с фабриками и продуктами только через абстрактные
    типы: Абстрактная Фабрика и Абстрактный Продукт. Это позволяет передавать
    любой подкласс фабрики или продукта клиентскому коду, не нарушая его.
    """
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.render()
    checkbox.render()
    button.on_click(lambda: print('Клик из клиентского кода!!!'))
    checkbox.on_change(lambda: print('Чекбокс был изменен из клиентского кода!!!'))


if __name__ == '__main__':
    client_code(WindowGUIFactory())
    print('_' * 40)
    client_code(MacOSGUIFactory())
