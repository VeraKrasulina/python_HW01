# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите значение Х: '))
y = int(input('Введите значение Y: '))


if (x > 0 and y > 0):
    print('Точка находится в первой четверти координат.')
elif (x < 0 and y > 0):
    print('Точка находится во второй четверти координат.')
elif (x < 0 and y < 0):
    print('Точка находится в третьей четверти координат.')
elif (x > 0 and y < 0):
    print('Точка находится в четвертой четверти координат.')
else: print('Значения Х и Y введены неверно')