# -*- coding: utf-8 -*-

""" Базовый синтаксис"""

""" № 1
def triangle(a, b, c):
    a = int(input("Please, input First triangle side"))
    b = int(input("Please, input Second triangle side"))
    c = int(input("Please, input Third triangle side"))
    while a < 0 or b < 0 or c < 0:
        print("One of numbers you entered is lesser than 0")
        a = int(input("Please, input First triangle side"))
        b = int(input("Please, input Second triangle side"))
        c = int(input("Please, input Third triangle side"))
    if a + b > c and a + c > b and b + c > a:
        if a+b+c==a+c or a+b+c==a+b or a+b+c == b+c:
            print("This is a vyrozhdenniy triangle")
        else:
            print("This is a triangle.")
    else:
        print("This is not a triangle")
 
triangle(a, b, c)
"""

""" № 2 Длина отрезка
from math import sqrt
 
def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
 
x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
print(distance(x1, x2, y1, y2))
"""

""" № 3
def number_to_words(n):
    f = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    o = {10: 'десять', 20: 'двадцать', 30: 'тридцать', 40: 'сорок',
         50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
         80: 'восемьдесят', 90: 'девяносто'}
    s = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
         14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
         17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
    n1 = n % 10
    n2 = n - n1
    if n < 10:
        return f.get(n)
    elif 10 < n < 20:
        return s.get(n)
    elif n >= 10 and n in o:
        return o.get(n)
    else:
        return o.get(n2) + ' ' + f.get(n1)
print(number_to_words(int(input())))
"""

""" №4 Отрицательная степень
def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res
 
print(power(float(input()), int(input())))
"""


""" №5 Палиндром
def palindrome(data):
    data = data.replace(' ','').lower()
    return 'Палиндром' if data == data[::-1] else 'Не палиндром'
"""

""" Области видимости """


""" №6 
ok = ['']

i = 1
def print_without_duplicates(message):
  ok.append(message)
  global i
  if ok[i] != ok[i-1]:
    print(message)
  i += 1
  return i

print_without_duplicates("HELLO")
print_without_duplicates("HELLO")
print_without_duplicates("hello")
print_without_duplicates("hello")
print_without_duplicates("Hello hello hello")
print_without_duplicates("HELLO")
print_without_duplicates("HELLO")
"""


""" №7
def add_friends(name, friend):
    if name in dict_friend:
        dict_friend[name] = dict_friend[name] + friend
    else:
        dict_friend[name] = friend
 
 
def are_friends(name1, name2):
    return name2 in dict_friend[name1]
 
 
def print_friends(name):
    print(*sorted(dict_friend[name]))
 
 
dict_friend = {}
"""


"""Работа с аргументами"""


""" №8
def mirror(arr):
    mirrored_part = arr[::-1]  
    arr += mirrored_part  
"""

""" №9
In [1]: def from_string_to_list(string, container):
   ...:     container.extend(map(int, string.split()))
   ...:
 
In [2]: a = [1, 2, 3]
   ...: from_string_to_list("1 3 99 52", a)
   ...: print(*a)
1 2 3 1 3 99 52
 
In [3]: a = [77, 'abc']
    ...: from_string_to_list("", a)
    ...: print(*a)
77 abc
"""



""" №10
def transpose(matrix):
    return[list(x) for x in zip(*matrix)]
 
matrix = [[1,2,3], [4,5,6], [7,8,9]]
 
print(transpose(matrix))
"""


"""Переменное число аргументов"""


""" №11
def matrix(n = None, m = None, a = 0):
    if not n:
        return [a]
    elif not m:
        m = n
    return [[a for _ in range(m)] for _ in range(n)]
 
rows = matrix(2)
for row in rows:
    print(*row)
"""


""" №12
def partialSums(*args):
    sums = [0]
    for i,x in enumerate(args):
            sums.append(x + sums[i])
    return sums
 
print(partialSums(1, 1/2, 1/4, 1/8, 1/16, 1/32))
"""


"""Рекурсия"""


""" №13
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
 
print(power(float(input()), int(input())))
"""



""" №14
def recursive_len(some_list):
    if not some_list:
        return 0
    return 1 + recursive_len(some_list[:-1])
"""

""" №15
def reverse():
    x = int(input())
    if x != 0:
        reverse()
    print(x)
 
reverse()
"""


""" №16
def linear(some_list):
    if not some_list:
        return some_list
    if type(some_list[0]) is list:
        return linear(some_list[0]) + linear(some_list[1:])
    return some_list[:1] + linear(some_list[1:])
"""

""" №17
arr = [0, 1, 2, 3, 5, 4, 1, 4, 5, 6, 7, 15, 24, 27, 36, 1020]
c = [_ for _ in arr if _ < 5]
print(c)
t = list(filter(lambda _: _ < 5, arr))
print(t)
"""

""" №18
arr = [1, 2, 3, 4, 5, 6, 8, 10, 11, 15, 43, 86, 1020, 99991]
print([_ / 2 for _ in arr])
print(list(map(lambda _: _/2,arr)))
"""

""" №19
print(sum(map(lambda _: _**2, filter(lambda _: not _%9, range(10,1000)))))
"""