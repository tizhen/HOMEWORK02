# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть.
# Пример:

# 5 -> 1 0 1 1 0
# 2

# coins = [0, 1, 1, 1, 0]
# if coins.count(0) < coins.count(1):
#     print(coins.count(0))
# else: 
#     print(coins.count(1))

from random import randint

k = 5
list_coins = []
for i in range(k):
    list_coins.append(randint(0, 1))
print(list_coins)
if list_coins.count(0) < list_coins.count(1):
    print(list_coins.count(0))
else: 
    print(list_coins.count(1))