class PC:
    def __init__(self, memory:str = '16GB', disk:str = '1Tb', model:str = 'Xeon', cpu:str = 'Intel'):
        print("создание класса pc")
        self.memory = memory
        self.disk = disk
        self.model = model
        self.cpu = cpu

    def __str__(self):
        return f'{self.memory} {self.disk} {self.model} {self.cpu}'


class Dimensions:
    def __init__(self, length:int = 10, width:int = 10, heigth:int = 10):
        self.length = length
        self.width = width
        self.heigth = heigth

    def __str__(self):
        return f'{self.length}x{self.width}x{self.heigth}'


class Desktop(PC, Dimensions):
    def __init__(self, hardware:PC, keyboard_dimensions:Dimensions, monitor_dimensions:Dimensions, mouse_dimensions:Dimensions):
        print("создание класса настольных pc")
        self.hardware = hardware
        self.monitor_dimensions = monitor_dimensions
        self.keyboard_dimensions = keyboard_dimensions
        self.mouse_dimensions = mouse_dimensions

    def characteristics(self):
        return print(f"Габариты монитора {self.monitor_dimensions}, Габариты клавиатуры {self.keyboard_dimensions},\
Габариты мышки {self.mouse_dimensions}, {self.hardware}")


class Laptop(PC, Dimensions):
    def __init__(self, hardware:PC, dimentions_laptop:Dimensions, diagonal:int = 15):
        print("создание класса ноутов")
        self.hardware = hardware
        self.dimentions_laptop = dimentions_laptop
        self.diagonal = diagonal

    def characteristics(self):
        return print(self.diagonal, self.dimentions_laptop, self.hardware)

pc1 = Desktop(PC('8GB', '500Mb', 'Xeon', 'Intel'), Dimensions(30,10,2), Dimensions(30,20,5), Dimensions(10,7,4))
pc1.characteristics()
pc2 = Laptop(PC('4GB', '250Mb', 'Lenovo', 'AMD'), Dimensions(50,30, 5), 15)
pc2.characteristics()

#####################################################################
class Animal:
    def get_class_name(self):
        return self.__class__

class Fox(Animal):

    def say(self):
        return 'wee-wee'

class Bird(Animal):
    def say(self):
        return 'chik-cirik'

class Cat(Animal):
    def say(self):
        return 'myau-myau'

class Dog(Animal):
    def say(self):
        return 'gav-gav'

animals = (Fox(), Bird(), Cat(), Dog())
for i in animals:
    print(f"The {''.join([y.__name__ for y in i.__class__.__bases__])} {i.__class__.__name__} says {i.say()}")


####################################################################

# Режимы доступа public, private, protected. Сеттеры и геттеры

class Point():
    def __init__(self, x=0, y=0, z=0):
        self._x = self._y = self._z = 0
        if self.__value_check(x) and self.__value_check(y) and self.__value_check(z):
            self._x = x
            self._y = y
            self.__z = z

    def __str__(self):
        return f"{self._x}, {self._y}, {self.__z}"

    @classmethod                        # метод класса не имеет связи экземплярами, т.к. нет параметра self
    def __value_check(cls, x):
        return type(x) in (int, float)  # такая форма записи в результате функции возвращает True если выражение True
                                        # иначе False

    def set_coord(self, z):
        if self.__value_check(z):
            self.__z = z
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coord(self):
        return self._x, self._y, self.__z

pt  = Point(1, 2, 3)
pt._x = 3   # режим protected только предостерегает пользователя от использования этого атрибута вне класса, но никак
            # не ограничивает. Подчеркивание только указывает что это внутренняя служебная переменная.
#pt.__z = 3  # это не сработает, режим private позволяет обращаться к таким переменным только внутри класса, для того
            # чтобы поменять такую переменную можно создать метод внутри класса(сеттер) и уже из экземпляра вызывать
            # этот метод
            # Конечно можно поменять эту переменную через атрибут _Point__z, но так делать не рекомендуется.

# Функционал геттеров и сеттеров для обращения к защищенным переменным и сами защищенный переменные нужны для
# соблюдения принципа инкапсуляции ООП, т.е чтобы оставить открытым для пользователя только необходимый функционал
# как руль, педали и т.д. в авто.
print(pt)
pt.set_coord(5)
print(pt)
print(pt.get_coord())

################################################################################

# Магические методы __setattr__, __getattribute__, __getattr__ и __delattr__

class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def change_max_coord(self, new_max):  # при желании измененить атрибут класса MAX_COORD нельзя взять и присвоить
        self.MAX_COORD = new_max          # новое значение через self т.к. self ссылается на экземпляр и при операторе
                                          # присваивания создастся или измениться атрибут экземпляра, а не класса.

    @classmethod
    def correct_change_max_coord(cls, new_max):  # Измененить атрибут класса MAX_COORD можно таким образом
        cls.MAX_COORD = new_max

    def __getattribute__(self, item):         # при обращении к атрибуту экземляра/класса всегда вызывается этот метод
        print("__getattribute__")             # и можно его перегрузить например для запрета обращения к конкретному
        if item == "x":                       # атрибуту
            raise ValueError("Обращение запрещено")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):        # вызывается каждый раз при установке нового значения
        print("__setattr__")                  # можно пользоваться как object так и self.__dict__[key], но предпочтит.
        if key == "z":                        # object
            raise ValueError("Недопустимое имя атрибута")
        return object.__setattr__(self, key, value)
        #return self.__dict__[key] = value

    def __getattr__(self, item):              # вызывается когд атрибута нет, если не хотим чтобы возникала ошибка
        return False                          # Attribute_error можно возвращать например False



pt = Point(1, 2)
print(pt.MAX_COORD)
pt.correct_change_max_coord(200)
print(Point.MAX_COORD)
print(pt.MAX_COORD)
print(pt.y)
pt.y = 10

###############################################################################

# Паттерн "Моносостояние". Позволяет создать множество экземпляров класса с одинаковыми атрибутами, при этом, если
# добавлять у конкретного экземпляра новый атрибут, то он появится и во всех других экземплярах.


class ThreadData:
    __shared_attrs = {
        'id': 1,
        'name': 'thread_1',
        'data': {}
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


###################################################################################

# Свойство property - более удобный способ работы с приватными атрибутами

from string import ascii_letters

class Person:
    def __init__(self, name, old):
        self.verify_name(name)

        self.__name = name
        #self.__old = old           # если используется property с сеттером old, то эту строку можно заменить на нижнюю
        self.old = old              # т.к. она не создает в экземпляре приватный атрибут, а вызывает сеттер old
                                    # который уже в свою очередь создает в экземпляре приватный атрибут __old


    def get_name(self):             # если будет еще больше атрибутов, то будет еще больше методов, что неудобно
        return self.__name          # запоминать,
                                    #
    def set_name(self, name):       #
        self.__name = name          #


    def get_old(self):              # вместо этого можно воспользоваться свойством property и объединить
        return self.__old           # геттер и сеттер для каждого атрибута в один метод

    def set_old(self, old):         #
        self.__old = old            #

    old = property(get_old, set_old)


    @property                       # вместо предыдущего варианта можно изменить запись property в виде декоратора
    def old(self):                  #
        return self.__old           #

    @old.setter
    def old(self, old):             #
        self.__old = old            #


    @classmethod
    def verify_name(cls, name):
        letters = ascii_letters
        if len(name.strip(letters)) != 0:       # strip удаляет из name все перечисленные символы в letters
            raise TypeError("Неверные символы")

p = Person('John', 20)
p.old = 40                # при таком обращении, когда в классе есть property old, то приоритет у него и
                          # будет меняться атрибут класса __old, а не создаваться/меняться атрибут экземпляра
                          # если в классе нет property old, то созастся локальный атрибут экземпляра old
print(p.old)
print(p.__dict__)

#################################################################

# Дескрипторы (data descriptor и non-data descriptor)

# Дескриптор это класс содержащий методы __get__, __set__, __del__. А non-data descriptor содержит только get
# При этом data descriptor имеет приоритет над локальными атрибутами экземпляра, т.е. если будет дескриптор xr и
# локальный атрибут xr в экземпляре, то при обращении pt.xr будет выводиться значение дескриптора
# а при использовании non-data descriptor если делаем pt.xr = 5 создастся локальный атрибут xr и потом при pt.xr
# будет выводиться именно он

class NonData:
    def __set_name__(self, owner, name):
        self.name = "_x"                    # это дескриптор не данных который будет читать атрибут _х

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

class Integer:

    @classmethod
    def verify_coord(cls, value):
        if type(value) != int:
            raise TypeError("Координата должна быть числом")

    def __set_name__(self, owner, name):    # self - ссылка на атрибут "х" класса Point3D(экземпляр класса Integer),
        self.name = "_" + name              # owner - это ссылка на сам класс Point3D,
                                            # name - это название атрибута "х"


    def __get__(self, instance, owner):         # self - ссылка на атрибут "х" класса Point3D(экземпляр класса Integer)
        # return instance.__dict__[self.name]     # instance - ссылка на экземпляр pt класса Point3D, из которого вызван
                                                # owner - это ссылка на сам класс Point3D
        return getattr(instance, self.name)     # второй вариант вместо return instance.__dict__[self.name]

    def __set__(self, instance, value):         # self - ссылка на атрибут "х" класса Point3D(экземпляр класса Integer)
        print(f"__set__:{self.name}={value}")   # instance - это ссылка на экземпляр pt класса Point3D, из которого вызван
        self.verify_coord(value)
        # instance.__dict__[self.name]=value      # value - это значение которое присваивается
        setattr(instance, self.name, value)     # второй вариант вместо instance.__dict__[self.name]=value


class Point3D:
    x = Integer()                   # При объявлении атрибута "x" как дескриптор Integer срабатывает метод
    y = Integer()                   # def __set_name__
    z = Integer()
    xr = NonData()

    def __init__(self, x, y, z):
        self.x = x                  # В инициализаторе в момент присваивания срабатывает метод __set__
        self.y = y
        self.z = z

pt = Point3D(1,2,3)                 # При создании экземпляра класса Point3D вызывается инициализатор
print(pt.x)                            # При запросе атрибута выполняется метод __get__
print(pt.xr, pt.__dict__)

# В классе Point3D объевляем атрибут "x" как дескриптор Integer. При объявлении атрибута срабатывает метод класа



















