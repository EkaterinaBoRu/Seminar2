"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть"""
#надо найти чего больше и их количество- решек или с гербом монет (0 или 1). из n вычесть это значение. столько переворотов нужно будет осуществить

from random import randint

n= int(input("Введите количество монет (положительное число): "))

count_0 = 0
count_1 = 0

for i in range(n):
    tempr=randint(0,1)
    print(tempr)
    if tempr>0:
        count_1 +=1
    else:
        count_0 +=1
print("Нужно перевернуть монет:")

if count_0>count_1:
    print (n-count_0)
else:
    print (n-count_1)


