import sys
import math
import numpy as np

def func1(x):
    return (x * math.cos(x)) + math.sin(x)
    
def func2(x):
    return (math.e ** -x) - x

def zero(a, b, f):
    fa = f(a)
    fb = f(b)
    functionCalls = 2
    minNum = math.ulp(0)
    e = sys.float_info.epsilon
    
    if(fa * fb > 0):
        print("Bracket [", a, ", ", b, "] does not bracket a root.", sep = '')
        return None
    
    if(fa == 0):
        return a, functionCalls
    elif(fb == 0):
        return b, functionCalls
    
    while True:
        while True:
            smallestInterval = [a, fa, b, fb]
            #Calculate c using false position
            #c = a - fa * (b - a) / (fb - fa) honestly not sure where i got this...
            c = ((fb * a)-(fa * b))/(fb - fa)
            fc = f(c)
            functionCalls += 1
            #Is fc within 1 ulp of 0? (minNum = math.ulp(0))
            if(abs(fc) <= minNum):
                #print("abs(fc) break")
                #print("We got the number!")
                break
            
            #Is the line really flat? (Unoptimized)

            if(c <= a or c >= b):
                #print("c <= a or c >= b break")
                break


            #Is the line really flat? (Optimized)
            '''
            if (c <= a):
                c = a + (e * abs(a))
            elif (c >= b):
                c = b - (e * abs(b))
            if (c == a or c == b):
                break
            '''
            
            #Is c within one ulp of a? or Is c within one ulp of b?
            if((abs(a - c) <= abs(a) * e) or (abs(c - b) <= abs(c) * e)):
                #print("(abs(a - c) <= abs(a) * e) or (abs(c - b) <= abs(c) * e) break")
                #print("c is within 1 ulp of a or b")
                #print("We got the number!")
                break
            
            #If fa and fc same sign use [a, c] to find d
            if (np.sign(fa) == np.sign(fc)):
                smallestInterval = [c, fc, b, fb]
                #Calculate d using secant method using [a, c]
                d = c - fc * ((c - a)/(fc - fa))
                fd = f(d)
                functionCalls += 1
                #Is fd within 1 ulp of 0? (minNum = math.ulp(0))
                if(abs(fd) <= minNum):
                    #print("abs(fd) break")
                    #print("We got the number!")
                    break
                
                #Is the secant line really flat?
                if(d >= b):
                    #print("d >= b break")
                    break
                
                smallestInterval = [c, fc, d, fd]
                #Is the length of [c, d] not less than half of [a, b]?
                if(abs(d-c) > (abs(b-a) / 2)):
                    #print("abs(d-c) > (abs(b-a) / 2) break")
                    #print("[c, d] is not less than half the length of [a, b]")
                    break
                
                #Change to new interval a = c and b = d
                a = c
                fa = fc
                b = d
                fb = fd
                
            #Else use [b, c] to find d
            else:
                smallestInterval = [a, fa, c, fc]
                #Calculate d using secant method using [c, b]
                d = b - fb * ((b - c)/(fb - fc))
                fd = f(d)
                functionCalls += 1
                #Is fd within 1 ulp of 0? (minNum = math.ulp(0))
                if(abs(fd) <= minNum):
                    #print("abs(fd) break")
                    #print("We got the number!")
                    break
                
                #Is the secant line really flat?
                if(d <= a):
                    #print("d <= a break")
                    break
                
                smallestInterval = [d, fd, c, fc]
                #Is the length of [d, c] not less than half of [a, b]?
                if(abs(c-d) > (abs(b-a) / 2)):
                    #print("abs(c-d) > (abs(b-a) / 2) break")
                    #print("[d, c] is not less than half the length of [a, b]")
                    break
                
                #Change to new interval a = d and b = c
                a = d
                fa = fd
                b = c
                fb = fc
                
        #End of False Position Loop
                
        #Root Checks
        #Is fc within 1 ulp of 0? (minNum = math.ulp(0))
        if(abs(fc) <= minNum):
            #print("abs(fc) break - Bisection")
            #print("We got the number!")
            break
        #Is c within one ulp of a? or Is c within one ulp of b?
        if((abs(a - c) <= abs(a) * e) or (abs(c - b) <= abs(c) * e)):
            #print("(abs(a - c) <= abs(a) * e) or (abs(c - b) <= abs(c) * e) break")
            #print("c is within 1 ulp of a or b - Bisection")
            #print("We got the number!")
            break
        #Is fd within 1 ulp of 0? (minNum = math.ulp(0))
        if(abs(fd) <= minNum):
            #print("abs(fd) break - Bisection")
            #print("We got the number!")
            c = d
            fc = fd
            break
        
        #Bisection
        #Calculate the mid point using the current smallest interval
        #smallestInterval = [x, f(x), y, y(x)] where x and y are either a, b, c, or d
        mid = (smallestInterval[0]+smallestInterval[2]) / 2
        fmid = f(mid)
        if(fmid * smallestInterval[1] > 0):
            functionCalls += 1
            a = mid
            fa = fmid
            b = smallestInterval[2]
            fb = smallestInterval[3]
            
        else:
            functionCalls += 1
            b = mid
            fb = fmid
            a = smallestInterval[0]
            fa = smallestInterval[1]
            
        if(abs(b - a) <= c * e):
            break
        
    #End of Bisection Loop
    return c, fc, functionCalls

def main():
    test1 = zero(2, 3, func1)
    print("Bracket [2, 3] in func1 has a root of", test1[0], "with f(root) =", test1[1], "with", test1[2], "function calls")
    
    test2 = zero(4, 5, func1)
    print("Bracket [4, 5] in func1 has a root of", test2[0], "with f(root) =", test2[1], "with", test2[2], "function calls")
    
    test3 = zero(0, 1, func2)
    print("Bracket [0, 1] in func2 has a root of", test3[0], "with f(root) =", test3[1], "with", test3[2], "function calls")

if __name__ == "__main__":
    main()