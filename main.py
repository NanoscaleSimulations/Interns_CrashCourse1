import math

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

def BMI(weight, height):
    return weight/height**2

def speed(distance, time):
    return distance/time

def Quadratic(a,b,c):
    #The Formula will have the imput of (a*x^2)+(b*x)+c=0
    #It will find the possible values of x
    
    if ((b**2)-(4*a*c)) > 0: #When the discriminant is larger than 0; Two real solutions.
        return ((-b+math.sqrt((b**2)-(4*a*c)))/(2*a),
                (-b-math.sqrt((b**2)-(4*a*c)))/(2*a))
        
    if ((b**2)-(4*a*c)) == 0: #When the discriminant is equal to 0; One real solution.
        return((-b+math.sqrt((b**2)-(4*a*c)))/(2*a))
    
    if ((b**2)-(4*a*c)) < 0: #When the discriminant is less than 0; No real solutions
        return(print('The Discriminant is less than 0; No real solutions'))

def Sin(x):
    #Find the value of the Sine function
    return(math.sin(x))

def Tan(x):
    #Find the value of the Tangent function
    return(math.tan(x))

def Standard_Deviation(X): #Calculate the Standard Deviation
    #Find the Mean
    Sum = 0
    for number1 in X:
        Sum += number1
    mean = Sum / len(X)
    
    #Find the Sum of the numerator
    Sum2 = 0
    for number2 in X:
        Sum2 += (number2 - mean)**2
        
    #Calculate the St. Dev.
    sd = (math.sqrt((1.0/(float(len(X))-1.0))*Sum2))
    return(sd)


def Largest_Value(X): #Return the Largest value in the list
    return (max(X))


def Smallest_Value(X): #Return the Smallest value in the list
    return (min(X))

def Lar_Val(X): #Return the Largest value in the list using a Loop
    var = 0
    for i in X:
        if i > var:
            var = i
            
    return (var)

def Small_Val(X):#Return the Smallest value in the list using a Loop
    var = 0
    for i in X:
        if i < var:
            var = i
            
    return (var)





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
    print("test for BMI")
    print(BMI(106, 1.76))
    print("testing speed")
    print(speed(200,4))    # Test of Quadratic Equation
    print('Test of Quadratic Equation')
    print(Quadratic(1,3,2))
    # Test of Sine Function
    print('Test of Sine Function')
    print(Sin(math.pi))
    # Test of the Tangent Function
    print('Test of the Tangent Function')
    print(math.pi)
    #Test St. Dev.
    print('Test of the Standard Deviation')
    print(Standard_Deviation([1,2,3,4,5]))
    print('Test for Largest Value')
    print(Largest_Value([1,2,3]))
    print('Test for Smallest Value')
    print(Smallest_Value([1,2,3]))
    print('Largest Value with loop')
    print(Lar_Val([1,2,3,7,3]))
    print('Smallest value with Loop')
    print(Small_Val([1,4,-3,9]))
    
