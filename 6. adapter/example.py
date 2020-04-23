import math


class RoundPeg:
    """
    Класс круглого колышка.

    Целевой класс. Клиентский код завязан на этом интерфейсе
    """

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius


class SquarePeg:
    """
    Класс квадратного колышка.

    Адаптируемый класс. Класс, который не совместим с клиентским кодом
    (разные интерфейсы)
    """

    def __init__(self, width):
        self._width = width

    @property
    def width(self):
        return self._width


class RoundHole:
    """
    Класс дыры.

    Ассоциация с классом круглого колышка. Т.к через круглую дыру может пройти
    только колышко с крыглым отверстием.
    """

    def __init__(self, radius):
        self.radius = radius

    def fits(self, other: RoundPeg):
        return self.radius >= other.radius


class SquarePegAdapter(RoundPeg):
    """
    Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
    интерфейсом.
    """

    def __init__(self, wrapper: SquarePeg):
        super().__init__(None)
        self.wrapper = wrapper

    @property
    def radius(self):
        half_width = self.wrapper.width / 2
        square_half_width = half_width ** 2
        return math.sqrt(square_half_width * 2)


def client_code(peg: RoundPeg):
    """Клиентский код, который работает с колышком круглой формы."""
    hole = RoundHole(5)
    print('Fits', hole.fits(peg))


if __name__ == '__main__':
    peg_original = RoundPeg(5)
    peg_adapter = SquarePegAdapter(SquarePeg(5))

    client_code(peg_original)
    client_code(peg_adapter)
