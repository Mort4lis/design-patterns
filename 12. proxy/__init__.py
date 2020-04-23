# Заместитель (Proxy) - это структурный паттерн проектирования, который позволяет
# подставлять вместо реальных объектов специальные объекты-заменители. Эти объекты
# перехватывают вызовы к оригинальному объекту, позволяя сделать что-то до или после
# передачи вызова оригиналу.
#
# Применимость:
# 1. Ленивая инициализация (виртуальный прокси). Когда у вас есть тяжелый объект, грузящий
# данные из файловой системы или базы данных.
#
# Вместо того, чтобы при старте программы создавать "тяжелый" объект, можно сэкономить ресурсы
# поручив создание этого объекта тогда, когда он действительно нужен объекту-заместителю
#
# 2. Защита доступа (защищающий прокси). Перед вызовом оригинального сервиса можно проверить
# различные условия (проверка доступа, и т.д.)
#
# 3. Локальный запуск сервиса (удаленный прокси). Когда настоящий сервисный объект находится
# на удаленном сервере.
#
# В этом случае, заместитель транслирует запросы клиента в вызовы по сети, в протоколе, понятному
# удаленному сервису.
#
# 4. Логирование запросов (логирующий прокси). Когда требуется хранить историю обращений к сервисному
# объекту.
#
# 5. Кэширование. Когда нужно кэшировать результаты запросов клиентов и управлять их жизненным циклом.
#
# Плюсы:
# 1. Позволяет контролировать сервисный объект незаметно для клиента
# 2. Может работать, даже если сервисный объект еще не создан (ленивая инициализация)
# 3. Может контролировать жизненный цикл служебного объекта
#
# Минусы:
# 1. Усложняет программу за счет дополнительных классов.
# 2. Увеличивает время отклика от сервиса.
