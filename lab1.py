from math import factorial
from math import exp
from math import sqrt
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from matplotlib import ticker
from prettytable import PrettyTable

v = 80  # номер варианта
lam = round(0.8 + v * 0.02, 5)  # параметр лямбда, пуассоновского распределения

random.seed(10)

x = np.random.poisson(lam, 200)  # генерация выборки
print("Выборка")
print(x)
xs = np.sort(x)  # сортировка полученной выборки
print("Упорядоченная выборка")
print(xs)

# построение статистического ряда
arr = np.unique(xs, return_counts=True)
x_i = arr[0]
n_i = arr[1]
w_i = [i for i in range(x_i.size)]
for k in range(arr[0].size):
    w_i[k] = round(n_i[k]/200, 5)
s_i = [i for i in range(x_i.size)]
s_i[0] = w_i[0]
for k in range(1, arr[0].size):
    s_i[k] = s_i[k-1]+w_i[k]

table = PrettyTable()
table.add_column("x_i", x_i)
table.add_column("n_i", n_i)
table.add_column("w_i", w_i)
table.add_column("s_i", s_i)
table.add_row([" ", np.sum(n_i), np.sum(w_i), " "])

print("Статитистический ряд:")
print (table)

# полигон относительных частот
fig, fir = plt.subplots()
fir.xaxis.set_major_locator(ticker.MultipleLocator(1))
fir.yaxis.set_major_locator(ticker.MultipleLocator(0.1))

p_i = [i for i in range(x_i.size)]
for k in range(x_i.size):
    p_i[k] = lam**(x_i[k])/factorial(k)*exp((-1)*lam)

fir.plot(x_i, w_i, 'b')
fir.plot(x_i, p_i, 'r')
plt.title("Полигон относительных частот")
plt.grid(True)


# график функции эмпирического распределения
fig, sec = plt.subplots()
sec.xaxis.set_major_locator(ticker.MultipleLocator(1))
sec.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
for k in range(x_i.size - 1):
    sec.plot([x_i[k], x_i[k+1]], [s_i[k], s_i[k]], 'b')
plt.title("Функция эмпирического распределения")
plt.grid(True)
plt.show()

# выборочное среднее
vs = sum(x_i*w_i)
print("Выборочное среднее ", round(vs, 5))

# выборочная дисперсия
vd = 0
for k in range(x_i.size):
    vd += (x_i[k]-vs)**2*w_i[k]
print("Выборочная дисперсия ", round(vd, 5))

# выборочное среднеквадратическое отклонение
vsq = sqrt(vd)
print("Выборочное среднеквадратическое отклонение ", round(vsq, 5))

# выборочная мода
max_w = max(w_i)
flg = 0
vm = 0
for k in range(x_i.size):
    if (w_i[k] == max_w):
        if flg > 0 and w_i[k] == w_i[k-1]:
            print("Выборочная мода не существует!")
            break
        vm += x_i[k]
        flg += 1
vm = vm/flg
print("Выборочная мода ", round(vm, 5))

# выборочная медиана
for k in range(x_i.size):
    if k == 0:
        if s_i[k] > 0.5:
            print("Выборочная медиана", round(x_i[k], 5))
            break
        if s_i[k] == 0.5:
            print("Выборочная медиана", (round(x_i[k]+x_i[k+1])/2, 5))
            break
    if (s_i[k] > 0.5) and (s_i[k-1] < 0.5):
        print("Выборочная медиана",  round(x_i[k], 5))
    if s_i[k] == 0.5:
        print("Выборочная медиана", (round(x_i[k]+x_i[k+1])/2, 5))
        break

# выборочный коэффициент асимметрии и выборочный коэффициент эксцесса
mu1 = vs
mu2 = 0
mu3 = 0
mu4 = 0
for k in range(x_i.size):
    mu2 += ((x_i[k]) ** 2) * w_i[k]
    mu3 += ((x_i[k]) ** 3) * w_i[k]
    mu4 += ((x_i[k]) ** 4) * w_i[k]
mu3_0 = mu3 - 3 * mu2 * mu1 + 2 * mu1 ** 3
mu4_0 = mu4 - 4 * mu3 * mu1 + 6 * mu2 * mu1 ** 2 - 3 * mu1 ** 4

vka = mu3_0 / (vsq**3)
vke = mu4_0 / (vsq**4) - 3
print("Выборочный коэффициент асимметрии", round(vka, 5))
print("Выборочный коэффициент эксцесса", round(vke, 5))



