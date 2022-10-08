# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


n = 0
while(n <=7):
    comb = [int(i) for i in str(f'{n:03b}')]
    print('X = ', comb[0], 'Y = ', comb[1], 'Z =', comb[2])
    if (not(comb[0] or comb[1] or comb[2]) == (not(comb[0]) and not (comb[1]) and not(comb[2]))):
       print(True)
    else: print (False)
    n += 1