# Проблему можно решить, если применять паттерн Стратегия.
#
# Для этого нужно выделить способы доставки в собственные классы
# с общим интерфейсом
#
# Теперь при добавлении нового способа доставки нужно будет реализовать
# новый класс интерфейса доставки, не трогая класса заказов


class Order:
    def __init__(self, items: list, shipping: 'ShippingType'):
        self.shipping = shipping
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
        return self.shipping.get_cost(self)


class ShippingType:
    def get_cost(self, order: Order):
        raise NotImplementedError


class Ground(ShippingType):
    def get_cost(self, order: Order):
        # Бесплатно для больших заказов
        if order.get_total() > 100:
            return 0

        # 1.5$ за 1 кг, но не меньше 10$
        return max(10, order.get_total_weight() * 1.5)


class Air(ShippingType):
    def get_cost(self, order: Order):
        # 3$ за 1 кг, но не меньше 20$
        return max(20, order.get_total_weight() * 3)
