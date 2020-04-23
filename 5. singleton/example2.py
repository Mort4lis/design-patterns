# Реализация одиночки на основе мета-классов (более предпочительный метод)


class SingletonMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Entity(metaclass=SingletonMeta):
    pass


obj1 = Entity()
obj2 = Entity()

print(id(obj1) == id(obj2))
