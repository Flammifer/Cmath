from math import log
import numpy as np
step = 100000000
prt_sum = []
flag = 1
n = 0

while flag:
    n += 1
    tmp = 0
    for i in range(n*step, (n-1)*step, -1):
        tmp += 1/i
    prt_sum.append(tmp)
    en = 0
    for j in range(n-1, -1, -1):
        en += prt_sum[j]
    en -= log(n*step)
    print("Current approximation:", (en - 0.57721566490153286)/(0.577215664901532))
    if (en - 0.57721566490153286)/(0.577215664901532) < 10^10:
        flag = 0
