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

####################################################################

# Магический метод __call__. Функторы и классы-декораторы

class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):    # Данный метод позволяет вызывать объекты, по-умолчанию он работает для
        print("__call__")                   # классов, т.е.когда мы пишем c = Counter() срабатывает метод __call__
        self.__counter += step                 # который в свою очередь вызывает методы __new__, __init__
        return self.__counter               # но экземпляр класса так вызвать нельзя c(), после того как прописываем
                                            # в классе __call__ экземпляры становится можно вызывать и такие классы
                                            # называются функторы


c = Counter()
c2 = Counter()              # таким образом можно создвать множество независимых счетчиков
c()
c(10)
c()
c2()
res = c()
res2 = c2()
print(res, res2)

# примеры использования вместо функции прерывания

class StripChars:
    def __init__(self, chars):
        self.__chars = chars
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError("Аргумент должен быть строкой")
        return args[0].strip(self.__chars)

s1 = StripChars("! ")
res = s1("!Hello World !")
print(res)

# пример использования как декоратор

import math

class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


@Derivate
def df_sin(x):
    return math.sin(x)

#df_sin = Derivate(df_sin)      # тут мы делаем df_sin экземпляром класса Derivate и т.к. есть метод __call__
                                # то можно сделать вызов экземпляра, по сути класс Derivate получается декоратором
print(df_sin(math.pi/3))


#################################################################

# Магические методы __str__, __repr__, __len__, __abs__

# __str__ для отображения информации об объекте класса для пользователей
# __repr__  для отображения информации об объекте класса в режиме отладки

class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        return f"{self.name}"

cat = Cat("Васька")
print(cat)

# __len__ позволяет применять функцию len() к экземплярам класса
# __abs__ позволяет применять функцию abs() к экземплярам класса (abs - вычисление модуля)

class Point:
    def __init__(self, * args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))

pt = Point(1, -2 ,4)
print(len(pt))
print(abs(pt))

##########################################################################

# Магические методы __add__, __sub__, __mul__, __truediv__

class Clock:
    __DAY = 86400 # число секунд в сутках

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Должно быть целое число")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть числом")
        sc = other
        if isinstance(sc, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):  # используется когда число слева от экземпляра класса
        return self + other     # в данном месте self вызовет __add__ который выполнит сложение

    def __iadd__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть числом")
        sc = other
        if isinstance(sc, Clock):
            sc = other.seconds
        self.seconds += sc
        return self

    @classmethod
    def __verify_operand(cls, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть числом")
        sc = other
        if isinstance(sc, Clock):
            sc = other.seconds
        return sc

    def __sub__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть числом")
        sc = other
        if isinstance(sc, Clock):
            sc = other.seconds
            return Clock(self.seconds - sc)
        elif isinstance(sc, int):
            return Clock(-(sc + self.seconds))

    def __rsub__(self, other):          # в уроке такого не было подобрал сам, т.к. other - self не работает
        return self - -(other)

    def __isub__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть числом")
        sc = other
        if isinstance(sc, Clock):
            sc = other.seconds
        self.seconds -= sc
        return self

    def __mul__(self, other):
        sc = self.__verify_operand(other)
        return Clock(self.seconds * sc)

    def __rmul__(self, other):
        return self * other

    def __floordiv__(self, other):           # __truediv__ не получится т.к. по условию д.б. целое число секунд
        sc = self.__verify_operand(other)
        return Clock(self.seconds // sc)

    ########################################

    # Методы сравнений __eq__, __ne__, __lt__, __gt__ и другие

    def __eq__(self, other):                # c1 == c2 если сравнивать 2 экземпляра класса без данного метода то
        sc = self.__verify_operand(other)     # сравниваться будут ячейки памяти в которых хранятся эти объекты,
        return self.seconds == sc           # а не сами значения этих экземпляров

    # def __ne__(self, other):    можно обойтись без него, когда итерпрет видит != то пытается выполнить not(c1 == c2)

    def __lt__(self, other):
        sc = self.__verify_operand(other)
        return self.seconds < sc

    # def __gt__(self, other):  можно обойтись без него, если есть __lt__, итерпрет просто поменяет операнды местами
    # аналогично с __le__ и __ge__ работает также

c1 = Clock(2000)
c2 = Clock(100)
c4 = Clock(10000)
c5 = c1 + c2 + c4
c2 -= 200
print(c2.get_time())
print(c5.get_time())
c6 = 3000 - c1
print(c6.get_time())
c7 = c4 // 2000
print(c7.get_time())
print(10000 == c4)

##########################################################################
# Магические методы __eq__ и __hash__

# в питоне есть функция хэш которая вычисляет определенное значение для неизменяемых объектов, если повторно вычислять
# хэш одного и того же объекта, то он всегда будет один и тот же.

# в словаре в качестве ключа хранится кортеж из хэша и названия ключа, сначала значение ищется по хэшу, если есть
# одинакавые хэши то уже сравнивается по значению ключа.

# экземпляры пользовательских классов считаются неизменяемыми объектами, поэтому у 2-х экземпляров с одинаковыми
# параметрами будут разные хэши


# Ограничения:
# если a == b(равны), то и их хэши будут равны
# если hash(a) == hash(b) не гарантирует равенство объектов
# если hash(a) != hash(b) то объекты точно не равны

class PointHash:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y)) # т.е. мы поменяли вычисление хэша от объекта класса на вычисление хэша от
                                      # кортежа координат. Делаем это только в том случае если надо воспринимать
                                      # как одинаковые
pt1 = PointHash(1, 2)
pt2 = PointHash(1, 2)
print(hash(pt1), hash(pt2))  # если pt1 == pt2 выдает false, то функция hash считает что объекты разные,
# но если перегружен метод __eq__, то функция hash считает объекты не хэшируемыми, т.к. нарушен алгоритм работы hash
# чтобы поправить это нужен метод __hash__

d = {}
d[pt1] = 1
d[pt2] = 2
print(d.items()) # если у нас переопределена __hash__ как показано выше, то при добавлении объектов в словарь, они
                # будут восприниматься как один объект и d[pt2] = 2 перезапишет d[pt1] = 1


##################################################################

# Магический метод __bool__ __len__

# Со стандартными типами данных функция bool работает следующим образом: для пустых значаний и цифры 0 будет False
# для остальных True

# Для экземпляров класса всегда возвращает True, но можно переопредить либо __bool__ либо __len__, т.к. если __bool__
# не переопредела то она вызывает метод __len__

class PointBool:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return self.x * self.x + self.y * self.y

pt3 = PointBool(2, 3)
print(bool(pt3))  # вернет True, т.к. возвращает True от любого ненулевого числа


################################################################

# Магические методы __getitem__, __setitem__ и __delitem__

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __getitem__(self, item): # позволяет через выражение s[2] напрямую обратиться к элементу списка
        if 0 <= item < len(self.marks):
            return self.marks[item]  # если использовать свой метод, то получится выражение s.method_name(2)
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key, value):
        if not isinstance(key, int) and key < 0:
            raise TypeError("Индекс должен быть целым не отрицательным")
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)
        self.marks[key] = value   # !!!!!! set ничего не возвращает return не нужен !!!!!

    def __delitem__(self, key):
        if not isinstance(key, int) and key < 0:
            raise TypeError("Индекс должен быть целым не отрицательным")
        del self.marks[key]

s = Student('Сергей', [5,5,3,2,4])
s[10] = 3
print(s.marks)
del s[6]
print(s.marks)

#####################################################################

# Магические методы __iter__ и __next__

# Итератор это объект у которого есть метод __next__. Без метода __iter__ можно пройти по элементам с помощью функции
# next, но нельзя использовать объект в цикле т.к. будет ошибка что объект не итерируемый

class FRange:
    def __init__(self, start = 0.0, stop = 0.0, step = 1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __iter__(self):  # получение итератора для перебора объекта
        self.value = self.start - self.step
        return self

    def __next__(self):  # переход к следующему элементу и его считывание
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

fr = FRange(0, 2, 0.5)
print(next(fr))
print(fr.__next__())
print(fr.__next__())
print(fr.__next__())
for i in fr:
    print(i)

class FRange2D:
    def __init__(self, start = 0.0, stop = 0.0, step = 1.0, rows = 5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0  # self.value может быть объявлено как тут так и в __init__ разницу не увидел
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return  iter(self.fr)
        else:
            raise StopIteration

fr2 = FRange2D(0, 2, 0.5, 5)
for row in fr2:
    for x in row:
        print(x, end=" ")
    print()

#################################################################

# Наследование

class Geom:
    def __init__(self, name):
        self.name = name

    def set_coords(self, x1, y1, x2, y2):  # если этот метод вызван из экземпляра дочернего класса, то self ссылается
        self.x1 = x1                       # на этот экземпляр дочернего класса.
        self.x2 = x2           # т.к. self базового класса может ссылаться не только на объекты этого класса, но и на
        self.y1 = y1           # объекты дочерних классов, все зависит от того откуда был вызван метод
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print("Рисование линии")

class Rect(Geom):
    def draw(self):
        print("Рисование прямоугольника")


l = Line('line')
l.set_coords(1, 1, 2, 2)
print(l.name)
r = Rect('rect')
r.set_coords(1, 1, 2, 2)

print(issubclass(Line, Geom))          #  можно проверить является ли Line подклассом Geom
# print(issubclass(l, Geom))           # но нельзя проверить экземпляр Line, хотя конечно прописать l.__class__
                                       # но наверно это не совсем коректно и нужно все же использовать isinstance

# Все классы наследуются от базового класса object. Так и стандартные типы данных тоже являются классами и их
# можно переопределять

class Vector(list):
    # pass                   # если не переопределять метод __str__ то будет выводиться как обычный список

    def __str__(self):
        return ' '.join(map(str, self))  # тут map нужна только потому что ниже список цифр, а их join не сможет
                                         # соединить в строку и поэтому переводим их в str
print(Vector([1, 2, 3]))
v = Vector([1, 2, 3])
print(type(v))            # тип будет не List, а Vector

#######################################################################

# Наследование. Функция super() и делегирование

class Geom:
    def __init__(self, x1, y1, x2, y2):
        print(f"инициализатор {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2



class Line(Geom):
    pass

class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):  # если переопределен метод в дочернем классе, то он не будет
        super().__init__(x1, y1, x2, y2)         # вызываться в базовом, и если мы хотим инициализировать координаты
        self.fill = fill                    # указанные в базовом нужно самостоятельно вызывать метод баз класса
                                            # super возвращает ссылку на посредник через который происходит вызов
                                            # методов базовых классов
# !!! Обязательно super() должна вызываться раньше дополнительных атрибутов дочернего класса, т.к. если в базовом
# классе окажется такой же атрибут, то он может быть перезаписан.

# Когда в дочернем классе вызывается функция super() с методом базового класса это называется делегирование
l = Line(0, 0, 1, 2)
r = Rect(0, 0, 10, 20)

# При создании экземпляра класса Line вызывается метод __call__ он вызывается из Метакласса
# он в свою очередь вызывает метод __new__ для создания экземпляра и метод __init__ для его инициализации. Эти методы
# ищутся в соответствующем классе Line, и если не находятся то по цепочке в базовых классах. __init__ берется из Geom
# __new__ берется из object
#

    # def __call__(self, *args, **kwargs):
    #     obj = self.__new__(self, *args, **kwargs)
    #     self.__init__(obj, *args, **kwargs)
    #     return obj
