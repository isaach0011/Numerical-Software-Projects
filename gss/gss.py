import numpy as np
import math
import sys

def f(x):
    return ((x ** 2) / 10) - (2 * math.sin(x))

def golden(func, left, right, tol):
    r = ((1+np.sqrt(5))/2) - 1
    d = r * (right-left)
    x1 = left + d
    f1 = func(x1)
    x2 = right - d
    f2 = func(x2)
    i = 1
    while True:
        if(f1 < f2):
            xopt = x1
            left = x2
            x2 = x1
            f2 = f1
            x1 = right - (x2 - left)
            f1 = func(x1)
        else:
            xopt = x2
            right = x1
            x1 = x2
            f1 = f2
            x2 = left + (right - x1)
            f2 = func(x2)
        if(xopt != 0):
            ea = (1 - r)*((right - left) / abs(xopt))
            if(ea < tol):
                break
        i += 1
    return xopt, f(xopt), i, i+2

def main():
    eps = sys.float_info.epsilon
    gss = golden(f, 0, 4, eps)
    print("The minimum is ", gss[1], " at x = ", gss[0], ".", sep='')
    print("Took", gss[2], "iterations with", gss[3], "function evaluations.")
        
if __name__ == "__main__":
    main() 