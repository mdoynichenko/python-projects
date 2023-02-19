# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def funct(t, y):
    return 1 + y/t

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
        

    

a = 1
b = 2
y_0 = 2
h = 0.25
n = 0

tmp_t = a
w_i = np.array([y_0])
x_i = np.array([a])
pl_x = np.array([a])
pl_y = np.array([y_0])


while(tmp_t < b):
    w_i = np.append(w_i, w_i[n] + funct(tmp_t, w_i[n]))
    n+=1
    tmp_t+=h
    x_i = np.append(x_i, tmp_t)

    
"""
for i in range(0, 11):
    pl_x = np.append(pl_x, a + (b-a)*i/100)
    pl_y = np.append(pl_y, approx_f(a+(b-a)*i/100, w_i, x_i, n))
    
"""

lag = 0.01
x = np.arange(1.0, 2.0, lag)
y = approx_f(x, w_i, x_i, n)
fig = plt.figure()
plt.plot(x, y)
plt.grid(True)



plt.show()

print(w_i)
print(x_i)

