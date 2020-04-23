# Предпочитайте композицию вместо наследования

# Проблемы, возникающие при наследовании:
#
# 1. Подкласс не может отказаться от интерфейса или реализации родителя.
# Вы должны будете реализовать все абстрактные методы родителя, даже
# если они не нужны для конкретного подкласса.
#
# 2. Переопределяя методы родителя, нужно заботиться о том, чтобы
# не сломать поведение базового класса.
#
# 3. Любое изменение в родителе может сломать поведение в подклассах.
#
# 4. Повторное использование кода через наследование может привести
# к разрастанию иерархии классов.
#
# У наследования есть альтернатива - композиция. Если наследование можно
# выразить словом "является" (автомобиль является транспортом), то композицию
# словом "содержит" (автомобиль содержит двигатель)
#
# Агрегация - более свободный вид композиции, где два объекта являются
# равноправными и ни один из них не управляет жизненным циклом другого.
# (например, автомобиль содержит человека, но тот может выйти из автомобиля
# и пойти пешком)
