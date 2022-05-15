from math import factorial
from math import pow
from math import exp
from math import sqrt
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from matplotlib import ticker
from prettytable import PrettyTable

var = 80  # номер варианта
a = pow(-1, var)*0.02*var
b = a+6
m = 1+int(np.log2(200))
step = (b-a)/m
print("Номер варианта:", var)
print("a =", a, "b =", b)
print("Число интервалов:", m)
print(a, a+8*step)


x = np.round(np.random.uniform(a, b, 200), 5)
xs = np.sort(x)
#print (xs)
print("---------- Неупорядоченная выборка ----------")
for k in range(len(x)):
    print(x[k])

print("---------- Упорядоченная выборка ----------")
for k in range(len(xs)):
    print(xs[k])

arr = [0]*10
for k in range(m+1):
    arr[k] = np.round(a + k*step, 5)
# интервалы

#  n[i]
n_i = [0]*(m)
for j in range(200):
    if (arr[0]<=x[j]<=arr[1]):
        n_i[0]+=1
for k in range(1, m):
    for j in range(200):
        if (arr[k]<x[j]<=arr[k+1]):
            n_i[k] += 1

#  w[i]
w_i = [0]*(m)
for k in range(m):
    w_i[k] = round(n_i[k]/200, 5)

print("Интервальный вариационный ряд:")
for k in range(m):
    print ("Интервал[", arr[k], ",", arr[k+1],"]: n_i =", n_i[k], "w_i =", w_i[k])
print ("sum(n_i) =", sum(n_i), " sum(w_i) =", sum(w_i))


print("Ассоцированный статический ряд")
x_i = [0]*m
for k in range(m):
    x_i[k] = np.round((arr[k]+arr[k+1])/2, 5)
    print ("x _", k, "* =", x_i[k], "n_i =", n_i[k], "w_i =", w_i[k])
print ("sum(n_i) =", sum(n_i), " sum(w_i) =", sum(w_i))

#  эмпирическая функция распределения
fig, sec = plt.subplots()
sec.xaxis.set_major_locator(ticker.MultipleLocator(1))
sec.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
for k in range(xs.size - 1):
    sec.plot([xs[k], xs[k+1]],[k/200, k/200], 'b')
plt.title("Функция эмпирического распределения")
plt.grid(True)
plt.show()

#  гистограмма относительных частот
fig, ox = plt.subplots()
for k in range(m):
    h = round(w_i[k] / step, 5)
    ox.plot([arr[k], arr[k]], [0, h], 'k')
    ox.plot([arr[k], arr[k+1]], [h, h], 'k')
    ox.plot([arr[k+1], arr[k+1]], [h, 0], 'k')
ox.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ox.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
plt.title("Гистограмма относительных частот")
plt.grid()
plt.show()

# выборочное среднее
vs = 0
for k in range(m):
    vs += x_i[k]*w_i[k]
vs = np.round(vs,5)
vs_ = np.round((a+b)/2,5)


# выборочная дисперсия с поправкой Шеппарда
vd = 0
for k in range (m):
    vd += ((x_i[k] - vs) ** 2) * w_i[k]
vd -= step**2 / 12
vd = np.round(vd, 5)
vd_ = np.round((b-a)**2/12, 5)

# выборочное среднее квадратическое отклонение
vsq_ = np.round((b-a)/(2*3**(1/2)), 5)
vsq = np.round(sqrt(vd), 5)

i = 0
for k in range(len(w_i)):
    if w_i[k] == max(w_i):
        i = k

# выборочная мода
vm_ = np.round((a+b)/2, 5)
vm = np.round(arr[i] + step * (w_i[i] - w_i[i-1]) / (2*w_i[i] - w_i[i-1] - w_i[i+1]), 5)
# выборочная медиана
md_ = np.round((a+b)/2, 5)
sum_w = 0
for i in range(len(w_i)):
    sum_w += w_i[i]
    if sum_w == 1 / 2:
        md = np.round(arr[i + 1], 5)
        break
    if sum_w > 1 / 2:
        md = np.round(arr[i] + step * (0.5 - sum_w + w_i[i - 1]) / w_i[i], 5)
        break

# выборочный коэффициент асимметрии и выборочный коэффициент эксцесса
vka_ = 0
vke_ = -6/5

mu1 = vs
mu2 = 0
mu3 = 0
mu4 = 0
for k in range(m):
    mu2 += ((x_i[k]) ** 2) * w_i[k]
    mu3 += ((x_i[k]) ** 3) * w_i[k]
    mu4 += ((x_i[k]) ** 4) * w_i[k]
mu3_0 = mu3 - 3 * mu2 * mu1 + 2 * mu1 ** 3
mu4_0 = mu4 - 4 * mu3 * mu1 + 6 * mu2 * mu1 ** 2 - 3 * mu1 ** 4

vka = np.round(mu3_0 / (vsq ** 3), 5)
vke = np.round((mu4_0 / (vsq ** 4)) - 3, 5)

table = PrettyTable()
table.field_names = ["Характеристика", "Экспериментальное зн", "Теоретическое зн", "Абс. откл.", "Отн. откл."]
table.add_row(["Выборочное среднее", vs, vs_, np.round(abs(vs-vs_),5), np.round(100*abs(vs-vs_)/vs_, 5)])
table.add_row(["Выборочная дисперсия", vd, vd_,  np.round(abs(vd-vd_),5), np.round(100*abs(vd-vd_)/vd_, 5)])
table.add_row(["Выборочное среднекв. откл", vsq, vsq_,  np.round(abs(vsq-vsq_),5), np.round(100*abs(vsq-vsq_)/vsq_, 5)])
table.add_row(["Выборочная мода", vm, vm_,  np.round(abs(vm-vm_),5), np.round(100*abs(vm-vm_)/vm_, 5)])
table.add_row(["Выборочная медиана", md, md_,  np.round(abs(md-md_),5), np.round(100*abs(md-md_)/md_, 5)])
table.add_row(["Выборочный коэф. асс.",vka, vka_,  np.round(abs(vka-vka_), 5), "—"])
table.add_row(["Выборочный коэф. асс.",vke, vke_,  np.round(abs(vke-vke_), 5), np.round(100*abs((vke-vke_)/vke_), 5)])

print(table)

