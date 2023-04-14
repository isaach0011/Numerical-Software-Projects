import sys
import math

# Defining Function
def f(x):
    return (x ** 4) - (6 * x ** 3) + (12 * x ** 2) - (10 * x) + 3

# Implementing False Position Method
def falsePosition(x0,x1,e):
    step = 1
    print('\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        print('Iteration-', step, ': x2 = ', x2, ' and f(x2) = ', f(x2))

        if f(x0) * f(x2) < 0:
            #x1 upper
            x1 = x2
        else:
            #x0 lower
            x0 = x2

        step = step + 1
        condition = abs(f(x2)) > e

    print('\nx Lower Bounds: ', x1)
    print('x UpperBounds: ', x2)
    print('\nRequired root is: ', x2)


# Input Section
x0 = 0
x1 = 1.5
e = sys.float_info.epsilon

# Converting input to float
x0 = float(x0)
x1 = float(x1)
e = float(e)

#Note: You can combine above two section like this
# x0 = float(input('First Guess: '))
# x1 = float(input('Second Guess: '))
# e = float(input('Tolerable Error: '))


# Checking Correctness of initial guess values and false positioning
print(f(x0))
print(f(x1))
print(f(x0) * f(x1))
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    falsePosition(x0,x1,e)