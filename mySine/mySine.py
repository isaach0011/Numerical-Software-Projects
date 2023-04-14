"""
Project: Module 4 - Programming Assignment: mySine
Author: Isaac Hill
Class: CS3320-001
"""
import math
import sys

def mySine(x):
    eps = sys.float_info.epsilon
    
    #If x is a small angle
    if(x ** 2 <= eps):
        return x
    #If x is a large angle
    if(abs(x) > 10 ** 9):
        return math.nan
    
    pi = math.pi
    
    #X reduction
    n = round(x/pi)
    t = x - (n * pi)
    
    sineX = 0.0
    add = True
    
    #Calculates the Taylor Series up to the 21st term.
    for term in range(1, 23, 2):
        factorialForTerm = 1
        
        #Calculates the factorial for the current term
        for factorial in range(1, term + 1):
            factorialForTerm *= factorial
            
        #Alternate between adding and subtracting
        if(add == True):
            sineX += (t ** term) / factorialForTerm
            add = False
        else:
            sineX -= (t ** term) / factorialForTerm
            add = True
            
    return sineX
    
def main():
    print(mySine(1.0e-08))     #1e-08 
    print(mySine(0.00001))     #9.999999999833334e-06 
    print(mySine(0))           #0 
    print(mySine(math.pi/2))   #1.0000000000000002 
    print(mySine(math.pi))     #-0.0 
    print(mySine(100))         #-0.5063656411097555 
    print(mySine(-1000))       #-0.8268795405320125 
    print(mySine(999999999))   #-0.4101372630100049 
    print(mySine(-1000000001)) #nan

if __name__ == "__main__":
    main()