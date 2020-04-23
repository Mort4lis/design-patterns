import re
from abc import ABC, abstractmethod
from random import random
from typing import List


class Editor:
    """
    Класс текстового редактора (объект бизнес логики)

    Реализует выборку текста, вырезку текста и подмену.
    """

    def __init__(self, text: str) -> None:
        self.text = text

    def select_text(self) -> str:
        words = re.split(r'\s+', self.text)
        end = int(1 + random() * len(words))  # [1, 69]
        return ' '.join(words[0:end])

    def cut_text(self, selected: str) -> None:
        self.text = self.text.replace(selected, '', 1)

    def replace_text(self, selected: str, text: str) -> None:
        self.text = self.text.replace(selected, text, 1)


class Button:
    def __init__(self, callback):
        self.callback = callback

    def click(self):
        self.callback()


class Command(ABC):
    """
    Общий интерфейс команды.

    Определяет абстрактный метод execute, которые обязаны реализовать конкретные команды.
    Имеет метод сохранения текстового состояния редактора, отмены команды.
    """

    def __init__(self, app: 'Application', editor: Editor):
        self._app = app
        self._editor = editor
        self._backup = None

    @property
    def app(self):
        return self._app

    @property
    def editor(self):
        return self._editor

    @abstractmethod
    def execute(self) -> bool:
        """
        Абстрактный метод выполнения команды.

        Возвращает True если состояние редактора изменилось
        в результате выполнения команды, иначе - False

        :return: Булево значения, определяющее изменение состояния редактора.
        """
        pass

    def do_backup(self):
        self._backup = self.editor.text

    def undo(self):
        if self._backup is not None:
            self.editor.text = self._backup


class CopyCommand(Command):
    """Команда, которая сохраняет в буфер обмена выбранный редактором текст."""

    def execute(self) -> bool:
        """
        Метод выполнения команды копирования.

        Возвращает False, т.к состояние текстового редактора в результате выполнения этой
        операции никогда не меняется.

        :return:
        """
        self.app.clipboard = self.editor.select_text()
        return False


class PasteCommand(Command):
    """Команда, которая вставляет тест из буфера обмена в редактор."""

    def execute(self) -> bool:
        """
        Метод выполнения команды вставки.

        В случае, если в буфере обмена есть текст -> вернет True, т.к тест из этого буфера будет вставлен
        в текстовой редактор, а значит изменится состояние текстового редактора. В противном случае - False.

        :return:
        """
        clipboard = self.app.clipboard
        if clipboard is not None:
            self.do_backup()
            selected_text = self.editor.select_text()
            self.editor.replace_text(selected_text, clipboard)
            return True
        return False


class CutCommand(Command):
    """Команда, которая вырезает выбранный текст и сохраняет его в буфер обмена."""

    def execute(self):
        """
        Метод выполнения команды вырезки.

        Возвращает True при любом раскладе, т.к по результату выполнения этой команды
        всегда меняется состояние.

        :return:
        """
        text = self.editor.select_text()
        self.do_backup()
        self.editor.cut_text(text)
        self.app.clipboard = text
        return True


class Application:
    """
    Класс приложения (клиентский код).
    """

    def __init__(self, editor: Editor):
        self._editor = editor
        self._clipboard = None
        self.history: List[Command] = []

    @property
    def clipboard(self):
        return self._clipboard

    @clipboard.setter
    def clipboard(self, value: str):
        self._clipboard = value

    @property
    def editor(self):
        return self._editor

    def run(self):
        def callback(command: Command):
            def command_executer():
                if command.execute():
                    self.history.append(command)

            return command_executer

        copy_button = Button(callback(CopyCommand(self, self.editor)))
        cut_button = Button(callback(CutCommand(self, self.editor)))
        paste_button = Button(callback(PasteCommand(self, self.editor)))

        copy_button.click()
        paste_button.click()
        cut_button.click()
        cut_button.click()

    def undo(self):
        for command in reversed(self.history):
            self.history.pop()
            command.undo()


if __name__ == '__main__':
    with open('file') as file:
        text = file.read()
        editor = Editor(text)

    application = Application(editor)
    application.run()
    application.undo()

    print(editor.text == text)
