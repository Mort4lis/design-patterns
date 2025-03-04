# Команда (Command) - это поведенческий паттерн проектирования, который превращает
# запросы в объекты, позволяя передавать их как аргументы при вызове методов, ставить
# запросы в очередь, логировать их, а также поддерживать отмену операций.
#
# По сути, паттерн Команда - является прослойкой между отправителем и получателем. В качестве
# отправителя может быть GUI с кнопками, при клики которых выполняются команды, которые в свою
# очередь делегируют их выполнение Получателям (бизнес-логике).
#
# Применимость:
# 1. Когда вы хотите параметризовать объекты выполняемым действием.
#
# Команды превращает операции в объекты. А объекты можно передавать, хранить
# и взаимозаменять внутри других объектов.
#
# 2. Когда вы хотите ставить операции в очередь, выполнять их по расписанию или
# передавать по сети.
#
# 3. Когда вам нужна операция отмены.
#
# Плюсы:
# 1. Убирает прямую зависимость между объектами, вызывающие операции и
# объектами, которые их непостредственно выполняют.
# 2. Позволяет реализовать простую отмену и повтор операций.
# 3. Позволяет реализовать отложенный запуск команд.
# 4. Позволяет собирать сложные команды из простых.
# 5. Реализует open/close principle
#
# Минусы:
# 1. Усложняет код программы за счет дополнительных классов.
