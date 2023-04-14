"""
Project: Module 2 - Programming Assignment: ulps
Author: Isaac Hill
Class: CS3320-001
"""
import sys 
import math

base = sys.float_info.radix 
eps = sys.float_info.epsilon 
prec = sys.float_info.mant_dig 
inf = math.inf

def ulps(x, y):
    #If x or y are 0 or infinite or one has a difference sign than the other, return inf
    if(x == 0 or y == 0 or x == inf or y == inf or (x > 0 and y <= 0) or (x <= 0 and y > 0)):
        return inf
    if(x < 0 and y < 0): #If both negative, take the absolute value of both
        x = abs(x)
        y = abs(y)
    
    if(x > y): #If x is greater than y, swap their places
        tempNum = x
        x = y
        y = tempNum
    
    result = 0
    
    #Calculates x glb, lub, and exponent
    xExp = 0
    xLub = 1
    while(xLub <= x):
        xLub *= base
        xExp += 1
    if(xLub > x):
        xGlb = xLub / 2
        xExp -= 1
    if(xGlb > x):
        xLub = xGlb
        xGlb = xGlb / 2
        xExp -= 1
    
    #Calculates y glb, lub, and exponent
    yExp = 0
    yLub = 1
    while(yLub <= y):
        yLub *= base
        yExp += 1
    if(yLub > y):
        yGlb = yLub / 2
        yExp -= 1
    if(yGlb > y):
        yLub = yGlb
        yGlb = yGlb / 2
        yExp -= 1
    
    if(xExp == yExp): #If they are the same exponent
        result = int((y - x) / (eps * (2 ** xExp)))
    else:
        xInterval = (eps * (2 ** xExp))
        yInterval = (eps * (2 ** yExp))
        xResult = (xLub - x) / xInterval
        yResult = (y - yGlb) / yInterval
        if(xExp == (yExp - 1)):  #If they are one exponent apart
            result = int(xResult) + int(yResult)
        else:  #If they are more than one exponent apart
            midCount = 0
            expInbetween = ((yExp - xExp) - 1)
            while(expInbetween > 0): #For each exponent inbetween x and y, get the count of intervals
                midExp = xExp + expInbetween
                midGlb = 2 ** midExp
                midLub = 2 ** (midExp + 1)
                midInterval = (eps * (2 ** (xExp + expInbetween)))
                midCount += (midLub - midGlb) / midInterval
                expInbetween -= 1
            result = int(xResult) + int(midCount) + int(yResult)
    return result

def main():  
    print(ulps(-1.0, -1.0000000000000003)) 
    print(ulps(1.0, 1.0000000000000003)) 
    print(ulps(1.0, 1.0000000000000004)) 
    print(ulps(1.0, 1.0000000000000005))   
    print(ulps(1.0, 1.0000000000000006)) 
    print(ulps(0.9999999999999999, 1.0)) 
    print(ulps(0.4999999999999995, 2.0)) 
    print(ulps(0.5000000000000005, 2.0)) 
    print(ulps(0.5, 2.0)) 
    print(ulps(1.0, 2.0)) 
    print(2.0**52)        
    print(ulps(-1.0, 1.0)) 
    print(ulps(-1.0, 0.0)) 
    print(ulps(0.0, 1.0)) 
    print(ulps(5.0, math.inf))
    print(ulps(15.0, 100.0))  

    
if __name__ == "__main__":
    main()
