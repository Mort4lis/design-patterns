# Реализация одиночки на основе декоратора.


import functools


def singleton(cls):
    instance = None

    @functools.wraps(cls)
    def inner(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance

    return inner


@singleton
class Entity:
    pass


if __name__ == '__main__':
    obj1 = Entity()
    obj2 = Entity()

    print(id(obj1) == id(obj2))
