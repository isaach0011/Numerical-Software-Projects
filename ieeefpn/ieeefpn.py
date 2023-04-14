"""
Project: Module 3 - Programming Assignment: IEEE Utilities
Author: Isaac Hill
Class: CS3320-001
"""
import struct
import math
import numpy as np

def sign(x):
    bitNum = struct.unpack('Q', struct.pack('d', x))[0]
    #If sign bit contains a 1 (if number is negative)
    if (bitNum & (1 << 63)):
        #If after removing the 1 the number is not zero
        if((bitNum ^ (1 << 63)) != 0):
            return -1
        else:
            return 0
    else:
        #If number is not zero
        if(bitNum != 0):
            return 1
        else:
            return 0

def exponent(x):
    bitNum = struct.unpack('Q', struct.pack('d', x))[0]
    EXPONENT_MASK = 0x7FF0000000000000
    
    #Cuts out exponent from bitNum
    exponent = int(format(bitNum & EXPONENT_MASK, '0>64b')[1:12], 2)
    
    #If number is subnormal
    if(exponent == 0):
        if(bitNum != 0):
            return exponent - 1022
        else:
            return 0
    else:
        return exponent - 1023

def fraction(x):
    bitNum = struct.unpack('Q', struct.pack('d', x))[0]
    FRAC_MASK = 0x000FFFFFFFFFFFFF
    
    #Cuts out fraction from bitNum
    fractionNum = int(format(bitNum & FRAC_MASK, '0>64b')[12:64], 2)
    
    return fractionNum * (2 ** -52)
    
def mantissa(x):
    bitNum = struct.unpack('Q', struct.pack('d', x))[0]
    MANT_MASK = 0x000FFFFFFFFFFFFF
    
    #cuts out fraction from bitNum
    mantissaNum = int(format(bitNum & MANT_MASK, '0>64b')[12:64], 2)
    
    if (exponent(x) == 0):
        return mantissaNum * (2 ** -52)
    else:
        #Add one to fraction to create mantissa
        return (mantissaNum * (2 ** -52)) + 1
    
def is_posinfinity(x):
    #If sign is negative
    if(sign(x) == -1):
        return False
    else:
        #If all exponent bits are set and fraction bits are 0
        if(exponent(x) == 1024 and fraction(x) == 0):
            return True
        else:
            return False
    
def is_neginfinity(x):
    #If sign is positive
    if(sign(x) == 1):
        return False
    else:
        #If all exponent bits are set and fraction bits are 0
        if(exponent(x) == 1024 and fraction(x) == 0):
            return True
        else:
            return False

def ulp(x):
    bitNum = struct.unpack('Q', struct.pack('d', x))[0]
    
    if(bitNum == 0):
        return(2 ** -1022) * (2 ** -52)
    else:
        return (2 ** exponent(x)) * (2 ** -52)

def ulps(x, y):
    #Swap x and y if x is greater than y
    if(x > y):
        tempNum = x
        x = y
        y = tempNum
        
    xbitNum = struct.unpack('Q', struct.pack('d', x))[0]
    ybitNum = struct.unpack('Q', struct.pack('d', y))[0]
    
    return ybitNum - xbitNum

def main():
    y = 6.5 
    subMin = np.nextafter(0,1) #subMin = 5e-324
    print(sign(y)) #1 
    print(sign(0.0)) #0 
    print(sign(-y)) #-1 
    print(sign(-0.0)) #0
    print(exponent(y)) #2 
    print(exponent(16.6)) #4
    print(fraction(0.0)) #0.0 
    print(mantissa(y)) #1.625 
    print(mantissa(0.0)) #0.0
    var1 = float('nan')
    print(exponent(var1)) #1024 
    print(exponent(0.0)) #0 
    print(exponent(subMin)) #-1022
    print(is_posinfinity(math.inf)) #True 
    print(is_neginfinity(math.inf)) #False 
    print(not is_posinfinity(-math.inf)) #True 
    print(is_neginfinity(-math.inf)) #True
    print(ulp(y)) #8.881784197001252e-16
    print(ulp(1.0)) #2.220446049250313e-16
    print(ulp(0.0)) #5e-324
    print(ulp(subMin)) #5e-324 
    print(ulp(1.0e15)) #0.125
    print(ulps(5,99)) #4503599627370496 
    
if __name__ == "__main__":
    main()