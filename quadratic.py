#!/usr/bin/python
import sys
import math

#Python script that returns the roots of a quadratic equation
#of the form a*x^2 + b*x + c = 0
#Enter values for a, b, and c in the command line
#e.g. run: >python quadratic.py 1 2 -15
def main():
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    x1, x2 = find_roots(a, b, c)
    print ("This is x1: %f" %x1)
    print ("This is x2: %f" %x2)


def find_roots(a,b,c): #Fixed by changing b^2 to b**2, sqrt_mid = mid**(1/2) to math.sqrt(mid)
    try:
        float(a)
        float(b)
        float(c)
    except TypeError:
        print "Not a valid input, please enter three numerical values"
    a = float(a)
    b = float(b)
    c = float(c)
    try:
        1/a
    except ZeroDivisionError:
        print "Zero leading coefficient; not a quadratic"
    mid = b**2 - 4*a*c
    try:
        math.sqrt(mid)
    except ValueError:
        print "This is a negative root, there are no real solutions."
    sqrt_mid = math.sqrt(mid)
    x1 = (-b + sqrt_mid)/(2*a)
    x2 = (-b - sqrt_mid)/(2*a)
    return x1, x2


if __name__=="__main__":
        main()
