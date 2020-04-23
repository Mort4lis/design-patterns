from abc import abstractmethod


class Device:
    """
    Интерфейс устройств (реализация)

    Все устройства имеют общий интерфейс, поэтому с ними может работать любой пульт.

    На практике оба интерфейса (и абстракции, и реализации) могут быть разными. Как правило
    Реализация предоставляет только примитивные операции, в то время как Абстракция определяет
    операции более высокого уровня, основанные на этих примитивных операций Реализации.
    """

    @abstractmethod
    def is_enabled(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @property
    @abstractmethod
    def volume(self):
        pass

    @volume.setter
    @abstractmethod
    def volume(self, percent):
        pass

    @property
    @abstractmethod
    def channel(self):
        pass

    @channel.setter
    @abstractmethod
    def channel(self, channel):
        pass


class TV(Device):
    """Класс телевизора (конкретная реализация)."""

    def is_enabled(self):
        pass

    def enable(self):
        pass

    def disable(self):
        pass

    @property
    def volume(self):
        return 0

    @volume.setter
    def volume(self, percent):
        pass

    @property
    def channel(self):
        return 0

    @channel.setter
    def channel(self, channel):
        pass


class Radio(Device):
    """Класс радио (конкретная реализация)."""

    def is_enabled(self):
        pass

    def enable(self):
        pass

    def disable(self):
        pass

    @property
    def volume(self):
        return 0

    @volume.setter
    def volume(self, percent):
        pass

    @property
    def channel(self):
        return 0

    @channel.setter
    def channel(self, channel):
        pass


class Remote:
    """
    Класс пультов (Абстракция).

    Устанавливает ссылку на устройство, которым управляет. Методы этого класса
    делегируют свою работу методам связанного устройства.
    """

    def __init__(self, device: Device):
        self._device = device

    def toggle_power(self):
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()

    def volume_up(self):
        self._device.volume += 10

    def volume_down(self):
        self._device.volume -= 10

    def channel_up(self):
        self._device.channel += 1

    def channel_down(self):
        self._device.channel -= 1


class AdvancedRemote(Remote):
    """
    Расширенный класс пультов.

    Расширяет абстракцию (пульты) без изменений реализации (устройства).
    """

    def mute(self):
        self._device.volume = 0


def client_code(obj: Remote):
    """
    За исключением этапа инициализации, когда объект Абстракции связывается с
    определённым объектом Реализации, клиентский код должен зависеть только от
    класса Абстракции. Таким образом, клиентский код может поддерживать любую
    комбинацию абстракции и реализации.
    """
    obj.toggle_power()
    obj.volume_up()
    obj.volume_up()


if __name__ == '__main__':
    """
    Клиентский код должен работать с любой предварительно сконфигурированной
    комбинацией абстракции и реализации.
    """
    remote = Remote(TV())
    client_code(remote)

    remote_other = AdvancedRemote(Radio())
    client_code(remote)
