# -*- coding: utf-8 -*-
"""
условия и циклы
"""

"""1 Ряд - 3
A = int(input("Please, enter number A: "))
B = int(input("Please, enter number B: "))
while A < B*A or A < B or B*A < B:
    print("Please, choose numbers so the following condition will be true be: A > B*A > B")
    A = int(input("Please, enter number A: "))
    B = int(input("Please, enter number B: "))
for i in range(A, B-1, -1):
    if i%2==0:
        continue
    else:
        print(i)
"""

"""2 Факториал
num = int(input("Enter a number: "))  
factorial = 1  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   for i in range(1, num + 1):  
       factorial = factorial*i  
   print("The factorial of", num,"is", factorial)
"""

"""3 Лесенка
print("Remember that n should be equal or lesser than n")
n = int(input("Please, enter n: "))
while n > 9:
    print("Remember that n should be equal or lesser than n")
    n = int(input("Please, enter n: "))
for i in range(1, n+1+1):
    for j in range(1, i):
        print(j, end="")
    print("\n")
"""

"""4 Минимальный делитель
print("Remember that a should be greater than 2")
a = int(input("Please, enter a: "))
while a < 2:
    print("Please, enter a once again!")
    a = int(input("Please, enter a:"))
b = 2
minb = 0
flagb = 0
while b < a:
    temp = a % b
    maxb = b
    if temp == 0:
        if flagb == 0:
            flagb = 1
            minb = b
        elif maxb > minb:
            break
        elif b == a - 1 and minb == 0:
            print("No natural divisor for this number")
    b += 1
if flagb == 1:
    print(minb, "is the lesser natural divisor for", a, "number")
"""

"""
строки
"""

"""1 Делаем срезы
a = input()
print(a[2])
print(a[len(a)-1-1])
print(a[:5])
print(a[:len(a)-2])
print(a[0::2])
print(a[1::2])
print(a[::-1])
print(a[-1::-2])
print(len(a))
"""

"""2 Две половинки
a = input()
print(a[(len(a) + 1) // 2:] + a[:(len(a) + 1) // 2])
"""

"""3 Обращение фрагмента
s = input("Please, enter the word!")
while s.count('h') < 2:
    s = input("Please, enter the word again, it should have 2 'h' symbols")
a = s[:s.find('h')]
b = s[s.find('h'):s.rfind('h') + 1]
c = s[s.rfind('h') + 1:]
s = a + b[::-1] + c
print(s)
"""

"""4 Первое и последнее вхождения
s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))
"""

"""списки"""

"""1 Больше предыдущего
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])
"""

"""2 Соседи одного знака
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break
"""

"""3 Переставить соседние
a = [int(i) for i in input().split()]
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))
"""

"""4 Уникальные элементы
a = [int(s) for s in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')
"""

"""5 Ферзи
n = 8
x = []
y = []
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)

correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False

if correct:
    print('NO')
else:
    print('YES')
"""

"""6 Количество различных чисел
print(len(set(input().split())))
"""

"""7 Количество совпадающих чисел
print(len(set(input().split()) & set(input().split())))
"""

"""8 Пересечение множеств
print(*sorted(set(input().split()) & set(input().split()), key=int))
"""

"""9 Встречалось ли число раньше
numbers = [int(s) for s in input().split()]
occur_before = set()
for num in numbers:
    if num in occur_before:
        print('YES')
    else:
        print('NO')
        occur_before.add(num)
"""


"""10 Количество слов в тексте
words = set()
for _ in range(int(input())):
    words.update(input().split())
print(len(words))
"""


"""11 Номер появления слова
counter = {}
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
"""

"""12 Словарь синонимов
n = int(input())
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])
"""


"""13 Выборы в США
votes = set()
for _ in range(int(input())):
    votes.update(input().split())
print(len(votes))
"""

"""14 Права доступа
"""

"""15 Страны и города
motherland = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        motherland[city] = country
         
for i in range(int(input())):
    print(motherland[input()])
"""

"""16 Частотный Анализ
from collections import Counter
 
words = []
for _ in range(int(input())):
    words.extend(input().split())
 
counter = Counter(words)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print('\n'.join(words))
"""