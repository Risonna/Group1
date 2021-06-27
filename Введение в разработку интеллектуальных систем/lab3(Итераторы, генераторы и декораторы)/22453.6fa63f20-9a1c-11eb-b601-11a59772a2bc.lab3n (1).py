# -*- coding: utf-8 -*-
""" №1
def factorials(n):
    f = 1

    for a in range(1, n+1):
        f = f*a
        yield f
for _ in factorials(10):
    print(_)
"""

""" №2
a = int(input('Give amount: '))

def square_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a**2
        a, b = b, a + b

print(list(square_fibonacci(a)))
"""

""" 4
def arithmetic_operation(op):
    if op=='+':
        return lambda x,y: x+y
    elif op=='-':
        return lambda x,y: x-y
    elif op=='*':
        return lambda x,y: x*y
    elif op=='/':
        return lambda x,y: x/y
    else:
        return lambda x,y: print('bad operation!')

operation = arithmetic_operation('&')
print(operation(1, 4))

"""

""" 5
def same_by(func, val):
    return len(set(map(func, val))) == 1 if val else True
"""

""" 6
def print_operation_table(operation, num_rows=9, num_columns=9):
    print('\n'.join(['\t'.join([str(operation(i, j))
                                for j in range(1, num_columns + 1)])
                     for i in range(1, num_rows + 1)]))

"""

""" 7
print(*sorted(input().split(), key=str.lower))
"""

""" 8
a = [5, 13, -2, 4, -15, 6, 23, 71]
a.sort(key=abs)
print(a)
"""

""" 10
import sys
print("0" in sys.stdin.read().split()) #ctrl+d чтобы закончпть
"""

""" 12
st = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
 
res = sum(lst[0])
 
if all([sum(x) == res for x in lst]) and all([sum(x) == res for x in list(zip(*lst))]):
    print('YES')
else:
    print('NO')
"""


""" 13
def check_password(test):
    def wrap():
        n = input()
        if n != '123':
            print('В доступе отказано')
            return
        test()
    return wrap
      
@check_password
def test():
    print('123')
    return
 
test()

"""


""" 14
def check_password(password):
    def wrapper(func):
        """декоратор"""
        def wrap(*args, **kwargs):
            if input('пароль: ') != password:
                print('неверный пароль')
                return
            return func(*args, **kwargs)
        return wrap
    return wrapper
 
 
@check_password('password')
def make_burger(typeOfMeat, withOnion=False, withTomato=True):
    print('make_burger')
    
    
make_burger(1)
    print(1 + 1)
"""


