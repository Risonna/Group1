"""1

class BigBell:
    def __init__(self):
        self.ding = 'ding'

    def sound(self):
        print(self.ding)
        if self.ding == 'ding':
            self.ding = 'dong'
        else:
            self.ding = 'ding'


"""

"""2
class Balance:
    def __init__(self):
        self.left = 0
        self.right = 0

    def add_right(self, num):
        self.right += num

    def add_left(self, num):
        self.left += num

    def result(self):
        if self.left == self.right:
            return '='
        if self.left > self.right:
            return 'L'
        if self.left < self.right:
            return 'R'
"""

"""3
class Selector:
    def __init__(self, g):
        self.Lis = g
        self.even = []
        self.odd = []
        for i in self.Lis:
            if i % 2 != 0:
                self.odd.append(i)
            else:
                self.even.append(i)

    def get_odds(self):
        return self.odd

    def get_evens(self):
        return self.even
"""


"""4

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
"""

"""5

class ReversedList(object):
    def __init__(self, ls):
        self.a = list(reversed(ls))

    def __str__(self):
        return str(self.a)


rl = ReversedList([5, 50, 100])
print(rl)
"""


"""6
class SparseArray:

    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data.get(key, 0)

    def __setitem__(self, key, value):
        self.data[key] = value
"""

"""7
class Polynomial:
    def __init__(self, koef):
        self.koef = koef

    def __call__(self, x):
        s = 0
        for i in range(len(self.koef)):
            s += self.koef[i] * pow(x, i)
        return s

    def __add__(self, other):
        st = []
        k = Polynomial(st)
        if len(self.koef) < len(other.koef):
            m = len(self.koef)
        else:
            m = len(other.koef)
        for i in range(m):
            st.append(self.koef[i] + other.koef[i])
        if len(self.koef) > m:
            st += self.koef[m::]
        else:
            st += other.koef[m::]
        k.koef = st
        return k
"""

"""8
class Queue:
    def __init__(self, *values):
        self.nums = []
        for i in values:
            self.nums.append(i)

    def append(self, *values):
        for i in values:
            self.nums.append(i)

    def copy(self):
        new = Queue()
        new.nums += self.nums
        return new

    def pop(self):
        if self.nums:
            first = self.nums[0]
            del self.nums[0]
            return first

    def extend(self, queue):
        self.nums += queue.nums

    def next(self):
        new = self.copy()
        new.nums = new.nums[1:]
        return new

    def __rshift__(self, n):
        if len(self.nums) > n:
            new = Queue()
            new.nums += self.nums[n:]
            return new
        return Queue()

    def __add__(self, other):
        new = self.copy()
        new.nums += other.nums
        return new

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __eq__(self, other):
        if self.nums == other.nums:
            return True
        return False

    def __str__(self):
        if self.nums:
            self.nums = list(map(str, self.nums))
            nums = ' -> '.join(self.nums)
            return f'[{nums}]'
        return '[]'


def next(queue):
    new = queue.copy()
    new.nums = new.nums[1:]
    return new


q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)  # 4
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))  # 6
q3 = q2.next()
print(q1, q2, q3, sep='\n')  # 7, 8, 9
print(q1 + q3)  # 10
q3.extend(Queue(1, 2))
print(q3)  # 11
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)  # 12
q5 = next(q4)
print(q4)  # 13
print(q5)

"""

"""9
class Triangle(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):

    def __init__(Triangle, a):
        Triangle.a = a
        Triangle.b = a
        Triangle.c = a

    def perimeter(self):
        return Triangle.perimeter(self)
"""

"""10
class Summator:

    def transform(self, x):
        return x

    def sum(self, N):
        k = 0
        for i in range(1, N + 1):
            k += self.transform(i)
        return k


class SquareSummator(Summator):

    def transform(self, x):
        return x ** 2


class CubeSummator(Summator):

    def transform(self, x):
        return x ** 3


summa = Summator()
print(summa.sum(10))
square = SquareSummator()
print(square.sum(10))
qubes = CubeSummator()
print(qubes.sum(10))
"""

"""12
class A:
    def __str__(self):
        return 'A.__str__ method'

    def hello(self):
        print('Hello')


class B:
    def __str__(self):
        return 'B.__str__ method'

    def good_evening(self):
        print('Good evening')


class C(A, B):
    pass


class D(B, A):
    pass
"""

"""13
class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        if target.is_alive():
            if (self.range ** 2 >= (target.pos_x - actor.pos_x) ** 2 +
                    (target.pos_y - actor.pos_y) ** 2):
                print(f'Врагу нанесен урон оружием {self.name} в размере {self.damage}')
                target.hp -= self.damage
            else:
                print(f'Враг слишком далеко для оружия {self.name}')
        else:
            print('Враг уже повержен')

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, x, y, hp):
        self.pos_x = x
        self.pos_y = y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, amount):
        if self.is_alive():
            self.hp -= amount

    def get_coords(self):
        return self.pos_x, self.pos_y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if target.__class__.__name__ == 'MainHero':
            self.weapon.hit(self, target)
        else:
            print('Могу ударить только Главного героя')

    def __str__(self):
        return f'Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.weapon.name}'


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.weapons = []
        self.current_weapon = 0

    def hit(self, target):
        if self.weapons:
            if target.__class__.__name__ == 'BaseEnemy':
                self.weapons[self.current_weapon].hit(self, target)
            else:
                print('Могу ударить только Врага')
        else:
            print('Я безоружен')

    def add_weapon(self, weapon):
        if weapon.__class__.__name__ == 'Weapon':
            self.weapons.append(weapon)
            print(f'Подобрал {weapon}')
        else:
            print('Это не оружие')

    def next_weapon(self):
        if len(self.weapons) == 1:
            print('У меня только одно оружие')
        elif len(self.weapons) > 1:
            self.current_weapon += 1
            if self.current_weapon == len(self.weapons):
                self.current_weapon = 0
            print(f'Сменил оружие на {self.weapons[self.current_weapon]}')
        else:
            print('Я безоружен')

    def heal(self, amount):
        self.hp += amount
        if self.hp > 200:
            self.hp = 200
        print(f'Полечился, теперь здоровья {self.hp}')
"""

"""14
from sys import exit


class MailClient:
    def __init__(self, server, user):
        self.s = server
        self.u = user

    d = dict()

    def f(self):
        return self.d

    def list(self):
        self.d[self.s] = self.u


class Receive(MailClient):

    def __init__(self):
        super().f()

    def Mail(self):
        s = input('На какой сервер зайдем? ')
        if s in self.d.keys():
            if type(self.d[s]) == tuple:
                print(f'Получено письмо от пользователя {self.d[s][0]}: {self.d[s][1]}')
            else:
                print('В папке "Вся почта" пока пусто')
        else:
            print('К сожалению, такого сервера не существует ¯\_(ツ)_/¯')


class Send(MailClient):

    def __init__(self):
        super().f()

    def get_key(self, d, value):
        for k, v in d.items():
            if v == value:
                return k

    def send(self):
        un = input('Кому напишем? ')
        if un in self.d.values() and len(self.d[self.get_key(self.d, un)]) > 1:
            tom = input('Введи текст сообщения: ')
            for i in self.d.values():
                if i == un:
                    self.d[self.get_key(self.d, un)] = (i, tom)
            print(f'Сообщение успешно отправлено пользователю {un}!')
        else:
            print('Такого пользователя не существует ¯\_(ツ)_/¯')


def main():
    while True:
        print('Привет! Ты попал(а) на почтовый сервис!')
        serv = input('На какой сервер зайдем? ')
        name = input('Как тебя звать? ')
        print(f'{name[0].upper() + name[1:].lower()}, добро пожаловать!')
        m = MailClient(serv, name)
        m.list()
        way = input('Что хотим сделать? ')
        if way.lower().strip() == 'отправить сообщение' or way.lower().strip() == 'написать сообщение' \
                or way.lower().strip() == 'написать':
            s = Send()
            s.send()
        elif way.lower().strip() == 'просмотреть ящик' or way.lower().strip() == 'посмотреть сообщения' \
                or way.lower().strip() == 'прочитать сообщения' or way.lower().strip() == 'почитать' \
                or way.lower().strip() == 'посмотреть почту':
            r = Receive()
            r.Mail()
        else:
            print('Ой! Ошибочка вышла...')

        print('/-----------------------------------------\ ')
        s = '|"exit" - выйти                           |\n|"return" - вернуться на домашнюю страницу|'
        print(s)
        print('\-----------------------------------------/ ')
        a = input()
        if a == 'exit':
            exit()
        elif a == 'return':
            pass
        else:
            print('Ой! Ошибочка вышла...')
            exit()


main()
"""

"""15
class Digits:

    def __init__(self, a):
        self.a = [int(x) for x in a.split()]

    def make_negative(self):
        for i in range(len(self.a)):
            self.a[i] = -abs(self.a[i])

    def square(self):
        for i in range(len(self.a)):
            self.a[i] = (self.a[i]) ** 2

    def strange_command(self):
        for i in range(len(self.a)):
            if self.a[i] % 5 == 0:
                self.a[i] += 1

    def stringify(self):
        for i in range(len(self.a)):
            self.a[i] = str(self.a[i])


d = Digits(input())
for i in range(int(input())):
    s = input()
    if s == 'make_negative':
        d.make_negative()
    elif s == 'square':
        d.square()
    else:
        d.strange_command()
d.stringify()
print(' '.join(d.a))
"""

"""16
from math import sqrt


class Indentity:
    def call(self, x):
        return x


class SqrtFun:
    def call(self, x):
        return sqrt(x)


class Const:
    def __init__(self, value):
        self.value = value

    def call(self, x):
        return self.value


class Expression:
    def __init__(self, f1, op, f2):
        self.f1 = f1
        self.f2 = f2
        self.op = op

    def call(self, x):
        a = self.f1.call(x)
        b = self.f2.call(x)
        if self.op == '+':
            return a + b
        if self.op == '-':
            return a - b
        if self.op == '/':
            return a / b
        if self.op == '*':
            return a * b


def main():
    functions = {'x': Indentity(), 'sqrt_fun': SqrtFun()}
    n = int(input())
    for _ in range(n):
        command, *args = input().split()
        if command == 'define':
            name, f1, op, f2 = args
            if f1.isdigit() or (f1[0] == '-' and f1[1:].isdigit()):
                f1 = Const(int(f1))
            else:
                f1 = functions[f1]
            if f2.isdigit() or (f2[0] == '-' and f2[1:].isdigit()):
                f2 = Const(int(f2))
            else:
                f2 = functions[f2]
            functions[name] = Expression(f1, op, f2)
        elif command == 'calculate':
            name, *x_values = args
            print(' '.join(str(functions[name].call(int(x))) for x in x_values))


if __name__ == '__main__':
    main()
"""

"""18
files = {}


class System:
    def add_directory(self, name):
        directories = name.split('/')
        while len(directories) != 1:
            if directories[0] in list(files.keys()):
                files[directories[0]].append(directories[1])
            else:
                files[directories[0]] = [directories[1]]
            del directories[0]
        files[directories[0]] = []

    def print_directory(self, name):
        print(files[name])


class File:
    def __init__(self):
        self.filecontents = {}

    def add_file_content(self, name, text):
        if name in list(self.filecontents.keys()):
            self.filecontents[name] = text
        else:
            road = name.split('/')
            files[road[-2]].append(road[-1])
            self.filecontents[name] = text

    def print_file_content(self, name):
        print(self.filecontents[name])
"""