from math import log
import numpy as np
step = 100000000
prt_sum = np.array([])
flag = 1
n = 0

en = 0
C = 0
while flag:
    n += 1
    tmp = 0
    C += 1/n
    if (n % step == 0):
        en = C - log(n)
        print("Current approximation:", (en - 0.57721566490153286)/(0.577215664901532))
        if (abs((en - 0.57721566490153286)/(0.577215664901532)) < 10**(-10)):
            flag = 0

print(en)
