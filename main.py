print('This is our main')
import numpy as np
def Subtract(x,y):
    return x-y

def Divide(x,y):
    return x/y

def add(x,y):
    return x+y

def times(x,y):
    return x*y

def exponential(a,b):
    return a**b

def cos(x): #In degrees
    return np.cos(x)

def sqrt(x):
    return np.sqrt(x)

if __name__ == "__main__":
    print('testing mulitplication')
    print(times(2,4))
    print('testing addition')
    print(add(10,5))
    print('testing subtraction')
    # Test of Subtract
    print(Subtract(5,2))
    print('testing division')
    # Test of Divide
    print(Divide(10,2))
    print("Testing exponents")
    print(exponential(3,2))
    print("Testing the cosine function")
    print(cos(45))
    print("Testing square root")
    print(sqrt(9))