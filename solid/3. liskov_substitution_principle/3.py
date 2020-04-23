# Метод подкласса не должен ужесточать пред условия


class Calculator:
    def add(self, a, b):
        return a + b


class PositiveCalculator(Calculator):
    def add(self, a, b):
        # Ужесточение пред условий!!!
        if a > 0 and b > 0:
            return super().add(a, b)
        return 0


def client_code(calculator: Calculator):
    print(calculator.add(-5, 10))


# Базовый клиентский код
client_code(Calculator())

# Код сломается, т.к класс PositiveCalculator ужесточил пред условие
# Раньше базовый класс отличного работал с отрицательными числами, а теперь нет
client_code(PositiveCalculator())
