# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# Пример:

# 4 4 -> 2 2
# 5 6 -> 2 3


# sum = x + y
# mult = x*y
# x = sum - y
# y*(sum - y)-mult = 0
# y**2 - sum*y + mult = 0

# import math
 
# print("Введите коэффициенты для уравнения")
# print("ax^2 + bx + c = 0:")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
 
# discr = b ** 2 - 4 * a * c
# print("Дискриминант D = %.2f" % discr)
 
# if discr > 0:
#     x1 = (-b + math.sqrt(discr)) / (2 * a)
#     x2 = (-b - math.sqrt(discr)) / (2 * a)
#     print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
# elif discr == 0:
#     x = -b / (2 * a)
#     print("x = %.2f" % x)
# else:
#     print("Корней нет")


s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))
d = s*s - 4*p
if d > 0:
    print(round((s-d)/2),round((s+d)/2))
elif d == 0:
    print(round(s/2),round(s/2))
else:
    print("Решений нет")