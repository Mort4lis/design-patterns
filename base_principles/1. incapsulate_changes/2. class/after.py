class Order:
    """
    Класс, содержащий логику вычисления итоговой суммы заказа с учетом налогов.

    Объекты заказов теперь делегируют вычисление налогов
    отдельному классу калькулятору TaxCalculator.
    """

    def __init__(self, items, country, state, city):
        self.items = items or []
        self.country = country
        self.state = state
        self.city = city
        self.tax_calculator = TaxCalculator()

    def get_total(self):
        pass


class TaxCalculator:
    def get_text(self, product, country, state):
        pass

    def _get_us_tax(self):
        pass

    def _get_eu_tax(self):
        pass
