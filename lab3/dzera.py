from math import factorial
from math import pow
from math import exp
from math import sqrt
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from matplotlib import ticker

a = 4.50
b = 9.36
m = 1+int(np.log2(200))
step = (b-a)/m
print("a =", a, "b =", b)
print("Число интервалов:", m)

#-------------------Выборка-------------------
x = [5.70339, 7.84887, 5.42523, 8.54804, 6.87707, 6.62098, 9.28939, 8.75147, 6.94157, 4.86294,
     8.84928, 7.48809, 8.77307, 9.32906, 8.56796, 8.47115, 7.60901, 4.63747, 7.00777, 8.14863,
     5.71434, 8.56147, 9.05490, 5.43779, 5.19610, 8.94430, 6.09532, 5.00918, 7.67327, 6.86710,
     5.39721, 8.85917, 5.79475, 7.97973, 7.43244, 6.71350, 5.19023, 6.69493, 8.70748, 9.26014,
     6.78215, 6.84276, 8.50339, 7.85329, 6.52863, 5.26711, 8.39677, 5.18140, 7.25659, 6.87353,
     7.98373, 4.52670, 8.23022, 6.10741, 9.08757, 8.35725, 5.39218, 8.84492, 8.30697, 4.88358,
     6.53037, 4.94562, 6.00744, 7.26083, 9.12161, 6.87128, 8.84847, 5.18339, 6.73640, 7.93852,
     7.59503, 5.36761, 8.44723, 5.81177, 9.24067, 7.11600, 5.58049, 7.01017, 8.35807, 4.67015,
     8.02098, 5.64329, 6.18894, 7.80691, 7.47821, 8.19758, 7.99240, 5.03401, 7.24841, 5.52290,
     7.74251, 6.77568, 4.58836, 6.39781, 8.21054, 8.62249, 6.59204, 6.64075, 4.71727, 5.79918,
     6.63346, 6.58624, 4.79966, 7.37612, 5.78260, 7.06297, 7.54590, 6.11783, 9.19707, 5.35707,
     5.98373, 8.15589, 4.93245, 8.80728, 6.93214, 4.91063, 4.90893, 5.46386, 4.68934, 9.11463,
     5.01796, 8.44684, 8.06467, 4.58027, 8.14036, 9.04122, 5.53841, 7.64856, 9.34265, 8.65600,
     8.12485, 8.32936, 8.67192, 8.51581, 8.19243, 6.82526, 5.19133, 5.37359, 5.32601, 8.96965,
     7.28802, 8.84002, 9.30292, 8.03993, 8.01716, 8.97801, 8.02075, 4.61459, 6.00452, 7.42820,
     4.52110, 6.90227, 8.28802, 8.05350, 7.96746, 6.70383, 7.38678, 6.72021, 7.79314, 9.26977,
     6.52670, 8.14331, 5.59950, 6.14370, 7.99581, 7.54557, 7.79887, 4.82944, 6.97182, 8.67699,
     7.36273, 8.47120, 5.70700, 4.72263, 8.93674, 5.07430, 8.31239, 8.64716, 6.33299, 8.36847,
     5.03889, 4.67828, 6.98437, 8.18440, 7.68916, 6.01722, 6.46126, 6.71932, 7.30581, 8.06308,
     5.03455, 5.78662, 7.72993, 8.99259, 6.36744, 8.49870, 6.39226, 8.88214, 6.83462, 7.58688]
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
    buf =max(abs((k+1)/200 - (xs[k]-a)/(b-a)), abs(k/200 - (xs[k]-a)/(b-a)))
    if (buf > DN):
        DN = buf
        x_ = xs[k]
        j = k+1

#-------------------Таблиза 5.1-------------------

print("a=", a, "b=", b, "N=", 200, "D_N=", np.round(DN, 5), "DNsqrt(N)=", np.round(DN*np.sqrt(200), 5),
      "x*0=", x_, "F(x*)=", np.round((x_ - a)/(b-a), 5), "FN(x*)=", np.round(((j)/200), 5), "FN(x* - 0)=", np.round((j-1)/200, 5))