from scipy.stats import norm
from os import system
from math import sqrt
from os import system
system("cls")

#Задание 1
#Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800]. Найдите ее среднее значение и дисперсию.
a = 200
b = 800
print(
    f'На промежутке ({a}, {b}]\nСреднее значение: М(А) = {(a+b)/2: .0f}\nДисперсия: D(A) = {((b-a)**2)/12: .0f}')

#Задание 2
#О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2. 
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5? Если да, найдите ее.
a = 0.5
d = 0.2
b = a+(d*12)**(1/2)
print(f'Правая граница  В = {b: .3f}\n'
      f'Среднее значение В на промежутке ({a}; {b: .3f}) M(B) = {(b+0.5)/2: .3f}'
      )
#Задание 3
#Непрерывная случайная величина X распределена нормально и задана плотностью распределения f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)
#Найдите:
#а). M(X)
#б). D(X)
#в). std(X) (среднее квадратичное отклонение)
print('M(x) = a = -2 \n'
      'std(x) = 4 \n'
      'D(x) = std(x)^2 = 16 \n'
      )
#Задание 4
#Рост взрослого населения города X имеет нормальное распределение.
#Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
#Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
#а). больше 182 см
#б). больше 190 см
#в). от 166 см до 190 см
#г). от 166 см до 182 см
#д). от 158 см до 190 см
#е). не выше 150 см или не ниже 190 см
#ё). не выше 150 см или не ниже 198 см
#ж). ниже 166 см.
mu = 174
sigma = 8
a = 182
pa = 1-norm.cdf(a, mu, sigma)
print(f'>>> Вероятность роста больше {a} см = {pa: .4f}')
b = 190
pb = 1-norm.cdf(b, mu, sigma)
print(f'>>> Вероятность роста больше {b} см = {pb: .4f}')
v1, v2 = 166, 190
pv = norm.cdf(v2, mu, sigma)-norm.cdf(v1, mu, sigma)
print(f'>>> Вероятность роста от {v1} см до {v2} см = {pv: .4f}')
g1, g2 = 166, 182
pg = norm.cdf(g2, mu, sigma)-norm.cdf(g1, mu, sigma)
print(f'>>> Вероятность роста от {g1} см до {g2} см = {pg: .4f}')
d1, d2 = 158, 190
pd = norm.cdf(d2, mu, sigma)-norm.cdf(d1, mu, sigma)
print(f'>>> Вероятность роста от {d1} см до {d2} см = {pd: .4f}')
e1, e2 = 150, 190
pe = norm.cdf(e1, mu, sigma)+1-norm.cdf(e2, mu, sigma)
print(f'>>> Вероятность роста не выше {e1} см или не ниже {e2} см = {pe: .4f}')
yo1, yo2 = 150, 198
pyo = norm.cdf(yo1, mu, sigma)+1-norm.cdf(yo2, mu, sigma)
print(
    f'>>> Вероятность роста не выше {yo1} см или не ниже {yo2} см = {pyo: .4f}')
zh = 166
pzh = norm.cdf(zh, mu, sigma)
print(f'>>> Вероятность роста ниже {zh} см = {pzh: .4f}')
#Задание 5
#На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см, от математического ожидания роста в популяции, 
# в которой M(X) = 178 см и D(X) = 25 кв.см?
rost = 190
mx = 178
dx = 25
std = sqrt(dx)
sigma = (rost-mx)/std
print(
    f'Рост человека, равный {rost} см, отклоняется от математического ожидания роста в популяции на {sigma} сигм.')