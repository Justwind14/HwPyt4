# 1. Вычислить число Пи c заданной точностью d
# Пример: 
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi
d = float(input("Задайте значение точности для π: "))
def calc_fract(d):
    count = 0
    while d % 1 != 0:
        d *= 10
        count += 1
    return count
if d == 10**(-1) or d == 10**(-2) or d == 10**(-3)\
or d == 10**(-4) or d == 10**(-5) or d == 10**(-6)\
or d == 10**(-7) or d == 10**(-8) or d == 10**(-9)\
or d == 10**(-10): 
    d_round = calc_fract(d)
    print(f'число π с заданной точностью {d} = {round(pi, d_round)}')
else:
    print('Число не соответствует условию:')