# class Point:
#     color = 'red'
#     circle = 2
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#     def get_coords(self):
#         return(self.x, self.y)
# pt = Point()
# pt2 = Point()
# pt.set_coords(1, 2)
# pt2.set_coords(10, 20)
# f = getattr(pt, 'get_coords')
# print(f())
# print(pt.color)

# class Point:
#     def __init__(self, x=0, y=0, z='piu'):
#         print('вызов __init__')
#         self.x = x
#         self.y = y
#         self.z = z
#     def __del__(self):
#         print('Удаление экземпляра: ' + str(self))
# pt = Point(1, 7)
# print(pt.__dict__)

# import random
# class Ghost(object):
#   def __init__(self):
#     self.color = random.choice(["white", "yellow", "purple", "red"])

# class Point:
#     def __new__(cls, *args, **kwargs):
#         print('вызов __new__ для ' + str(cls))
#         return super().__new__(cls)
#     def __init__(self, x=0, y=0):
#         print('вызов __init__ для ' + str(self))
#         self.x = x
#         self.y = y
# pt = Point(1, 2)
# print(pt)

# class DataBase:
#     __instance = None
#     def __new__(cls, *arg, **fup):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#     def __del__(self):
#         DataBase.__instance = None
#     def __init__(self, user, psw, port):
#         self.user = user
#         self.psw = psw
#         self.port = port
#     def connect(self):
#         print(f'соединение с БД: '
#               f'{self.user}, '
#               f'{self.psw}, '
#               f'{self.port}')
#     def close(self):
#         print('закрытие соединения с БД')
#     def read(self):
#         return 'данные из БД'
#     def write(self, data):
#         print(f'запись в БД {data}')
# db = DataBase('user1', '5690', 90)
# db2 = DataBase('user2', '7345', 12)
# print(id(db), id(db2))

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def get_coord(self):
#         return self.x, self.y
# v = Vector(1, 2)
# res = v.get_coord()
# rev = Vector.get_coord(v)
# print(f'Vernuli: {res}, {rev}')

# a = input()
# print(a, type(a))

# s1 = "Панда"
# s2 = "Panda"
# print(s1)
# print(s2)
# text = '''278. I'd like a cup of coffee.
# 279. My boss doesn't see her.
# 280. I want to buy a new flat (apartment).
# 281. He doesn't know it.
# 282. I'd like a cup of tea.
# 283. I need to speak English fluently.
# 284. I want to have a good car.
# 285. I'd like to become a businessman.'''
# print(text)

# a, b = map(str, input().split())
# print(" ".join(sorted([a, b])))

# x = 4
# if x < 0:
#     x = -x
# print(x)

# marks = [3, 3, 4, 4]
# if 2 in marks:
#     print("otchislen")
# else:
#     print('sdal')

# x = int(input())
# if x < 0:
#     print("x - отрицательное число")
# else:
#     print("x - не отрицательное число")

# lst = list(map(int, input()))
# if sum(lst[0:3]) == sum(lst[3:7]):
#     print("ДА")
# else:
#     print("НЕТ")

# Работа светофора для пешеходов запрограммирована следующим
# образом: в начале каждого часа в течение трех минут горит
# зеленый сигнал, затем в течение двух минут – красный,
# в течение трех минут – опять зеленый и т. д.
# Дано вещественное число t, означающее время в минутах,
# прошедшее с начала очередного часа. Определить,
# сигнал какого цвета горит для пешеходов в этот момент.
# На экран вывести сообщение (без кавычек) "green" -
# для зеленого и "red" - для красного.
# a = float(input())
# if 0 <= a%5 <= 3:
#     print("green")
# else:
#     print("red")

# x = int(input())
# if x % 2 == 0:
#     if 0 <= x <= 9:
#         print("x - это цифра")
#     else:
#         print("x - это число")
# else:
#     print("x - нечетное число")

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# if a > b:
#     if a > c:
#         print("a - max")
#     else:
#         print("c - max")
# else:
#     if b > c:
#         print("b - max")
#     else:
#         print("c - max")

# m = '''1. Введение в Python
# 2. Строки и списки
# 3. Условные операторы
# 4. Циклы
# 5. Словари, кортежи и множества
# 6. Выход'''
# a = m[m.find("1"):m.find("2")]
# print(a)

# month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# a, b = map(int, input().split())
# b1 = None
# b2 = None
# a1 = None
# a2 = None
# if 1 < b < month[a-1]:
#     b1 = b-1
#     b2 = b+1
#     a1 = a
#     a2 = a
# elif b == 1:
#     b1 = month[(a-1)-1]
#     b2 = b+1
#     a1 = a-1
#     a2 = a
# elif b == month[a-1]:
#     b1 = b-1
#     b2 = 1
#     a1 = a
#     a2 = a+1
# print(f"{str(a1).rjust(2, '0')}.{str(b1).rjust(2, '0')} {str(a2).rjust(2, '0')}.{str(b2).rjust(2, '0')}")

# a = 12
# b = 7
# res = a if a > b else b
# print(res)

# s = "python"
# t = 'upper'
# res = s.upper() if t == 'upper' else s
# print(res)

# m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# a, b, c = map(int, input().split())
# a1 = m[a - 1] if (m[a - 1] != "до" and m[a - 1] != "фа") else ("#" + m[a - 1])
# b1 = m[b - 1] if (m[b - 1] != "до" and m[b - 1] != "фа") else ("#" + m[b - 1])
# c1 = m[c - 1] if (m[c - 1] != "до" and m[c - 1] != "фа") else ("#" + m[c - 1])
# print(f"{a1} {b1} {c1}")

# s = 0
# i = 1
# N = 1000
# while i <= N:
#     s += i
#     i += 1
# print(s)

# pass_true = "password"
# ps = ""
# while ps != pass_true:
#     ps = input("Введите пароль: ")
# print("Вход в систему")

# N = 20
# i = 1
# while i <= N:
#     if i % 3 == 0:
#         print(i)
#     i += 1

# a = int(input())
# i = 10
# res = 1
# while a > 0:
#     res *= a % (i)
#     a = a // i
# print(int(res))

# a = int(input())
# i = 1
# res = i
# lis = [res]
# while len(lis) < a:
#     lis.append(res)
#     res = lis[i-1] + lis[i]
#     i += 1
# print(*lis)

# n = int(input())
# i = 0
# a = 1
# while i < (n // 3):
#     a *= 2
#     i += 1
# print(a)

# year = int(input())
# schet = 1000
# i = 0
# while i < year:
#     schet *= 1.05
#     i += 1
# print(schet)

# n, m = map(int, input().split())
# b = (n % 2) - 1
# i = n + (n % 2)
# lis = []
# while n <= i <= m:
#     lis.append(i)
#     i += 2
# print(*lis)

# i = 100
# lis = []
# while len(str(i)) == 3:
#     if i % 47 == 43 and i % 3 == 0:
#         lis.append(i)
#     i += 1
# print(*lis)

# n, m = map(int, input().split())
# b = (n % 2) == 0
# i = n+b
# lis = []
# while n <= i <= m:
#     lis.append(i)
#     i += 2
# print(*lis)

# d = [1, 5, 3, 1, 16, 11, 19]
# i = 0
# flFind = False
# while i < len(d):
#     print(i)
#     flFind = d[i] % 2 == 0
#     if flFind:
#         break
#     i += 1
# print(flFind)

# s = 0
# d = 1
# while d != 0:
#     d = int(input("Введите целое число: "))
#     if d % 2 == 0:
#         continue
#     s += d
#     print("s = " + str(s))

# p = [0] * 10
# i = None
# while p.count(1) < 5:
#     i = int(input())
#     if p[i] == 1:
#         continue
#     p[i] = 1
# print(*p)

# names = list(map(str, input().split()))
# i = 0
# a = None
# while i < len(names):
#     a = names[i].upper()
#     if a[0] == a[-1]:
#         break
#     i += 1
# if i < len(names):
#     print("ДА")
# else:
#     print("НЕТ")
#
# n = int(input())
# i = 1
# lis = []
# while 0 < i < 100:
#     if i % 3 == 0 and i % 5 == 0:
#         lis.append(i)
#     if i >= n:
#         print(*lis)
#         break
#     i += 1
# else:
#     print("слишком большое значение n")

# maxa = int(input())
# i = 10
# d = 1
# while True:
#     if i > maxa:
#         break
#     i *= 1.1
#     d += 1
# print(d)

# d = [1, 2, 3, 4, 5]
# for x in d:
#     print(x)

# print(*range(11))

# a = list(input().split())
# for i in range(len(a)):
#     a[i] = len(a[i])
# print(*

# a = list(map(str, input().lower().split()))
# for i in range(len(a)):
#     a[i] = a[i].rstrip('ъыь')
#     if i > 0:
#         if a[i-1][-1] != a[i][0]:
#             print("НЕТ")
#             break
# else:
#     print("ДА")

# words = ['Python', 'дай', 'мне', 'сил']
# s = ''
# for w in words:
#     s += w + " "
# print(s.rstrip())

# words = ['Python', 'дай', 'мне', 'сил']
# a = " ".join(words)
# print(a)

# digs = [1, 2, 67, 98, 154, -11, 20, 4]
# for i, d in enumerate(digs):
#     print(i, d)
#     if 10 <= abs(d) <= 99:
#         digs[i] = 0
# print(digs)

# t = ["a", "b", "v", "g", "d"]
# start_index = ord('а')
# title = "вава..., вада..., баба,,,,,"
# slug = ''
# for s in title.lower():
#     if 'а' <= s <= 'д':
#         slug += t[ord(s) - start_index]
#     elif s in " !?:;.,":
#         slug += "-"
#     else:
#         slug += s
# while "--" in slug:
#     slug = slug.replace('--', '-')
# print(slug.rstrip("-"))

# strk = input()
# bit = 0
# x = None
# while bit < strk.count("ра"):
#     print(strk.find("ра", x), end=" ")
#     bit += 1
#     x = strk.find("ра", x) + 2
# if bit == 0:
#     print(-1)

# strg = input()
# if strg[0:3] == "+7(" and strg[6] == ")" and strg[10] == "-" and strg[13] == "-" and strg[3:6].isdigit() and strg[7:10].isdigit() and strg[11:13].isdigit() and strg[14:].isdigit():
#     print("ДА")
# else:
#     print("НЕТ")

# a = input()
# a = a.replace(" ", "")
# s = 0
# a1 = a.split("-")
# for i, znak in enumerate(a1):
#     a1[i] = znak.split("+")
# for i in range(len(a1)):
#     for el in range(len(a1[i])):
#         a1[i][el] = int(a1[i][el])
#     a1[i] = sum(a1[i])
# for i in range(len(a1)):
#     if i == 0:
#         s += a1[i]
#     else:
#         s -= a1[i]
# print(s)

# a = input()
# a = a.replace(" ", "")
# a = a.replace("+", "_+")
# a = a.replace("-", "_-")
# a = a.split("_")
# for i in range(len(a)):
#     a[i] = int(a[i])
# s = sum(a)
# print(s)

# a = list(map(int, input().split()))
# a2 = []
# print(a)
# for i in range(len(a)):
#     a2.append(a[i])
#     a2.append(a[i])
# print(a2)
#
# a = list(map(float, input().split()))
# x = a[0]
# for i in a:
#     if i <= x:
#         x = i
# print(x)

# a = [[1,2,3],[4,5,6],[7,8,9]]
# a2 = []
# for i, row in enumerate(a):
#     r = []
#     for j in range(len(row)):
#         r.append(a[j][i])
#     a2.append(r)
# print(a2)

# N = int(input())
# s = []
# for i in range(N):
#     s1 = []
#     for j in range(N):
#         s1.append(1)
#     s.append(s1)
#     s[i][N-1] = N+1
#     print(*s[i])

# lst_in = ['django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya', 'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']
# for i in range(len(lst_in)):
#     while "  " in lst_in[i]:
#         lst_in[i] = lst_in[i].replace("  ", " ")
#     lst_in[i] = lst_in[i].replace(" ", "-")
#     print(lst_in[i])

# n = int(input())
# s = []
# for i in range(2, n):
#     bit = 0
#     for j in range(2, n):
#         if i % j == 0:
#             bit += 1
#     if bit <= 1:
#         s.append(i)
# print(*s)

# lst_in = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
# a = "ДА"
# for i, row in enumerate(lst_in[:-1]):
#     for el, cow in enumerate(row[:-1]):
#         if cow + lst_in[i][el+1] + lst_in[i+1][el] + lst_in[i+1][el+1] > 1:
#             a = "НЕТ"
#             break
#
# print(a)

# lst_in = [[2, 3, 4, 5, 6], [3, 2, 7, 8, 8], [4, 7, 2, 0, 4], [5, 8, 0, 2, 1], [6, 9, 4, 1, 2]]
# a = "ДА"
# for i, row in enumerate(lst_in):
#     for j, cow in enumerate(row):
#         if lst_in[i][j] != lst_in[j][i]:
#             a = "НЕТ"
#             break
# print(a)

# a = [2, 4, 6, 1, -5, -5, 7]
#
# # -5 -5 6 1 2 4 7
#
# for i in range(len(a)):
#     x = min(a[i:])
#     if a[i] > x:
#         c = a[i:].index(x)
#         a[i], a[c] = a[c], a[i]
#
#
# print(*a)

a = [f'{i} * {j} = {i*j}'
     for i in range(4)
     for i in range(4)
     ]
for i in a:
    for el in range(1, len(a)+1, 4):
        print(a[el], end="   ")