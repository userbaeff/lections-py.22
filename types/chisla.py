# тип данных int()

number = 5 #number - переменная

# +
a = 10
b = 5
result = a + b
print(result)
print (a + 100)

# / and //
# 5 / 2 = 2.5 -> (float)
# 5 // 2 = 2 -> целочисленное деление

num1 = 25
num2 = 12
print(num1 / num2)
print(num1 // num2)

# % -> деление при котором мы получим остаток
a = 9
b = 7
result = a % b
print(result)


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

a = 5.5655
result = round(a, 1)
print(result)

# abs() - абсолюттное значение abs(-5) -> 5
a = abs(-16)
print(a)

#divmod (a, b) -> она выводит два числа, первое число это результат целочисленного деления (//) a на b. 
#второе число это мольное деление (%) a на b

result = divmod(5, 2)
print(result)

import math

a = 5
print(math.sqrt(a))