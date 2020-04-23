from typing import List


class TreeType:
    """
    Класс типов деревьев (класс легковес).

    Легковес хранит общую часть состояния (внутреннее состояние), которая принадлежит нескольким
    реальным бизнес-объектам (контекстам). Легковес принимает оставшуюся часть состояния (внешнее состояние,
    уникальное для каждого объекта) через его параметры метода.
    """

    def __init__(self, name, color, texture):
        self._name = name
        self._color = color
        self._texture = texture

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

    @property
    def texture(self):
        return self.texture()

    def draw(self, x, y, canvas=None):
        print('Отрисовка дерева с координатами ({x},{y}) типа {name}'.format(x=x, y=y, name=self.name))


class TreeTypeFactory:
    """
    Класс фабрики типов деревьев.

    Фабрика Легковесов создает объекты-Легковесы и управляет ими. Она
    обеспечивает правильное разделение легковесов. Когда клиент запрашивает
    легковес, фабрика либо возвращает существующий экземпляр, либо создает
    новый, если он ещё не существует.
    """
    tree_types: List[TreeType] = []

    @classmethod
    def get_tree_type(cls, name, color, texture):
        """
        Возвращает существующий Легковес с заданным состоянием или создает
        новый.
        """
        for tree_type in cls.tree_types:
            if (tree_type.name == name and tree_type.color == color
                    and tree_type.texture == texture):
                return tree_type

            tree_type = TreeType(name, color, texture)
            cls.tree_types.append(tree_type)
            return tree_type


class Tree:
    """
    Класс деревьев (класс контекст)

    Класс Контекстов отделены от Легковесов и хранят свое уникальное для каждого объекта
    состояние (внешнее состояние). Хранит ссылку на объект класса Легковеса.
    """

    def __init__(self, x: int, y: int, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self, canvas=None):
        self.tree_type.draw(self.x, self.y, canvas=canvas)


class Forest:
    """
    Класс леса.

    Клиент данной структуры. Создает или получает объект Легковес и передает его для создания
    объекта Контекста.
    """

    def __init__(self):
        self._trees = []

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeTypeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self._trees.append(tree)

    def draw(self):
        for tree in self._trees:
            tree.draw()
