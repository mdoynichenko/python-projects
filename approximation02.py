# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math

def funct(t, y):
    return -t*y + 4*t/y

def approx_f(x, w_i, x_i, n):
    result = 0
    tmp_l = 1
    for i in range(0, n+1):
        tmp_l = 1
        for j in range(0, n+1):
            if i == j:
                continue
            tmp_l *= (x - x_i[j])
            tmp_l /= (x_i[i] - x_i[j])
        result += w_i[i]*tmp_l
    return result
        

    

a = 0
b = 1
y_0 = 1
h = 0.1
n = 0
k1 = 0
k2 = 0
k3 = 0
k4 = 0

tmp_t = a
w_i_tr = np.array([y_0])
w_i_h = np.array([y_0])
w_i_st = np.array([y_0])
w_i_rk = np.array([y_0])
x_i = np.array([a])
pl_x = np.array([a])
pl_y = np.array([y_0])

"""
трапеции
"""
while(tmp_t < b):
    w_i_tr = np.append(w_i_tr, w_i_tr[n] + h*(funct(tmp_t, w_i_tr[n]) + funct(tmp_t+h, w_i_tr[n]+ h*funct(tmp_t, w_i_tr[n])))/2)
    n+=1
    tmp_t+=h
    x_i = np.append(x_i, tmp_t)
    
"""
метод Хойна
"""
tmp_t = a
n = 0

while(tmp_t < b):
    w_i_h = np.append(w_i_h, w_i_h[n] + h*(funct(tmp_t, w_i_h[n]) + 3*funct(tmp_t + 2*h/3, w_i_h[n]+ 2*h*funct(tmp_t, w_i_h[n])/3))/4)
    n+=1
    tmp_t+=h
    
    
"""
метод средней точки
"""

tmp_t = a
n = 0

while(tmp_t < b):
    w_i_st = np.append(w_i_st, w_i_st[n] + h*(funct(tmp_t + h/2, w_i_st[n] + h*funct(tmp_t,  w_i_st[n])/2 ) ))
    n+=1
    tmp_t+=h


"""
метод Рунге Кутта четвертого порядка
"""

tmp_t = a
n = 0

while(tmp_t < b):    
    k1 = funct(tmp_t, w_i_rk[n])
    k2 = h*funct(tmp_t + h/2, w_i_rk[n] + k1/2)
    k3 = h*funct(tmp_t + h/2, w_i_rk[n] + k2/2)
    k4 = h*funct(tmp_t + h, w_i_rk[n] + k3)
    
    w_i_rk = np.append(w_i_rk, w_i_rk[n] + (k1 + 2*k2 + 3*k3 + k4)/6)
    
    n+=1
    tmp_t+=h
        
lag = 0.01
x = np.arange(a, b, lag)
y_tr = approx_f(x, w_i_tr, x_i, n)
y_h = approx_f(x, w_i_h, x_i, n)
y_st = approx_f(x, w_i_st, x_i, n)
y_rk = approx_f(x, w_i_rk, x_i, n)
y_f = np.array([math.sqrt(4 - 3*math.exp(-x[0]*x[0]))])
tmp_x = a+lag
while tmp_x <= b:
    y_f = np.append(y_f, math.sqrt(4 - 3*math.exp(-tmp_x*tmp_x)))
    tmp_x+=lag
    

fig, ax = plt.subplots()

ax.plot(x, y_f, linewidth  = 9, color = 'black')
ax.plot(x, y_rk, linewidth  = 7, color = 'blue')
ax.plot(x, y_st, linewidth  = 5, color = 'yellow')
ax.plot(x, y_h, linewidth  = 3, color = 'green')
ax.plot(x, y_tr, linewidth  = 1, color = 'red')

plt.grid(True)

fig.set_figwidth(12)
fig.set_figheight(6)
fig.set_facecolor('linen')
ax.set_facecolor('ivory')

plt.show()

print("метод трапеций")
print(w_i_tr)
print("метод Хойна")
print(w_i_h)
print("метод средней точки")
print(w_i_st)
print("метод Рунге-Кутты")
print(w_i_rk)
print(x_i)

