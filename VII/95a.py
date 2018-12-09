import MyMath as mm
import numpy as np

x = [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]
y = [1, 0.989616, 0.958851, 0.908852 , 0.841471, 0.759188 , 0.664997, 0.562278 , 0.454649]
print(mm.int_trapeze(x, y))
print(mm.int_simpson(x, y))
print(mm.int_rich(x, y))
