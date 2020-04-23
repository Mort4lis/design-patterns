def get_order_total(order):
    """
    Метод рассчитывает финальную сумму заказа с учетом налогов.

    Теперь логика вычисления налогов вынесена в отдельный метод `get_tax_amount`.
    Метод `get_order_total_after` ничего не знает о реализации метода
    подсчета налогов, следовательно, мы можем менять логику вычисления налогов, не
    затрагивая основной метод вычисления стоимости заказа.
    """
    total = 0
    for item in order.items:
        total += item.price * item.quantity

    total -= total * get_tax_amount(order.country)

    return total


def get_tax_amount(country):
    """Метод посчета налогов."""
    if country == 'US':
        return 0.07
    elif country == 'EU':
        return 0.2
