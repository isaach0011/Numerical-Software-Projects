"""
Project: Module 5 - Programming Assignment: Regula Falsi
Author: Isaac Hill
Class: CS3320-001
"""
import sys
import math

def functionOne(x):
    return (x ** 4) - (6 * x ** 3) + (12 * x ** 2) - (10 * x) + 3
    
def functionTwo(x):
    return (x ** 3) - (7 * x ** 2) + (15 * x) - 9 

def regulaFalsi(xLower, xUpper, func):
    maxIter = 100000
    root = 0
    iterations = 0
    e = sys.float_info.epsilon
    
    #If [xLower, xUpper] doesn't bracket a root
    if(func(xLower) * func(xUpper) > 0):
        flag = -1
        return root, flag, 0, iterations
    
    #If xLower or xUpper is the root
    if(func(xLower) == 0 or func(xUpper) == 0):
        if(func(xLower) == 0):
            root = xLower
        else:
            root = xUpper
        flag = 0
        return root, flag, func(root), iterations
    
    for i in range(maxIter):
        prevRoot = root
        
        #root caculation with Regula Falsi function
        root = xLower - func(xLower) * (xUpper - xLower) / (func(xUpper) - func(xLower))
        iterations += 1
        
        #Break Conditions
        if(abs(func(root)) < e):
            break
        if(abs(root - prevRoot) < math.ulp(root)): #May need python 3.9+ for ulp
            break
        
        #Bracket Adjustment
        if(func(xLower) * func(root) > 0):
            xLower = root
        else:
            xUpper = root
            
    
    flag = 0
    return root, flag, func(root), iterations

def main():
    lower = 2.5             #Lower Bounds
    upper = 3.5             #Upper Bounds
    function = functionOne  #Function to use
    
    rf = regulaFalsi(lower, upper, function)

    print("Bracket [{}, {}]".format(lower, upper))
    print("--------------------------")
    
    #Check Flag
    if(rf[1] == -1):
        print("Flag:", rf[1], "- No root found at given bounds.\n")
    else:
        print("Flag:", rf[1], "- Root Found")
        print("Root =", rf[0])
        print("Function at root =", rf[2])
        print("Iterations =", rf[3], "\n")
        
if __name__ == "__main__":
    main()