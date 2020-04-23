# Данный класс нарушает принцип открытости / закрытости,
# т.к способы доставки (по суше, по воздуху) вшиты в метод
# подсчета стоимости доставки. И если мы добавим новый способ доставки
# (например, по воде), то нам придется трогать весь класс


class Order:
    def __init__(self, items, shipping_type='ground'):
        self.shipping_type = shipping_type
        self.items = items or []

    def get_total(self):
        """Подсчет стоимости товаров."""
        total = 0
        for item in self.items:
            total += item.price * item.quantity

        # tax here...

        return total

    def get_total_weight(self):
        """Суммарный вес заказа."""
        return sum([item.weight for item in self.items])

    def get_shipping_cost(self):
        """Подсчет стоимости доставки."""
        if self.shipping_type == 'ground':
            # Бесплатно для больших заказов
            if self.get_total() > 100:
                return 0

            # 1.5$ за 1 кг, но не меньше 10$
            return max(10, self.get_total_weight() * 1.5)

        if self.shipping_type == 'air':
            # 3$ за 1 кг, но не меньше 20$
            return max(20, self.get_total_weight() * 3)
