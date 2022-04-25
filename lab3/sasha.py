from math import factorial
from math import pow
from math import exp
from math import sqrt
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from matplotlib import ticker

a = 4.70
b = 9.32
m = 1+int(np.log2(200))
step = (b-a)/m
print("a =", a, "b =", b)
print("Число интервалов:", m)

#-------------------Выборка-------------------
x = [8.51149, 8.29295, 5.14167, 7.51340, 6.76633, 5.58015, 6.83550, 5.42791, 5.22127, 7.24661,
     4.95884, 6.91286, 6.96513, 6.03939, 5.98652, 7.09064, 6.22988, 8.52162, 5.81310, 8.78405,
     6.16729, 7.53934, 6.59479, 5.51798, 6.13476, 5.97320, 8.22066, 5.54903, 5.96579, 8.85127,
     8.24047, 7.18827, 5.03347, 6.22551, 6.16834, 7.91284, 6.94507, 6.80955, 7.34214, 5.03862,
     5.46720, 6.36768, 9.15001, 6.71400, 7.87661, 4.98978, 8.00138, 4.82027, 6.49873, 6.23702,
     5.12200, 8.23751, 6.17147, 7.90987, 5.26848, 5.53342, 4.76662, 9.15796, 8.96544, 8.51977,
     5.56737, 6.99691, 6.19526, 6.87817, 5.42471, 8.67525, 6.33150, 8.94898, 9.19296, 8.86994,
     4.74463, 5.20790, 9.29822, 4.83744, 6.19592, 7.63832, 6.02787, 7.26794, 5.38503, 6.25504,
     5.50663, 6.72136, 6.86095, 7.89779, 8.00576, 5.13231, 9.02409, 8.23818, 7.12026, 6.43106,
     5.92976, 5.55271, 7.43415, 5.31634, 5.34801, 7.82794, 7.04092, 8.64074, 6.07959, 5.21393,
     7.54631, 4.76494, 7.78856, 8.23495, 8.84562, 5.42505, 5.43566, 6.62768, 8.61317, 6.14557,
     7.78131, 5.76954, 6.31146, 9.23958, 6.83176, 7.72368, 4.89348, 7.27301, 7.10874, 8.07834,
     7.18060, 7.02856, 8.73183, 4.93122, 7.17284, 7.23146, 5.65719, 5.16906, 5.87114, 8.97071,
     9.10494, 6.38481, 5.02578, 5.82325, 7.59294, 6.27091, 5.79585, 8.64498, 7.22852, 8.65709,
     7.29718, 6.17750, 6.22323, 5.56568, 6.71102, 7.76070, 8.90821, 4.80731, 7.21041, 6.73125,
     9.30462, 7.49002, 7.42795, 5.54499, 4.84672, 4.89553, 6.78432, 7.91220, 8.44806, 7.57231,
     7.81685, 4.79095, 6.89086, 8.34241, 5.84125, 4.73904, 7.41545, 5.85944, 4.86997, 8.02959,
     5.44151, 8.80224, 9.12338, 4.96060, 8.53308, 6.43838, 5.70958, 9.11944, 7.11271, 5.15396,
     7.77443, 5.08167, 9.18448, 7.34454, 7.06927, 5.68499, 6.60672, 7.06094, 6.79887, 5.24255,
     6.88454, 8.42976, 6.60712, 8.11701, 6.13111, 8.52635, 7.31569, 8.49990, 6.73639, 8.51144]
print("Bыборка:")
print(x)

#-------------------Упорядоченная выборка-------------------
xs = np.sort(x)
print("Упорядоченная выборка")
print(xs)

arr = [0]*9
for k in range(m+1):
    arr[k] = np.round(a + k*step, 5)
print (arr)
#-------------------n_i-------------------
n_i = [0]*m
for j in range(200):
    if (arr[0] <= x[j] <= arr[1]):
        n_i[0] += 1
for k in range(1, m):
    for j in range(200):
        if (arr[k] < x[j] <= arr[k+1]):
            n_i[k] += 1

#-------------------w_i-------------------
w_i = [0]*m
for k in range(m):
    w_i[k] = round(n_i[k]/200, 5)

#-------------------x_i*-------------------
x_i = [0]*m
for k in range(m):
    x_i[k] = np.round((arr[k]+arr[k+1])/2, 5)

#-------------------Таблица 4.1-------------------
print("Таблица 4.1")
for k in range(m):
    print ("Интервал[", arr[k], ",", arr[k+1], "]:", "x _", k, "* =", x_i[k], "n_k =", n_i[k], "w_k =", w_i[k])
print ("sum(n_k) =", sum(n_i), "sum(w_k) =", sum(w_i))

#-------------------p*_k-------------------
p = 1/m

#-------------------|w_k-p*_k|-------------------
razn = [0]*m
for k in range(m):
    razn[k] = np.round(abs(w_i[k]-p), 5)

#-------------------N|w_k-p*_k|^2/p*_k=-------------------
hi2 = [0]*m
for k in range(m):
    hi2[k] = np.round(200*razn[k]*razn[k]/p, 5)
hi2kr = 14.1

#-------------------Таблица 4.2-------------------
print("Таблица 4.2")
for k in range(m):
    print("Интервал[", arr[k], ",", arr[k + 1], "]:", "w_k=", w_i[k], "p*_k =", p, "|w_k-p*_k|=", razn[k],
          "N|w_k-p*_k|^2/p*_k=", hi2[k])
print("sum(w_k) =", sum(n_i), "sum(p*_k) =", p*8, "max|w_k-p*_k|=", max(razn), "sum(N|w_k-p*_k|^2/p*_k)=", np.round(sum(hi2)))

#-------------------Проверка гипотезы-------------------
if np.round(sum(hi2)) <= hi2kr:
    print(f"{np.round(sum(hi2))} <= {hi2kr} Гипотеза НЕ ПРОТИВОРЕЧИТ экспериментальным данным")
else:
    print(f"{np.round(sum(hi2))} > {hi2kr} Гипотеза ПРОТИВОРЕЧИТ экспериментальным данным")

#-------------------Графики-------------------
fig, ox = plt.subplots()
for k in range(m):
    h = round(w_i[k] / step, 5)
    ox.plot([arr[k], arr[k]], [0, h], 'k')
    ox.plot([arr[k], arr[k+1]], [h, h], 'k')
    ox.plot([arr[k+1], arr[k+1]], [h, 0], 'k')
ox.plot([a, b], [1/abs(b-a), 1/abs(b-a)], 'r', linewidth=2)
ox.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ox.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
plt.title("Гистограмма относительных частот")
plt.grid()
plt.show()


#-------------------Задание 3.5-------------------

#-------------------График функции эмпирического распределения-------------------
fig, sec = plt.subplots()
sec.xaxis.set_major_locator(ticker.MultipleLocator(1))
sec.yaxis.set_major_locator(ticker.MultipleLocator(0.05))
for k in range(xs.size - 1):
    sec.plot([xs[k], xs[k+1]], [(k+1)/200, (k+1)/200], 'b', linewidth=1) #выборочная
sec.plot(xs, (xs-a)/(b-a), 'r', linewidth=1) #
plt.title("Функция эмпирического распределения")
plt.grid(True)
plt.show()

#-------------------D_N-------------------
DN = 0
x_ = 0
j = 0 #x*
for k in range(xs.size):
    buf =max(((k+1)/200 - (xs[k]-a)/(b-a)), (k/200 - (xs[k]-a)/(b-a)))
    if (buf > DN):
        DN = buf
        x_ = xs[k]
        j = k+1

#-------------------Таблиза 5.1-------------------

print("a=", a, "b=", b, "N=", 200, "D_N=", np.round(DN, 5), "DNsqrt(N)=", np.round(DN*np.sqrt(200), 5),
      "x*0=", x_, "F(x*)=", np.round((x_ - a)/(b-a), 5), "FN(x*)=", np.round(((j+1)/200), 5), "FN(x* - 0)=", np.round(j/200, 5))