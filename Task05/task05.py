# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# Если вы не знаете как вычислить квадратный корень, оставьте квадрат расстояния


import math

# 1st solution (please, comment out solution, which you're not checking at the moment)

a_x = int(input('Введите значение Х для точки А: '))
a_y = int(input('Введите значение Y для точки А: '))

b_x = int(input('Введите значение Х для точки B: '))
b_y = int(input('Введите значение Y для точки B: '))

ab_dist = math.sqrt((b_x - a_x)**2 - (b_y - a_y)**2)
print(round((ab_dist), 2))

# 2nd solution (please, comment out solution, which you're not checking at the moment)

a_x = int(input('Введите значение Х для точки А: '))
a_y = int(input('Введите значение Y для точки А: '))

a = [a_x, a_y]

b_x = int(input('Введите значение Х для точки B: '))
b_y = int(input('Введите значение Y для точки B: '))

b = [b_x, b_y]

ab_dist = math.dist(a , b)
print(round((ab_dist), 2))