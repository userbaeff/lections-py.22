# # тип данных int()

# number = 5 #number - переменная

# # +
# a = 10
# b = 5
# result = a + b
# print(result)
# print (a + 100)

# # / and //
# # 5 / 2 = 2.5 -> (float)
# # 5 // 2 = 2 -> целочисленное деление

# num1 = 25
# num2 = 12
# print(num1 / num2)
# print(num1 // num2)

# # % -> деление при котором мы получим остаток
# a = 9
# b = 7
# result = a % b
# print(result)


# ** -> возведение в степень
# 5 ** 4 = 625
# 5 ** 2 = 5 * 5 = 25
# print(4 ** 4)
# pow(a, b)
# a = 5
# b = 3
# result = pow(a, b)
# print(result)


# round() - округление числа c плавающей точкой

# a = 5.5655
# result = round(a, 1)
# print(result)

# # abs() - абсолюттное значение abs(-5) -> 5
# a = abs(-16)
# print(a)

#divmod (a, b) -> она выводит два числа, первое число это результат целочисленного деления (//) a на b. 
#второе число это мольное деление (%) a на b

# result = divmod(5, 2)
# print(result)

# import math
# import string

# a = 5
# print(math.sqrt(a))


# num = 6
# num = "string"
# print(num)
# print(type(num))

# str1 = "Hello world"
# num = 5
# print(str1 * num)

# num = 5
# str1 = "20"
# print(str1 + str(num))
# num2 = int(str1)
# print(type(num2))


# var = input()
# print(var)
# print(type(var))

# num1 = int(input("Vvedite chislo: "))
# num2 = int(input("Vvedite stepen: "))
# print(num1 ** num2)
# print(pow(num1, num2))

# from random
# from random import randint
# num = randint(0, 2)
# print (num)


# from random import randint
# name = input('Vvedite Imya: ')
# last_name = input('Vvedite familiyu: ')
# result = name + last_name + str(randint(650, 1000))
# print(result)
# from random import randint 
# num = str(randint(0, 5000))
# num = set(num)
# num = "".join(num)
# print(num)


# a = 1
# b = a
# print(id(a))
# print(id(b))


