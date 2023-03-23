# print("Hello")
# print("Результат: ", 5, ", ", 15, sep="")
# print("Second line")
# print('Second \\line')
# print("Ostatok pri delenii:", 5%5, sep=" ")
# print("Mimimalnoe chislo:", pow(6, 2))
# input("Vvedi chota: ")

# celoe_chislo = 4 # integer
# drobnoe_chislo = 4.5 # float
# word = "Privit" # string
# TrueFalse = True # boolean

# print(celoe_chislo + drobnoe_chislo)
# print(celoe_chislo + word)
# chiselko = "3"

# print(word + " " + str(celoe_chislo + int(chiselko)), sep=" ")

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
#
# number1 += 5
#
# print("Result: ", number1 + number2)
# print("Result: ", number1 - number2)
# print("Result: ", float(number1 * number2))
# print("Result: ", str(number1 / number2))
# print("Result: ", number1 ** number2)
# print("Result: ", number1 // number2)

# doom = 0
# print(bool(doom))

# num1 = 2
# num1 **= 3
# print(num1)

# if 5 > 5:
#     print("yes")
#     print("!!!")

# user_data = int(input("VVedite chislo: "))
# if user_data != 5:
#     print("Number is not 5")
#     if user_data >= 6:
#         print("Number is bigger than 5")
# print("a pofig")

# isHappy = True
# if isHappy == True:
#     print("Happy")

# isHappy = True
# if isHappy:
#     print("Happy")

# isHappy = True
# if isHappy == False:
#     print("Happy")

# isHappy = True
# if not isHappy:
#     print("Happy")

# user_data = int(input("chislo suda: "))
# per = False
# if not per:
#     print("happy")
# elif user_data == 5:
#     print("chislo piat")
# elif user_data == 7:
#     print("chislo sem")
# else:
#     print("unhappy")

# data = True
# user_data = int(input("chislo suda: "))
#
# if data or user_data == 5:
#     print("pravda 5")
# else:
#     print("neudacha")
#
# data = input()
#
# number = 5 if data == "Five" else 0
#
# # if data == "Five":
# #     number = 5
# # else:
# #     number = 0
#
# print(number)

# for i in range(1, 6, 2):
#     print(i)

# count = 0
# word = "Hello World!!!"
# for i in word:
#     if i == "l":
#         count += 1
#         print(count)
# print("count:", count)

# i = 5
# while i <= 15:
#     print(i)
#     i += 2

# polznach = True
# while polznach:
#     if input() == "Stop":
#         polznach = False

# for i in range(1, 11):
#     if i == 5:
#         break
#     if i % 2 == 0:
#         continue
#     print(i)

# found = None
# for i in "hello":
#     if i == "l":
#         found = True
#         break
#     else:
#         found = False
# print(found)

# word = ["Hello"]
# for i in word:
#     print(len(i))

# i = True
# a = str(input())
# while i:
#     if a == "Stop":
#         i = False
#     elif a == "stop":
#         i = False
#     else:
#         a = str(input())

# i = True
# while i:
#     if input() == "Stop" or input() == "stop":
#         i = False

# nums = [5, 1, 5, 4, 7, 8, 14, 8.7]
# print(nums)

# nums = [2, True, "Hello", 8.1, [2, 3, 4, 5]]
# nums[0] = 50
# nums[1] = 1
# print(nums)
# print(nums[4])
# print(nums[-1][1])

# numbers = [5, 7, 14, 12]
# # numbers[4] = -1
# numbers.append(-1)
# numbers.append(-7)
# numbers.insert(1, 6)
# numbers.insert(-1, 6)
# numbers.extend([14, 15, 16])
# a = [14, 15, 16]
# numbers.extend(a)
# numbers.sort()
# numbers.pop()
# numbers.pop(-2)
# numbers.remove(14)
# # numbers.clear()
# print(numbers)
# print(numbers.count(8))
# print(len(numbers))

# nums = [5, 2, 7, "50", False]
# for el in nums:
#     el *= 2
#     print(el)

# n = input("Enter length: ")
# user_list = []
# i = 0
# while i < int(n):
#     string = "Enter chisllo " + str(i+1) + ":"
#     user_list.append(int(input(string)))
#     i += 1
# print(user_list)
# for el in user_list:
#     el *= 2
#     print(el)

# n = int(input("Enter length: "))
# user_list = []
# while len(user_list) < n:
# 	string = input(f"Entr element #{len(user_list)+1}: ")
# 	user_list.append(string)
# print(user_list)

# stroka = 'Privet konfeta, ahaha'
# print(stroka[5])
# print(len(stroka))
# print(stroka.count('h'))
# print(stroka.count(')'))
# print(stroka.upper())
# print(stroka.isupper())
# print(stroka.lower())
# print(stroka.islower())
# print(stroka.capitalize())
# print(stroka.find('a'))
# print(stroka.split(' '))

# stroka = 'Privet konfeta, ahaha'
# spisok = stroka.split(' ')
# print(spisok)
# print(spisok[1])

# word = 'goodbuy'
# print(word[1:6:2])

# list = [6, 7, False, 'Future', 0.9]
# print(list[::-1])

# number = 3.1415926535897932
# print(str(number)[3])

# data = (4, 6, 7, 8, 14, 'coco', False)
# print(data[1:])
#
# data = (4, 6, 7, 8, 14, 'coco', False)
# print(data.count(14))
# print(len(data))
#
# cortezh = 4, 6, 17
# print(cortezh)
# cort = 4
# print(cort)
# cort2 = 4,
# print(cort2)
# cort3 = (4)
# print(cort3)

# cort = 1, 5, 16, 'dude', True, 'pdfka', 17.8
# for el in cort:
#     print(el)
#
# nums = [4, 6, 18]
# new_data = tuple(nums)
# print(new_data)
#
# stroka = tuple('boogimen plashet')
# print(stroka)

# proverka = input('Vvod: ')
# print(proverka.count('-'))
# print(proverka.count('-') * 100 / 300)

# print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
# contents = []
# while True:
#     try:
#         line = input()
#     except EOFError:
#         break
#     contents.append(line)
# print(contents)

# country = {'code': 'RU', 'name': 'Russian', 'populatin': 144}
# print(country['code'])

# country = dict(code='RU', name='Russion')
# print(country['code'])

# country = {'code': 'RU', 'name': 'Russian', 'populatin': 144}
# print(country['code'])
# print(country)
# for key in country: # - цикл для вывода ключей
#     print(key)

# country = {'code': 'RU', 'name': 'Russian', 'populatin': 144}
# print(country['code'])
# print(country.items())
# for key, value in country.items(): # - цикл для вывода значений
#     print(key, ' - ', value)

# Действия со словарями
# country = {'code': 'RU', 'name': 'Russian', 'populatin': 144}
# print(country['code'])
# print(country.get('name'))
# country.clear()
# country.pop('name')
# country.popitem()
# print(country.keys())
# print(country.values())
# country.update()
# country['code'] = 'None'
# print(country)

# person = {
#     'user_1': {
#         "first name": 'John',
#         "second name": "Pavlov",
#         "years old": 19,
#         "sex": "male",
#         "address": ['г. Москва', 'ул. Какая-то', '45']},
#     'user_2': {
#         "first name": 'Anna',
#         "second name": "Kim",
#         "years old": 39,
#         "sex": "female",
#         "address": ['г. Москва', 'ул. Какая-то', '94']},
#     'user_3': {
#         "first name": 'Mike',
#         "second name": "Johns",
#         "years old": 14,
#         "sex": "male",
#         "address": ['г. Москва', 'ул. Какая-то', '40']}}
# person['user_3']['first name'] = 'Mikel'
# print(person['user_3']['first name'])

# def create_phone_number(n):
#     s = ''.join(str(i) for i in n)
#     return print('Phone number: ', '"(', s[0:3], ") ", s[3:6], "-", s[6:10], '"', sep="")
# create_phone_number([1, 3, 6, 8, 4, 3, 4, 8, 6, 9])

# a = [1, 3, 5, 7, 9]
# b = [0, 2, 4, 6, 8]
# c = ('chetnoe')
# d = ('nechetnoe')
# slovar = {d:a, c:b}
# print(slovar)

# a = [1, 3, 5, 7, 9]
# b = [0, 2, 4, 6, 8]
# c = ('chetnoe')
# d = ('nechetnoe')
# slovar = dict(d=a, c=b)
# print(slovar)

# data = set('hello')
# print(data)

# data = {5, 7, 3, 1, 2, 3, 4, 5, 6, 7}
# data.add(84)
# data.update(["76", False, 8, 9, 10, 5])
# data.remove(False)
# data.pop()
# data.clear()
# print(data)

# nums = [2, 5, 5, 6, 6, 99, 10, 2]
# new_nums = set(nums)
# print(new_nums)

# new_data = frozenset([5, 7, 3, 1, 2, 3, 4, 5, 6, 7])
# print(new_data)

# integer = 5
# limit = 28
# spisok = [int(integer), int(limit)]
# i = 2
# while spisok[0] <= limit:
#     a = integer
#     a *= i
#     print(integer)
#     if a > limit:
#         break
#     spisok.insert(0, a)
#     i += 1
#     print(spisok)
# spisok.sort()
# print(spisok)

# integer = 5
# limit = 25
# spisok = [integer, limit]
# i = 2
# while spisok[0] <= limit:
#     a = integer
#     a *= i
#     if a > limit:
#         break
#     spisok.insert(0, a)
#     i += 1
# if limit >= spisok[0]:
#     spisok.remove(limit)
# spisok.sort()
# print(spisok)

# def find_multiples(integer, limit):
#     return list(range(integer, limit+1, integer))
# print(find_multiples(3, 31))

# def test_funk(word):
#     print(word, end = "")
#     print("!")
# test_funk("Gugleopik")
# test_funk("Joker")

# def summa(a, b, c):
#     res = a+b+c
#     print("Result: ", res)
# summa("hi", "people", "!")
# summa(9, 10, 11)

# def summa(a, b):
#     res = a + b
#     return res
# res = summa(2, 3)
# print(res)
# res = summa()

# def summa(a, b):
#     return a + b
# print(summa(2,3))

# nums1 = [10, 17, 77, 5, 7, 0]
# min = nums1[0]
# for el in nums1:
#     if el < min:
#         min = el
# print(min)

# nums2 = [5.6, 8.9, 0.1, 9.2, 8]
# min2 = nums2[0]
# for el in nums2:
#     if el < min2:
#         min2 = el
# print(min2)

# def minimal(l):
#     mini = l[0]
#     for el in l:
#         if el < mini:
#             mini = el
#     print(mini)
#     return mini
# nums1 = [10, 17, 77, 5, 7]
# nums2 = [5.6, 8.9, 0.1, 9.2, 8]
# min1 = minimal(nums1)
# min2 = minimal(nums2)
# if min1 <= min2:
#     print(min1)
# else:
#     print(min2)

# def funciya(x, y):
#     return x * y
# print(funciya(4, 70))

# funciya = lambda x, y: x * y
# print(funciya(5, 2))

# def rps(p1, p2):
#     otvet = None
#     a = "paper"
#     b = "rock"
#     c = "scissors"
#     if p1 == p2:
#         otvet = "Draw!"
#     elif (p1 == a and p2 == b) or (p1 == b and p2 == c) or (p1 == c and p2 == a):
#         otvet = "Player 1 won"
#     elif (p2 == a and p1 == b) or (p2 == b and p1 == c) or (p2 == c and p1 == a):
#         otvet = "Player 2 won"
#     return otvet
# print(rps("paper", "scissors"))

# def reverse_list(l):
#     rev = []
#     for el in l:
#         rev.append(el)
#     rev.reverse()
#     return rev
#
# a = [1, 2, 3, 4]
# print(reverse_list(a))

# def reverse_list(l):
#   l.reverse()
#   return l
#
# a = [1,9, 3, 4]
# print(reverse_list(a))

# data = input('Vvvedi text: ')
# file = open('data/text.txt', 'a')
# file.write(data + '\n')
# file.close()

# file = open('data/text.txt', 'r')
# # print(file.read())
# for line in file:
#     print(line, end='')
# file.close()

# x = 0
# while x == 0:
#     try:
#         x = int(input("Vvedite chislo: "))
#         x += 5
#         print(x)
#     except ValueError:
#         print('Vvedite imenno chislo!')

# try:
#     x = 5/1
#     x = int(input())
# except ZeroDivisionError:
#     print("Деление на ноль!!!")
# except ValueError:
#     print("Вы ввели что-то не так!")
# else:
#     print("else")
# finally:
#     print('Finally')

# def merge_arrays(arr1, arr2):
#     return sorted(list(set(arr1+arr2)))
# x = merge_arrays([1,2,3,4], [9,8,7,6,5,4,3,2])
# print(x)

# def is_opposite(s1,s2):
#     i = 0
#     if s1 == "" or s2 == "":
#         return False
#     else:
#         for el in s1:
#             if el == s2[i]:
#                 return False
#             elif el != s2[i]:
#                 i += 1
#                 return True
# print(is_opposite("Ab", "Ab"))

# try:
#     with open('data/text.txt', 'r', encoding='utf-8') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('Файл не найден')

# from mymodule import add_three_numbers as add
# print(add(5, 6, 0))

# import cowsay
# cowsay.cow('Hell')

# def get_status(is_busy):
#     status = dict(status = "None")
#     if is_busy == True:
#         status["status"] = "busy"
#     else:
#         status["status"] = "available"
#     return status

# class Cat:
#     name = None
#     age = None
#     isHappy = None
#     some = [1, 2, 3]
#     def set_data(self, name, age, isHappy):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#     def get_data(self):
#         print(self.name, "age: ", self.age, ". Happy: ", self.isHappy)
# cat1 = Cat()
# cat1.set_data("Barsik", 3, True)
# cat2 = Cat()
# cat2.set_data("Nochnoy ohotnik", 90, False)
# cat2.get_data()

# class Cat:
#     name = None
#     age = None
#     isHappy = None
#     some = [1, 2, 3]
#     def set_data(self, name = None, age = None, isHappy = None):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#     def get_data(self):
#         print(self.name, "age: ", self.age, ". Happy: ", self.isHappy)
#     def __init__(self, name=None, age=None, isHappy=None):
#         self.set_data(name, age, isHappy)
#         self.get_data()
# cat1 = Cat()
# cat1.set_data()
# cat2 = Cat("Nochnoy ohotnik", 90, False)

# class Point:
#     color = 'red'
#     circle = 2

# text = input('Vvedi: ')
# mistakes = text.count(' -')
# proc = (600 - int(mistakes)) * 100 / 600
# print(mistakes, proc, sep="\n")

# arrows = ([{'range': 5}, {'range': 10, 'damaged': True}, {'damaged': True}])
# print(len(arrows))
# a = 0
# for el in arrows:
#     value = el.get('damaged')
#     if value == True:
#         a += 1
# if a >= len(arrows):
#     print(False)
# else:
#     print(True)

# def list_animals(animals):
#     list = ''
#     nomer = 1
#     a = None
#     for i in animals:
#         list += str(nomer) + '. ' + i + '\n'
#         nomer += 1
#         print(list)
#         # list += nomer + 1, '. ', animals[i], '\n'
#     return list
#
# animals = [ 'dog', 'cat', 'elephant' ]
# list_animals(animals)

# def find_average(nums):
#     a = 0
#     for i in nums:
#         a += i
#     return a/len(nums)
# print(find_average([1, 3, 5, 7]))

# def lowercase_count(strng):
#     i = 0
#     for buk in strng:
#         if buk.islower():
#             i += 1
#     return(i)
# print(lowercase_count("abcABC123"))

# def rain_amount(mm):
# #     if mm < 40:
# #          return "You need to give your plant " + str(40 - mm) + " mm of water"
# #     else:
# #          return "Your plant has had more than enough water for today!"
# # print(rain_amount(42))

# stroka = "papa, dad"
# str2 = stroka.split(",")
# print(str2[0])

# a = [2, 4, 6, 1, -5, -5, 7]
# # -5 -5 6 1 2 4 7
# for i in range(len(a)):
#     x = min(a[i:])
#     if a[i] > x:
#         c = a.index(x, i+1)
#         a[i], a[c] = a[c], a[i]
#
# print(*a)

# a = [2, 4, 6, 1, -5, -5, 7]
# b = 0
# for i in range(len(a)-b):
#     if b < len(a):
#         i = 0
#     else:
#         break
#     for j in range(i+1, len(a)):
#         if a[j] < a[i]:
#             a[j], a[i] = a[i], a[j]
#             i += 1
#             j += 1
#         else:
#             i += 1
#             j += 1
#             continue
#     b += 1
# print(a)

# n = int(input())
# val = [1, 2, 4, 8, 16, 32, 64]
# val = val[::-1]
# alv = ""
# for i in val:
#     if n // i > 0:
#         alv += (str(i) + " ") * (n // i)
#         n -= i * (n // i)
# print(alv)

# N = 16
# lis = []
# for i in range(N):
#     row = [1]*(i+1)
#     for j in range(i+1):
#         if j != 0 and j != i:
#             row[j] = lis[i-1][j-1] + lis[i-1][j]
#     lis.append(row)
# for r in lis:
#     print(r)

# N = 6
# a = [0]*N
# print(a)
# for i in range(N):
#     a[i] = i ** 2
# print(a)
#
# a = [x ** 2 for x in range(N)]

# i = input("Числа через пробел: ")
# print(i)
# i = [int(x) for x in i.split()]
# print(i)

# a = ["hello", "python", "how", "are", "you"]
# for i, row in enumerate(a):
#     x = [el for el in row]
#     a[i] = x
# print(a)

# d = [4, 3, -5, 0, 2, 11, 122, -8, 9]
# a = ["четное" if x % 2 == 0 else "нечетное"
#      for x in d
#      if x > 0
#      ]
# print(a)

# lst = input()
# lst = [abs(float(x)) for x in lst.split()]
# print(lst)

# lst = input()
# lst = [int(x) for x in lst]
# print(lst)

# N = int(input())
# lst = [[0 if j != i else 1 for j in range(N)] for i in range(N)]
# for i in lst:
#     print(*i)

# a = input()
# a = [i for i in a.split() if len(i) > 5]
# print(*a)

# n = int(input())
# lst = [i for i in range(1, n+1) if n % i == 0]
# print(*lst)

# N = int(input())
# [print(*[i]*N) for i in range(N)]

# a = "8.5 11.3 1.0 -4.5 11.34 6.45"
# a = [float(row) for i, row in enumerate(a.split())
#      if i % 2 == 0]
# print(*a)

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = [(a[i] + b[i]) for i in range(len(a))]
# print(*c)

# a, b = list(map(int, input().split())), list(map(int, input().split()))
# print(*[a[i]+b[i] for i in range(len(a))])

# a = input().split()
# a = [[a[i], int(a[i+1])] for i in range(0, len(a), 2)]
# print(a)

# a = [f'{i}*{j} = {i*j}'
#      for i in range(4)
#      for j in range(4)
#      ]
# print(a)
# for i in range(4):
#     print()
#     for el in range(i, len(a), 4):
#         print(a[el], end="   ")

# A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# A = [[row[i] for row in A] for i in range(len(A[0]))]
# print(A)

# g = [u**2 for u in [x+1 for x in range(5)]]
# print(g)

# lst_in = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
# lst_in = [x
#           for i in lst_in[::-1]
#           for x in i[::-1]
#           ]
# print(*lst_in)

# 1 2 3 4 5 6 7 8 9
# a = list(map(int, input().split()))
# from math import sqrt
# N = int(sqrt(len(a)))
# lst = [[a[el] for el in range(i, i+N)] for i in range(0, len(a), N)]
# print(lst)

# t = ["– Скажи-ка, дядя, ведь не даром",
#     "Я Python выучил с каналом",
#     "Балакирев что раздавал?",
#     "Ведь были ж заданья боевые,",
#     "Да, говорят, еще какие!",
#     "Недаром помнит вся Россия",
#     "Как мы рубили их тогда!"
#     ]
# print(len(t))
# lst = [[i for i in t[x].split() if len(i) > 3] for x in range(len(t))]
# print(lst)

# lst_in = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [5, 4, 3]]
# lst_in = [[lst_in[j][i] for j in range(len(lst_in))] for i in range(len(lst_in[0]))]
# print(lst_in)

# d = {"house": "дом", "car": "машина",
#      "tree": "дерево", "road": "дорога",
#      "river": "река"}
# print(d)

# d = input()
# d = [i.split("=") for i in d.split()]
# d = [[int(d[ind][i]) if i == 1 else d[ind][i] for i in range(len(row))] for ind, row in enumerate(d)]
# print(d)

# lst_in = ['5=отлично', '4=хорошо', '3=удовлетворительно']
# d = {}
# for i in range(len(lst_in)):
#     d[int(lst_in[i].split("=")[0])] = lst_in[i].split("=")[1]
# print(*sorted(d.items()))

# d = dict([i.split("=") for i in input().split()])
# print(d)

# +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
# d = input().split()
# x = []
# for i in d:
#     print(i)
#     if not [i[0]+i[1]] in x:
#         x.append([i[0]+i[1]])
# for i in range(len(x)):
#     v = ""
#     for j in d:
#         if [j[0]+j[1]] == x[i]:
#             v += j + " "
#             print(v)
#     x[i].append(v.split())
# d = dict(x)
# print(d)

# lst_in = ['+71234567890 Сергей', '+71234567810 Сергей', '+51234567890 Михаил', '+72134567890 Николай']
# lst_in = [lst_in[i].split() for i in range(len(lst_in))]
# d = []
# for i in range(len(lst_in)):
#     if not [lst_in[i][1]] in d:
#         d.append([lst_in[i][1]])
# for el in range(len(d)):
#     v = []
#     for i in range(len(lst_in)):
#         if [lst_in[i][1]] == d[el]:
#             v.append(lst_in[i][0])
#             print(v)
#     d[el].append(v)
# d = dict(d)
# print(d)

# lst_in = ['+71234567890 Сергей', '+71234567810 Сергей', '+51234567890 Михаил', '+72134567890 Николай']
# lst_in = [i.split() for i in lst_in]
# d = {}
# for i in lst_in:
#     key = i[1]
#     value = i[0]
#     if not key in d:
#         d[key] = [i[0]]
#     else:
#         d[key] += [i[0]]
# print(d)

# Пользователь вводит в цикле целые положительные числа, пока не введет число 0.
# Для каждого числа вычисляется квадратный корень (с точностью до сотых) и значение
# выводится на экран (в столбик). С помощью словаря выполните кэширование данных так,
# чтобы при повторном вводе того же самого числа результат не вычислялся, а бралось ранее
# вычисленное значение из словаря. При этом на экране должно выводиться:
#
# значение из кэша: <число>

# x = None
# d = {}
# while x != 0:
#     x = int(input())
#     a = round(x**0.5, 2)
#     if x == 0:
#         break
#     elif not x in d:
#         d[x] = a
#         print(a)
#     else:
#         print(f"значение из кэша: {a}")
# print(d)

# d = {}
# n = None
# while True:
#     n = input()
#     if n in d:
#         print(f"Взято из кэша: {d[n]}")
#     else:
#         d[n] = "HTML-страница для адреса " + n

# morz = {"А":".-", "Б": "-...", "В":".--", "Г": "--.",
#         "Д": "-..", "Е": ".", "Ж": "...-", "З": "--..",
#         "И": "..", "Й": ".---", "К": "-.-", "Л": ".-..",
#         "М": "--", "Н": "-.", "О": "---", "П": ".--.",
#         "Р": ".-.", "С": "...", "Т": "-", "У": "..-",
#         "Ф": "..-.", "Х": "....", "Ц": "-.-.", "Ч": "---.",
#         "Ш": "----", "Щ": "--.-", "Ъ": "--.--", "Ы": "-.--",
#         "Ь": "-..-", "Э": "..-..", "Ю": "..--", "Я": ".-.-",
#         " ": "-...-"}
# # a = ""
# # for i in input().upper():
# #     a += morz.get(i) + " "
# # print(a.strip())
# zorm = {}
# for key, value in morz.items():
#     zorm[value] = key
#
# a = ".-- ... . -...- .-- . .-. -. ---"
# a = a.split()
# for i in a:
#     print(zorm[i].lower(), end="")

# lst = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']
# lst_in = {}
# for i in lst:
#     a, b = i.split()
#     print(a, b)
#     if not a in lst_in:
#         lst_in[a] = b
#     else:
#         lst_in[a] += ", " + b
# for i in lst_in:
#     print(f"{i}: {lst_in.get(i)}")

# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
# Сергей собирается в поход и готов взвалить на свои хрупкие плечи максимальный вес в N кг (вводится с клавиатуры).
# Он решил класть в рюкзак предметы в порядке убывания их веса (сначала самые тяжелые, затем, все более легкие) так,
# чтобы их суммарный вес не превысил значения N кг. Все предметы даны в единственном экземпляре. Выведите список
# предметов (в строчку через пробел), которые берет с собой Сергей в порядке убывания их веса.
# P. S. 1 кг = 1000 грамм
# things2 = {value: key for key, value in things.items()}
# N = int(input()) * 1000
# bag = []
# i = 0
# while N >= 0 and len(things2) > 0:
#     if len(things2) > 1:
#         i = max(things2.keys())
#     else:
#         i = 10
#     a = things2.pop(i)
#     if N >= i:
#         bag.append(a)
#         N -= i
# print(*bag)

# class Guesser:
#     def __init__(self, number, lives):
#         self.number = number
#         self.lives = lives
#
#     def guess(self, n):
#         while self.lives > 0:
#             if n == self.number:
#                 return True
#             else:
#                 self.lives -= 1
#                 return False
#         else:
#             raise "Expect error: \"Omae wa mo shindeiru\""
#
# guesser = Guesser(10, 0)
# print(guesser.guess(1))
# print(guesser.guess(1))
# print(guesser.guess(1))
# print(guesser.guess(1))

# t = tuple(input().split())
# t2 = ()
# if "Ульяновск" in t:
#     for i in t:
#         if i == "Ульяновск":
#             continue
#         t2 += (i,)
#     print(*t2)
# else:
#     print(*t)

# t = ((1, 0, 0, 0, 0),
#      (0, 1, 0, 0, 0),
#      (0, 0, 1, 0, 0),
#      (0, 0, 0, 1, 0),
#      (0, 0, 0, 0, 1))
# N = int(input())
# t2 = ()
# for i in range(0, N):
#     x = ()
#     for j in range(0, N):
#         x += (t[i][j],)
#     t2 += (x,)
# for i in t2:
#     print(*i)

# lst_in = ['Главная home', 'Python learn-python', 'Java learn-java', 'PHP learn-php']
# lst_in = {i.split()[0]: i.split()[1] for i in lst_in}
# t = tuple(lst_in.items())
# print(t)

# s = set(map(str, input().lower().split()))
# print(s)

# s = set(input())
# g = [i for i in s if i.isdigit()]
# print(*sorted(g)) if len(g) > 0 else print("НЕТ")
#
# def evil(n):
#     if n == 1: return "It's Odious!"
#     s = []
#     while n // 2 > 0:
#         s.append(n%2)
#         n = n//2
#         if n == 1:
#             s.append(n)
#     return "It's Evil!" if s.count(1) % 2 == 0 else "It's Odious!"

# d = {2, 3, 5}
# N = int(input())
# prost = set()
# res = set()
# for i in range(1, 1000):
#     x = set()
#     for j in range(1, 1000):
#         if i % j == 0:
#             x.add(j)
#     if len(x) <= 2:
#         prost.add(i)
# for i in prost:
#     if N % i == 0:
#         res.add(i)
# print("ДА") if res >= d else print("НЕТ")

# x = input().split()
# d = {i: x[i] for i in range(int(x[0]), len(x))}
# print(d)

# x = input().split()
# d = {key: value for key, value in enumerate(x[1:], int(x[0]))}
# print(d)

# d = input().lower().split()
# d = {i:d.count(i) for i in d}
# print(0) if "и" not in d else print(d["и"])

# lst_in = ["Пушкин: Сказака о рыбаке и рыбке",
#           "Есенин: Письмо к женщине",
#           "Тургенев: Муму",
#           "Пушкин: Евгений Онегин",
#           "Есенин: Русь"]
# lst_in = [[i.split(":")[0].strip(), i.split(":")[1].strip()] for i in lst_in]
# d = {i[0]: {j[1] for j in lst_in if i[0] == j[0]} for i in lst_in}
# print(lst_in)
# print(d)

# x = input()
#
# def get_correct_ly(email):
#     a = True
#     simbol = "@._abcdefghijklmnopqrstuvwxyz1234567890"
#     for j, i in enumerate(email.lower()):
#         if i in simbol:
#             a = True
#         else:
#             a = False
#             break
#         if i == "@":
#             a = email[j+1] == "."
#     if email[0].isalpha() and email[-1].isalpha() and email.count("@") == 1 and "." in email and a:
#         print("ДА")
#     else:
#         print("НЕТ")
#
#
# get_correct_ly(x)

# def even(x):
#     return x % 2 == 0
#
#
# sett = [i for i in range(1, 21) if even(i)]
# print(sett)

# def is_triangle(x, y, z):
#     return x+y > z and x+z > y and z+y > x
#
#
# print(is_triangle(3, 4, 5))

# def missing(nums, s):
#     s = s.replace(" ", "")
#     message = ""
#     try:
#         for i in sorted(nums):
#             message += s[i]
#         return message
#     except IndexError:
#         return "No mission today"
#
#
# print(missing([12, 4, 6], "Good Morning"))


# def break_chocolate(n, m):
#     i = 0
#     if m > 0 and n > 0:
#         i = (m-1) + ((n-1) * m)
#     else:
#         i = 0
#     return i
#
# print(break_chocolate(4, 7))

# def get_nod(a, b):
#     """Вычисление НОД для натуральных чисел
#     a и b по алгоритму Евклида.
#     :param a: первое натуральное число
#     :param b: второе натуральное число
#     :return: НОД
#     """
#
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a
#
#
# a = get_nod(82, 12)
# print(a)

# def speedo_get_nod(a, b):
#     while min(a,b) > 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#     return max(a, b)

# def get_nod(a, b):
#     while min(a, b) != 0:
#         a, b = max(a, b), a % b
#     return max(a, b)
#
#
# import time
#
# st = round(time.time(), 17)
# a = get_nod(22, 9999)
# et = round(time.time(), 17)
# dt = round((st - et), 17)
# print(a, dt)

# def get_required(player,enemy):
#     if sum(player) > sum(enemy) + 5:
#         return "Auto-win"
#     elif sum(player) + 5 < sum(enemy):
#         return "Auto-lose"
#     elif sum(player) == sum(enemy):
#         return "Random"
#     elif sum(player) + 6 == sum(enemy) + 1:
#         return "Pray for a tie!"
#     elif sum(player) > sum(enemy):
#         return f"({7 - (sum(player)-sum(enemy))}..6)"
#     elif sum(player) < sum(enemy):
#         return f"(1..{5 - (sum(enemy) - sum(player))})"
#
#
# print(get_required([7, 1], [2, 0]))
# print(get_required([1, 0], [7, 1]))
# print(get_required([5, 0], [4, 1]))
# print(get_required([7, 0], [8, 1]))
# print(get_required([7, 2], [6, 8]))

# def binary_gcd(x, y):
#     if x == 0 and y == 0: return 0
#     elif x == 0: return str(bin(y)).count("1")
#     elif y == 0: return str(bin(x)).count("1")
#     elif min(x, y) < 0: return 1
#     else:
#         while min(x, y) != 0:
#             x, y = y, x % y
#         return str(bin(max(x, y))).count("1")
#
# z = binary_gcd(666666, 333111)
# print(z)

# def check_password(a, chars="$%!?@#"):
#     if len(a) < 8 :
#         return False
#     else:
#         return True
#
#
# x = check_password("12345678", chars="$%!?@#")
# print(x)

# def get_biggest_city(*args):
#     x = ""
#     for i in args:
#         if len(i) > len(x):
#             x = i
#     return x
#
#
# z = get_biggest_city("Питер", "Москва", "Самара", "Воронеж", "Воронец")
# print(z)

# def get_data_fig(*N, **parametrs):
#     x = ["type", "color", "closed", "width"]
#     s = tuple()
#     for i in x:
#         if i in parametrs:
#             s += (parametrs.get(i),)
#     per = (sum([i for i in N]),) + s
#     return per
#
#
# a = get_data_fig(4, 6, 12, 1, type=False, color=4, closd=True, width=6)
# print(a)

# a = ([[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]],)
#
#
# def is_isolate(seg):
#     seg = [str(el) for el in seg]
#     return False if "1, 1" in ", ".join(seg) else True
#
#
# def verify(*N):
#     answer = True
#     N2 = None
#     for i in N:
#         if not is_isolate(i):
#             answer = False
#             return answer
#
#     N2 = [[row[i] for row in N] for i in range(len(N[0]))]
#     for j in N2:
#         if not is_isolate(j):
#             answer = False
#             return answer
#     return answer
#
# z = verify([1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0])
# print(z)


# def is_isolate(i, j, N):
#     if sum([N[i][j], N[i][j+1], N[i+1][j], N[i+1][j+1]])>1 or sum([N[i][j], N[i][j-1], N[i+1][j], N[i+1][j-1]])>1:
#         return False
#     else:
#         return True
#
#
# def verify(*N):
#     N = list(N)
#     answer = True
#     for x in N:
#         print(x)
#     for i in range(len(N)-1):
#         for j in range(len(N)-1):
#             if N[i][j] == 1 or j == len(N[i])-2:
#                 if not is_isolate(i, j, N):
#                     answer = False
#                     break
#     return answer


# def is_isolate(i, j, N):
#     print(N)
#     y = j!=(len(N)-1)
#     x = j!=0
#     z = i!=(len(N)-1)
#     h = i!=0
#     return False if sum([N[i][j], y*N[i][j+y], x*N[i][j-x],
#                          z*N[i+z][j], z*y*N[i+z][j+y], z*x*N[i+z][j-x],
#                          h*N[i-h][j], h*y*N[i-h][j+y], h*x*N[i-h][j-x]]) > 1 else True
#
#
# def verify(*N):
#     answer = True
#     for i in range(len(N)):
#         for j in range(len(N)):
#             if N[i][j] == 1:
#                 if not is_isolate(i, j, N):
#                     answer = False
#                     return answer
#     return answer
#
#
# z = verify([1, 0, 0, 0, 0],
#            [0, 0, 1, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1])
# print(z)

#
# def str_min(a, b):
#     return a if a < b else b
#
#
# def str_min3(a, b, c):
#     return str_min(b, c) if a > b else str_min(a, c)
#
#
# def str_min4(a, b, c, d):
#     return str_min3(a, b, c) if str_min3(a, b, c) < d else d
#
#
# a, b, c, d = input(), input(), input(), input()
# print(str_min4(a, b, c, d))


# def get_rec_N(N):
#     if N > 1:
#         get_rec_N(N-1)
#     print(N)
#
# get_rec_N(3)


# def get_rec_sum(N):
#     if len(N) != 1:
#         N.append(N.pop()+N.pop())
#         get_rec_sum(N)
#         return N
#
#
# x = get_rec_sum([1,2,3])
# print(*x)

#
# def fib_rec(N, f=[]):
#     if len(f) == 0:
#         f += [1, 1]
#     else:
#         f.append(f[-2]+f[-1])
#     if len(f) >= N:
#         return f
#     else:
#         return fib_rec(N)
#
#
# print(fib_rec(7))


# здесь продолжайте программу
# def get_line_list(d, a=[]):
#     for i in d:
#         if type(i) != list:
#             a.append(i)
#         else:
#             get_line_list(i)
#     return a
#
#
# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
# print(get_line_list(d))


# def get_path(n):
#     if n > 1:
#         return get_path(n-1) + get_path(n-2)
#     else:
#         return 1
#
# print(get_path(3))


# d = list(map(int, input().split()))
#
# def slit(L, R):
#     A = [0] * len(L+R)
#     i = k = n = 0
#     while i < len(L) and k < len(R):
#         if L[i] < R[k]:
#             A[n] = L[i]
#             i += 1
#             n += 1
#         else:
#             A[n] = R[k]
#             k += 1
#             n += 1
#     while i < len(L):
#         A[n] = L[i]
#         i += 1
#         n += 1
#     while k < len(R):
#         A[n] = R[k]
#         k += 1
#         n += 1
#     return A
#
# def breaking(a):
#     if len(a) <= 1:
#         return
#     else:
#         x = len(a) // 2
#         L = a[:x]
#         R = a[x:]
#     breaking(L)
#     breaking(R)
#     A = slit(L, R)
#     for i in range(len(A)):
#         a[i] = A[i]
#     return a
#
# x = breaking(d)
# print(x)


# def get_filter(a, filter=None):
#     if filter is None:
#         return a
#
#     a = [i for i in a if filter(i)]
#     return a
#
#
# a = get_filter([0, -2, 14, 71, 24, 55, 15, 19, 11, 22, 0.1, 0.16, 93])
# print(a)


# x = float(input())
# # f = lambda x: abs(x)
# print((lambda x: abs(x))(x))



# def func_show(func):
#     def func_vsp(*args, **kwards):
#         res = func(*args, **kwards)
#         print(f"Площадь прямоугольника: {res}")
#     return func_vsp
#
# @func_show
# def get_sq(width, height):
#     s = width*height
#     return s
#
#
# get_sq(4, 7)


# def show_menu(func):
#     def circle(*args, **kwargs):
#         spis = func(*args, **kwargs)
#         for i in range(len(spis)):
#             print(f"{i+1}. {spis[i]}")
#     return circle
#
# @show_menu
# def get_menu(s):
#     spis = list(s.split())
#     return spis
#
#
# menu = input()
# get_menu(menu)


# s = input()
#
#
# def decor_sort(func):
#     def sorting(*args, **kwargs):
#         spis = func(*args, **kwargs)
#         return sorted(spis)
#     return sorting
#
#
# @decor_sort
# def get_list(s):
#     return list(map(int, s.split()))
#
#
# lst = get_list(s)
# print(*lst)


# s1 = input()
# s2 = input()
#
#
# def decor_v_slovar(func):
#     def vspom(*args, **kwargs):
#         s1, s2 = func(*args, **kwargs)
#         slov = {s1[i]:s2[i] for i in range(len(s1))}
#         return slov
#     return vspom
#
# @decor_v_slovar
# def v_spis(s1, s2):
#     s1 = list(s1.split())
#     s2 = list(s2.split())
#     return s1, s2
#
#
# d = v_spis(s1, s2)
# print(*sorted(d.items()))


# import time
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# s = input()
#
#
# def minus_defis(func):
#     def funccia(*args, **kwargs):
#         st = time.time()
#         s = func(*args, **kwargs)
#         while "--" in s:
#             s = s.replace("--", "-")
#         et = time.time()
#         dt = et - st
#         print(dt)
#         return s
#     return funccia
#
# @minus_defis
# def kir_lat(s):
#     s2 = ""
#     for i in s.lower():
#         if i in t:
#             s2 += t[i]
#         elif i in ": ;.,_":
#             s2 += "-"
#         else:
#             s2 += i
#     return s2
#
# print(kir_lat(s))


# s = input()
# #
# # def decor_s_parametrom(start=5):
# #     def plus_start(func):
# #         def wrapper(*args, **kwargs):
# #             res = func(*args, **kwargs) + start
# #             return res
# #         return wrapper
# #     return plus_start
# #
# #
# # @decor_s_parametrom()
# # def summa(s):
# #     sum_spis = sum(list(map(int, s.split())))
# #     return sum_spis
# #
# # s = summa(s)
# # print(s)


# s = input()
#
# def tags(tag="h1"):
#     def stroka(func):
#         def wrapper(*args, **kwargs):
#             return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
#         return wrapper
#     return stroka
#
#
# @tags()
# def st_lower(s):
#     return s.lower()
#
#
# print(st_lower(s))


# from functools import wraps
#
# s = input()
#
#
# def decor_sum(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         res = sum(func(*args, **kwargs))
#         return res
#     return wrapper
#
# @decor_sum
# def get_list(s):
#     '''Функция для формирования списка целых значений'''
#     s = list(map(int, s.split()))
#     return s
#
#
# print(get_list(s), get_list.__name__, get_list.__doc__)


# import pprint
# pprint.pprint(locals())

# piu = 4.9
# print(int(piu))

# a = 4
# b = True
# print(a+b)

# a = bool([])
# print(a)

# a = sum([1.1, 2.8, 3.9, 4])
# print(a)

# value_1 = -2.1
# value_2 = int(value_1)
# print(value_2)

# lst = list(range(1, 10, 2))
# print(lst)
# it = iter(lst)
# b = None
# while b != "end":
#     b = next(it, "end")
#     print(b)

# stroka = "abracadabra"
# st = sorted(stroka)
# print("".join(st))

# a = input()
# while True:
#     if a == "ko":
#         exit()
#     else:
#         a = input()

# sample = "маленькая змея Василиса говорит «с-с-с-с»!"
# print(sample[-500:1])

# sample = "маленькая змея Василиса говорит «с-с-с-с»!"
# print(len(sample[-1:-2]))

# sample = "маленькая змея Василиса говорит с-с-с-с!"
# sample = sample.title()
# sample = sample.lower()
# sample = sample.upper()
# print(sample)

# first_dict = {"a": "alpha", "b": "bravo"}
# second_dict = {"c": "charlie", "d": "delta"}
#
# my_dict = first_dict | second_dict
# print(my_dict)

# the_int = 0
# the_float = 0.0
# the_str = "-"
# the_bool = False
# the_list = [0]
# the_dict = {0:0}
#
# def the_change():
#    the_int = 1
#    the_float = 1.0
#    the_str = "+"
#    the_bool = True
#    the_list.append(1)
#    the_dict[1] = 1
#
# the_change()
#
# print(the_int)
# print(the_float)
# print(the_str)
# print(the_bool)
# print(the_list)
# print(the_dict)

# my_list = [0]
# my_list *= 10
# print(my_list)

# x = open('C://Users//sclop//PycharmProjects//pythonProject//data//text.txt')
# z = x.read()
# print(z.split())
# x.close()
#
# letters = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
#
#
# def get_first_element():
#   return letters[0]
#
#
# def get_last_element():
#   return letters[-1]
#
#
# def get_list_length():
#   return len(letters)
#
# # Не удаляйте код ниже, он нужен для проверки
#
# print(get_first_element())
# print(get_last_element())
# print(get_list_length())
#
# a = [1, 2, 3]
# a[0:2] = []
# print(a)

# a = [1, 2, 3, 4]
# a = reversed(a)     # возвращает итератор
# print(next(a))

# level_and_words = {
#     "легкий": {
#         "family": "семья",
#         "hand": "рука",
#         "people": "люди",
#         "evening": "вечер",
#         "minute": "минута",
#     },
#     "средний": {
#         "believe": "верить",
#         "feel": "чувствовать",
#         "make": "делать",
#         "open": "открывать",
#         "think": "думать",
#     },
#     "сложный": {
#         "rural": "деревенский",
#         "fortune": "удача",
#         "exercise": "упражнение",
#         "suggest": "предлагать",
#         "except": "кроме",
#     }
# }
#
# a = level_and_words.values()
# print(type(a))

# a = {
#     "rural": "деревенский",
#     "fortune": "удача",
#     "exercise": "упражнение",
#     "suggest": "предлагать",
#     "except": "кроме",
# }
# del a["rural"]
# print(a)

# a = input()
# b = []
# for i in range(3):
#     b.append(a[0] + a[1] + a[2])
#     b.append(a[0] + a[2] + a[1])
#     a = a[-1] + a[:-1]
# print(b)


# def words(letters, word=''):
#     letters or print(word)
#     for letter in letters:
#         words(letters - {letter}, word + letter)
#
#
# words(set('1234'))

# import sys
#
# socks = [int(sock.rstrip()) for sock in sys.stdin]
#
# print(('Дима', 'Анри')[(len(socks) - 1) % 2 == socks[-1] % 2])

# a = 4
# b = 4
# c = 1
# if a == b == c:
#     print('числа равны')
# else:
#     print('числа не равны')

# a = int(input())
# if not a in range(37):
#     print("ошибка ввода")
# elif a == 0:
#     print("зеленый")
# elif a in range(1, 11) or a in range(19, 29):
#     print(["красный", "черный"][a % 2 == 0])
# else:
#     print(["черный", "красный"][a % 2 == 0])


# a, b = ((int(input()), int(input())+1) for _ in range(2))
# inter_section = sorted(set(range(*a)) & set(range(*b)))
# if not inter_section:
#     print("пустое множество")
# elif len(inter_section) == 1:
#     print(*inter_section)
# else:
#     print(min(inter_section), max(inter_section))


# a, b, c = float(input()), float(input()), float(input())
# D = b ** 2 - (4 * a * c)
# print(*set([(-b + D ** 0.5) / (2 * a), (-b - D ** 0.5) / (2 * a)]) if D >= 0 else ["Нет корней"], sep="\n")


# from datetime import datetime
# print(datetime.now())


# a, b = 1, 1
# for i in range(int(input())):
#     print(a, end=" ")
#     a, b = b, b + a


# import os
# print(os.path.abspath("."))


# n = int(input())
# for i in range(1, n + 1):
#     x = list(range(1, i + 1))
#     print(* x, * x[-2::-1], sep="")


# with open("data.txt", "w+", encoding="UTF-8") as file:
#     file.write("Всё работает")
#     file.seek(0)
#     print(file.readline())


# with open("expenses.txt", "r") as file:
#     list_expenses = [int(line) for line in file]
#
# sum_expenses = sum(list_expenses)
# mean_expenses = sum_expenses / len(list_expenses)
# print(sum_expenses, mean_expenses)


# employees = {
# "...": {"f": "", "i": "", "o": "", "pass": "", "birthday": "","phone": "", "position": ""},
# }
#
# values_staff = [i for i in employees["..."]]
#
# staff = ["Киселёв / Всеволод / Эдуардович / 342 020 / 14 ноября 2001 года / +7 (908) 161-64-28 / главный инженер",
# "Довлатова / Эмилия /  Ефимовна / 342 000 / 18 мая 2001 года / +7 (924) 588-50-15 / технолог",
# "Аверин / Мартын / Егорович / 217 340 / 12 февраля 1981 года / +7 (933) 768-22-15 / технолог",
# "Князева / Августа / Егоровна / 320 021 / 2 июля 1984 года / +7 (965) 886-27-01 / расфасовщик",
# "Шанская / Аграфена / Семёновна / 116 404 / 7 июля 1982 года/ +7 (954) 940-47-96 / психолог для рыб"]
#
# staff = [[j.strip() for j in i.split("/")] for i in staff]
#
# for person in staff:
#     x = ((values_staff[i], person[i]) for i in range(len(values_staff)))
#     employees[person[0]] = dict(x)
#
# del employees["..."]
# print(employees)

# employees = [
#
#  {"fio": "Киселёв Всеволод Эдуардович ", "vaccinated": True},
#  {"fio": "Довлатова Эмилия Ефимовна", "vaccinated": False},
#  {"fio": "Аверин Мартын Егорович", "vaccinated": True},
#  {"fio": "Князева Августа Егоровна", "vaccinated": False},
#  {"fio": "Шанская Аграфена Семёновна", "vaccinated": True},
#  {"fio": "Куприна Марина Викторовна", "vaccinated": False},
#  {"fio": "Селезнёв Константин Игоревич", "vaccinated": False},
# ]
# vaccinated = []
# not_vaccinated = []
#
# for person in employees:
#   if person["vaccinated"] == True:
#     vaccinated.append(person["fio"])
#   else:
#     not_vaccinated.append(person["fio"])
#
# print("Вакцинированные:", *vaccinated, sep="\n")
# print("Остальные:", *not_vaccinated, sep="\n")

# import copy
# fish = [
#
# {"specie": "Белуга", "water": "fresh"},
# {"specie": "Карась", "water": "fresh"},
# {"specie": "Красноперка", "water": "fresh"},
#
# {"specie": "Морской окунь", "water": "sea"},
# {"specie": "Тунец", "water": "sea"},
# {"specie": "Скумбрия", "water": "sea"},
#
# ]
#
# sea_water = [i["specie"] for i in fish if i["water"] == "sea"]
# fresh_water = [i["specie"] for i in fish if i["water"] == "fresh"]
#
# print(f"Морские: {', '.join(sea_water)}")
# print(f"Пресноводные: {', '.join(fresh_water)}")
#
# fish_new = copy.deepcopy(fish)


# print("green %s and %s" % ("eggs", "wow"))

# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')


# print("Something were created")

# import requests

