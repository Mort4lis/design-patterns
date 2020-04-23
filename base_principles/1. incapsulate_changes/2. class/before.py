class Order:
    """Класс, содержащий логику вычисления итоговой суммы заказа с учетом налогов."""

    def __init__(self, items, country, state, city):
        self.items = items or []
        self.country = country
        self.state = state
        self.city = city

    def get_total(self):
        pass

    def tax_amount(self):
        pass
