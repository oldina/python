#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания 
#все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
#m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

list_n = []
list_m = []
list_itog = []
n=int(input("Введите количество элементов первого множества "))
while n>0:
    number_1 = input("Введите элементы первого множества ")
    list_n.append(int(number_1))
    n -=1
list_n_u = list(set(list_n))
list_n_u.sort()
m=int(input("Введите количество элементов второго множества "))
while m>0:
    number_2 = input("Введите элементы второго множеатва ")
    list_m.append(int(number_2))
    m -=1    
list_m_u = list(set(list_m))
list_m_u.sort()
for i in range(len(list_n_u)):
    if list_n_u[i] in list_m_u:
       list_itog.append(list_n_u[i])
print(list_itog)

#В фермерском хозяйстве Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
#Таким образом, у каждого куста есть ровно 2 соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью,
#поэтому ко времени сбора урожая на них выросло различное число ягод - на i-том кусте выросло ai ягод. В этом фермерском хозяйстве
#внедрена система автоматического сбора черники. Система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий
#модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед
#некоторым кустом
from random import randint
gryadka = list(randint(2, 8) for i in range(int(input("Введите кол-во кустов на грядке: "))))
print(gryadka)
k = int(input("Введите номер куста с которого нужно собрать ягоды: "))
res = 0
if k == 1:
    res = gryadka[0] + gryadka[1] + gryadka[-1]
elif k == len(gryadka):
    res = gryadka[-2] + gryadka[-1] + gryadka[0]
else:
    res = gryadka[k-1] + gryadka[k-2] + gryadka[k]
print(res) 