list_words = ["programming", "gramm", "prograstination"]

# def common_char(list_words):
#     if isinstance(list_words, list) and all([type(word) == str for word in list_words]):
#         symbol = ''
#         variants = []
#         for char in list_words[0]:
#             if any([len(symbol) == len(word) for word in list_words[1:]]):
#                 return symbol
#             if all([symbol+char in word for word in list_words[1:]]):
#                 symbol += char
#             elif symbol != '':
#                 variants.append(symbol)
#                 symbol = ''
#         if variants:
#             return max(variants, key=len)
#         if symbol == '':
#             return 'нет одинаковых букв'
#         else:
#             return symbol
#     return 'не список слов'

# assert common_char(["programming", "wsu", "prograstination"]) == 'нет одинаковых букв'
# assert common_char(["programming", 1, "prograstination"]) == 'не список слов'
# assert common_char(["programming", "gramm", "prograstination"]) == 'gra'
# assert common_char(["programming", "gra", "prograstination"]) == 'gra'

def common_char_in_start(strs) -> str:
    result = []
    for items in zip(*strs):
        if len(set(items)) == 1:
            result.append(items[0])
        else:
            break

    return "".join(result)


assert common_char_in_start(["programming", "product", "prograstination"]) == 'pro'


def anagramSolution(s1,s2):
    c1 = [0]*26     # количество букв в алфавите
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    print(c1)
    #  [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

import timeit

print(anagramSolution('apple','pleap'))
t1 = timeit.Timer("anagramSolution('appledfg','pldfgeap')", "from __main__ import anagramSolution")
#print("time ", t1.timeit(number=1000), "milliseconds")  # запускается 1000 раз, по умолчанию 1млн


def two_sum(nums, target):
    sum = {}
    for i, num in enumerate(nums):
        num2 = target - num
        if num2 in sum:
            return [sum[num2], i]
        sum[num] = i
    return 'нет подходящих слогаемых'

print(two_sum([3,5,3,17], 6))


# Input: l1 = [2,4,3], l2 = [5,6,4]
l3 = [7,0,8]
l3.reverse()
print(l3)
# Explanation: 342 + 465 = 807.

def addTwoNumbers(l1, l2):  # нужно переделывать через связные списки
    l1.reverse()
    l2.reverse()
    sum = int(''.join(map(str, l1))) + int(''.join(map(str, l2)))
    l3 = list(str(sum))
    l3.reverse()
    return l3

print(addTwoNumbers([0], [0]))

def isPalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False

print(isPalindrome(-121))


def romanToInt(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    s_list = list(s)
    s_list.reverse()
    sum = 0
    for i, r in enumerate(s_list):
        if i < len(s_list) - 1 and roman[r] <= roman[s_list[i+1]]:
            sum += roman[r]
            continue
        elif i < len(s_list) - 1 and roman[r] >= roman[s_list[i+1]]:
            sum += roman[r] - roman[s_list[i+1]]*2
            continue
        sum += roman[r]
    return sum

print(romanToInt('XIV'))


def romanToIntLeed(s):
    convertedInt = 0
    romanHashmap = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    prevChar = None
    for i in range(0, len(s)):
        currChar = s[i]
        if (i > 0) and (romanHashmap[currChar] > romanHashmap[prevChar]):
            convertedInt = convertedInt - 2 * romanHashmap[prevChar] + romanHashmap[currChar]
        else:
            convertedInt += romanHashmap[currChar]
        prevChar = currChar
    return convertedInt

print(romanToIntLeed('CM'))



seq = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]

def binary_search(seq, item):
    first = 0
    last = len(seq) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if seq[midpoint] == item:
            found = True
        else:
            if seq[midpoint] > item:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

print(binary_search(seq, 5))


def bubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum -= 1

#alist = [54,26,93,17,77,31,44,55,20]
alist = [1,4,3,4,6,7]
bubbleSort(alist)
print('bubbleSort')
print(alist)

alist = [54,26,93,17,77,31,44,55,20]

def selectionSort(alist: list):
    for passnum in range(len(alist)-1,0,-1):
        position_max = 0
        for i in range(1, passnum+1):
            if alist[i] > alist[position_max]:
                position_max = i
        temp = alist[passnum]
        alist[passnum] = alist[position_max]
        alist[position_max] = temp

selectionSort(alist)
print('selectionSort')
print(alist)

alist = [54,26,93,17,77,31,44,55,20]

def insertionSort(alist):
    for passnum in range(1, len(alist)):
        for i in range(passnum):
            if alist[i] > alist[passnum]:
                alist.insert(i, alist[passnum])
                alist.pop(passnum+1)

insertionSort(alist)
print('insertionSort')
print(alist)

alist = [54,26,93,17,77,31,44,55,20]

def insertionSort2(alist):
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index
     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1
     alist[position]=currentvalue

insertionSort2(alist)
print('insertionSort2')
print(alist)

alist = [54,26,93,17,77,31,44,55,20]
t1 = timeit.Timer("bubbleSort(alist)", "from __main__ import bubbleSort, alist")
print("time bubbleSort ", t1.timeit(number=1000), "milliseconds")

alist = [54,26,93,17,77,31,44,55,20]
t1 = timeit.Timer("selectionSort(alist)", "from __main__ import selectionSort, alist")
print("time selectionSort ", t1.timeit(number=1000), "milliseconds")

alist = [54,26,93,17,77,31,44,55,20]
t1 = timeit.Timer("insertionSort(alist)", "from __main__ import insertionSort, alist")
print("time insertionSort ", t1.timeit(number=1000), "milliseconds")
alist = [54,26,93,17,77,31,44,55,20]
t1 = timeit.Timer("insertionSort2(alist)", "from __main__ import insertionSort2, alist")
print("time insertionSort2 ", t1.timeit(number=1000), "milliseconds")


alist = [1,2,3,4,5]

def summ(alist: list) -> int:
    if len(alist) == 1:
        return alist[0]
    return alist[0] + summ(alist[1:])

print(summ(alist))

def factorial(num: int) -> int:
    if num == 1:
        return 1
    return num * factorial(num-1)

print(factorial(6))


def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(3,2))


def decorator(func):
    def wrapper():
        return 'dec ' + func()
    return wrapper

@decorator
def sum_default():
    return 'a+b'

print(sum_default())
print(sum_default.__name__)

#######

from functools import wraps

def decorator_with_wraps(func):
    @wraps(func)
    def wrapper():
        return 'dec ' + func()
    return wrapper

@decorator_with_wraps
def sum_default():
    return 'a+b'

print(sum_default())
print(sum_default.__name__)

########

def decorator_with_args_func(func):
    def wrapper(*args):
        return 'dec ' + str(func(*args))
    return wrapper

@decorator_with_args_func
def sum_with_args(*args):
    return sum(args)

print(sum_with_args(2,4,6))

#############

def decorator_with_arg_for_wrapper(dec_arg1, dec_arg2):
    def decorator(func):
        def wraper(func_arg1, func_arg2):
            return f'{dec_arg1} + {dec_arg2} = ' + str(func(func_arg1, func_arg2))
        return wraper
    return decorator

@decorator_with_arg_for_wrapper('a', 'b')
def summ(arg1, arg2):
    return arg1 + arg2


print(summ(3,6))

#############

def generator(arg):
    for i in range(arg):
        yield i

gen = generator(5)
print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(f'cycle {i}')

nums_squared_gc = (num**2 for num in range(5))
print(nums_squared_gc)

#############

class Fibo:
    def __init__(self):
        self.a = 0
        self.b = 1
        self.next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.next < 10:
            temp = self.a + self.b
            self.a = self.b
            self.b = temp
            self.next += 1
            return self.b
        raise StopIteration

fibo = Fibo()
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(list(fibo))

for i in Fibo():
    print(i)

fibo = Fibo()
print(fibo)

######################

# моя версия суммы 3 чисел в списке

def sum3arr(arr: list, target: int) -> int:
    counter = 0
    summer = {}
    result_index = set()
    for first_index, first_value in enumerate(arr):
        for next_index, next_value in enumerate(arr):
            if next_index <= first_index:
                pass
            else:
                sum12 = target - next_value
                for k, v in summer.items():
                    if v == sum12 and int(k[0]) < int(k[1]) < next_index and k+str(next_index) not in result_index:
                        counter += 1
                        result_index.add(k+str(next_index))
                        print(k+str(next_index))
                summer[str(first_index) + str(next_index)] = first_value + next_value
                print(summer)
    return counter

arr = [1,1,2,2,3,3,4,4,5,5]
target = 8

print(sum3arr(arr, target))

def lengthOfLongestSubstring(s: str) -> int:
    max_counter = 0
    counter = 0
    chars = []
    for index, char in enumerate(s):
        if char in s[index+1:]:
            chars.append(char)
            counter +=1
            while counter > 0:
                chars.append(s[index+counter])
                if ''.join(chars) in s[index+1:]:
                    counter += 1
                else:
                    if counter > max_counter:
                        max_counter = counter
                    counter = 0
                    chars = []
    return max_counter


print(lengthOfLongestSubstring('bbbbb'))

#####################################

# Варианты вызова функции вида any_sum(5)(100)(-10)()

def any_sum_with_if(number):
    result = number
    def wrapper(number2=None):
        nonlocal result
        if number2 is None:
            return result
        result += number2
        return wrapper
    return wrapper

def any_sum_with_try(number):
    result = number
    def wrapper(number2=None):
        nonlocal result
        try:
            int(number2)
        except TypeError:
            return result
        result += number2
        return wrapper
    return wrapper


def any_sum_with_atr_wrapper(number):
    def wrapper(number2=None):
        if number2 is None:
            return wrapper.result
        wrapper.result += number2
        return wrapper
    wrapper.result = number  # т.к. фун-я это объект можно создать ее атрибут. Для wrapper можно wrapper.<атрибут>
    return wrapper


def any_sum_with_logic_dict(number):
    def wrapper(number2=None):
        def inner():
            wrapper.result += number2
            return wrapper
        logic = {
            type(None): lambda: wrapper.result,
            int: inner
        }
        return logic[type(number2)]()
    wrapper.result = number
    return wrapper

# lambda - анонимная функция которая может принимать аргументы и возвращать результат вычисления в одну строку
# lambda: 3*2 - возвращает объект класса функции и вызвать не получится, чтобы ее вызвать нужно присвоить ее переменной
# x = lambda: 3*2 - и вызывать через переменную x() или с аргументами x = lambda a,b: a*b ... x(a,b)
# по тому же принципу можно делать и с обычными функциями назначать переменной без (), потом переменную вызывать с ()
# map и lambda
# L = [1, 2, 3, 4]
# list(map(lambda x: x**2, L))
# filter и lambda
# print(list(filter(lambda x: x % 2 == 0, [1, 3, 2, 5, 20, 21])))


class any_sum_without_inherit:
    def __init__(self, number):
        self._number = number

    def __call__(self, value=0):
        return any_sum(self._number + value)

    def __str__(self):
        return str(self._number)


class any_sum(int):
    def __call__(self, value=0):
        print(f'{self} {value}')
        return any_sum(self + value)

print(any_sum(5)())
print(any_sum(5)(2)())
print(any_sum(5)(100)(-10)())