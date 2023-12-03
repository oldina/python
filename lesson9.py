import numpy as np
import matplotlib.pyplot as plt
#Задача 1
#Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], 
#ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. Используя математические операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату 
#(то есть, zp - признак), а за y - значения скорингового балла (то есть, ks - целевая переменная). Произвести расчет как с использованием intercept, так и без.
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
plt.scatter(zp, ks)
plt.xlabel('ЗП заемщиков')
plt.ylabel('Поведенческий кредитный скоринг', rotation = 90)
plt.show()
b = (np.mean(zp * ks) - np.mean(zp) * np.mean(ks)) / (np.mean(zp ** 2) - np.mean(zp) ** 2)
print(b)
a = np.mean(ks) - b * np.mean(zp)
print(a)
plt.scatter(zp, ks)
plt.plot(zp, a + b * zp, c = 'r')
plt.xlabel('ЗП заемщиков')
plt.ylabel('Поведенческий кредитный скоринг', rotation = 90)
plt.show()
#Задача 2
#Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).
def mse(b, x, y):
    return np.sum((b * x - y) ** 2) / len(x)
print(mse(b, zp, ks))
def mse_p(b,x,y):
    return (2 / len(x)) * np.sum((b * x - y) * x)
alpha = 1e-6
b = 0.1
mse_min = mse(b, zp, ks)
i_min = 1
b_min = b
iter = 10000
for i in range(iter):
    b -= alpha * mse_p(b, zp, ks)
    if i % 100 == 0:
        print(f'>>> Итерация #{i}, b={b}, mse={mse(b, zp, ks)}')
    if mse(b, zp, ks) > mse_min:
        print(f'>>> Итерация #{i_min}, b={b_min}, mse={mse_min},\n>>> Достигнут min\n>>> Получили {b_min} ')
        break
    else:
        mse_min = mse(b,zp,ks)
        i_min = i
        b_min = b
#Задача 3
#Произвести вычисления как в пункте 2, но с вычислением intercept. Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно
# (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).
def mse_ab(a,b, x, y):
    return np.sum(((a + b * x)-y) ** 2) / len(x)
def mse_pa(a, b, x, y): 
    return 2 * np.sum((a + b * x) - y) / len(x)
def mse_pb(a, b, x, y):
    return 2 * np.sum(((a + b * x) - y) * x) / len(x)
alpha = 3e-5
b = 0.1
a = 0.1
mseab_min = mse_ab(a, b, zp, ks)
i_min = 1
b_min = b
a_min = a
iter = 1000000   
for i in range(iter):
    a -= alpha * mse_pa(a, b, zp, ks)
    b -= alpha * mse_pb(a, b, zp, ks)
    if i % 50000 == 0:
        print(f'>>> Итерация #{i}, a={a}, b={b}, mse={mse_ab(a, b, zp, ks)}')
    if mse_ab(a, b, zp, ks) > mseab_min:
        print(f'>>> Итерация #{i_min}, a={a_min}, b={b_min}, mse={mseab_min},\nДостигнут min.')
        break
    else:
        mseab_min = mse_ab(a, b, zp, ks)
        i_min = i
        b_min = b
        a_min = a
print(f'>>> a = {a_min}\n>>> b = {b_min}')
plt.scatter(zp, ks)
plt.plot(zp, a_min + b_min * zp, c = 'r')
plt.xlabel('ЗП заемщиков')
plt.ylabel('Поведенческий кредитный скоринг', rotation = 90)
plt.show()
