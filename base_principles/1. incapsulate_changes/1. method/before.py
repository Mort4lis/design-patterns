def get_order_total(order):
    """
    Метод рассчитывает финальную сумму заказа с учетом налогов.

    Логика вычисления налогов вшита в реализацию метода. Мы можем предположить,
    что эта логика вычисления налогов будет часто меняться, т.к она зависит от страны,
    штата, и даже города. К тому же размер налога не постоянен - власти могут менять его,
    когда вздумается.
    """
    total = 0
    for item in order.items:
        total += item.price * item.quantity

    # Вычисление налогов
    if order.country == 'US':
        total -= total * 0.07
    elif order.country == 'EU':
        total -= total * 0.2

    return total
