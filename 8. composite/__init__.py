# Компоновщик (Composite) - структурный паттерн проектирования, который позволяет
# сгруппировать объекты в древовидную структуру, а затем работать с ней так, если
# бы это был единичный объект.
#
# Паттерн может быть применен если присутствует древовидная архитекутура.
# Паттерн Компоновщик включает в себя классы:
# 1. Компонент - определяет общий интерфейс для простых и состовных компонентов дерева.
# 2. Лист - простой компонент дерева, не имеющий ветвелений.
# 3. Контейнер (или composite) - это составной элемент дерева, который содержит набор
# дочерних компонентов, но ничего не знает об их типах. Но это не является проблемой, т.к
# все дочерние элементы следуют общему интерфейсу Компонента.
# 4. Клиент - работает с деревом через общий интерфейс компонентов. (в результате ему неважно
# как элемент перед ним находится - составной или простой.
#
# Применимость:
# 1. Когда нужно представить древовидную структуру объектов.
# 2. Когда клиенты должны единообразно трактовать простые и составные объекты.
#
# Плюсы:
# 1. Упрощает архитектуру клиента при работе со сложным деревом компонентов.
# 2. Облегчает добавление новых видов компонентов.
#
# Минусы:
# 1. Создает слишком общих дизайн классов.
