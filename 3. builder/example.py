from abc import ABC, abstractmethod


# "Сложные" продукты, которые порождают классы строителей

class Car:
    def __str__(self):
        return 'Объект автомобиля ready!'


class Manual:
    def __str__(self):
        return 'Объект мануала ready!'


class Builder(ABC):
    """
    Интерфейс строителя.
    Объявляет методы для конструирования различных частей Продуктов.
    """

    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def set_seats(self, number):
        pass

    @abstractmethod
    def set_engine(self, engine):
        pass

    @abstractmethod
    def set_trip_computer(self):
        pass

    @abstractmethod
    def set_gps(self):
        pass


class CarBuilder(Builder):
    """
    Класс конкретного строителя, реализующий интерфейс базового Строителя и предоставляет
    конкретные реализации шагов построения продукта (автомобиля).
    """

    def __init__(self):
        """
        Новый экземпляр строителя должен содержать пустой объект продукта,
        который используется в дальнейшей сборке.
        """
        self._car = None
        self.reset()

    def reset(self):
        self._car = Car()

    @property
    def product(self):
        """
        Конкретные Строители должны предоставить свои собственные методы
        получения результатов. Это связано с тем, что различные типы строителей
        могут создавать совершенно разные продукты с разными интерфейсами.
        Поэтому такие методы не могут быть объявлены в базовом интерфейсе
        Строителя (по крайней мере, в статически типизированном языке
        программирования).

        Как правило, после возвращения конечного результата клиенту, экземпляр
        строителя должен быть готов к началу производства следующего продукта.
        Поэтому обычной практикой является вызов метода сброса в конце тела
        метода getProduct (в нашем случае property product).
        Однако такое поведение не является обязательным, вы
        можете заставить своих строителей ждать явного запроса на сброс из кода
        клиента, прежде чем избавиться от предыдущего результата.
        """
        car = self._car
        self.reset()
        return car

    def set_seats(self, number):
        print('В автомобиль добавлено {0} сидений'.format(number))

    def set_engine(self, engine):
        print('В автомобиль добавлен {0} двигатель'.format(engine))

    def set_trip_computer(self):
        print('В автомобиль добавлен компьютер')

    def set_gps(self):
        print('В автомобиль добавлен GPS-навигатор')


class ManualBuilder(Builder):
    def __init__(self):
        self._manual = None
        self.reset()

    def reset(self):
        self._manual = Manual()

    @property
    def product(self):
        manual = self._manual
        self.reset()
        return manual

    def set_seats(self, number):
        print('В руководство добавлено {0} сидений'.format(number))

    def set_engine(self, engine):
        print('В руководство добавлен {0} двигатель'.format(engine))

    def set_trip_computer(self):
        print('В руководство добавлен компьютер')

    def set_gps(self):
        print('В руководство добавлен GPS-навигатор')


class Director:
    """
    Директор отвечает только за выполнение шагов построения в определённой
    последовательности. Это полезно при производстве продуктов в определённом
    порядке или особой конфигурации. Строго говоря, класс Директор необязателен,
    так как клиент может напрямую управлять строителями.
    """

    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, b: Builder):
        """
       Директор работает с любым экземпляром строителя, который передаётся ему
       клиентским кодом. Таким образом, клиентский код может изменить конечный
       тип вновь собираемого продукта.
       """
        self._builder = b

    def make_sport_car(self):
        self.builder.set_seats(2)
        self.builder.set_engine('спортивный')
        self.builder.set_trip_computer()
        self.builder.set_gps()


if __name__ == '__main__':
    # Клиентский код создаёт объект-строитель, передаёт его директору, а затем
    # инициирует процесс построения. Конечный результат извлекается из объекта-
    # строителя.

    director = Director()
    builder = CarBuilder()
    director.builder = builder

    print('Начато конструирование объекта автомобиля')
    director.make_sport_car()
    print(builder.product)

    print('\n')

    builder = ManualBuilder()
    director.builder = builder

    print('Начато конструирование объекта мануала для автомобиля')
    director.make_sport_car()
    print(builder.product)
