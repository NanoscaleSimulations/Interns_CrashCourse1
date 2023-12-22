import math

print('This is our main')

def Subtract(x,y):
    return x-y

def Divide(x,y):
    return x/y

def add(x,y):
    return x+y

def times(x,y):
    return x*y

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
    # Test of Quadratic Equation
    print('Test of Quadratic Equation')
    print(Quadratic(1,3,2))
    # Test of Sine Function
    print('Test of Sine Function')
    print(Sin(math.pi))
    # Test of the Tangent Function
    print('Test of the Tangent Function')
    print(math.pi)
    
