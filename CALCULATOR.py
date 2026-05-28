#Calculator:

#MATRIX OPERATION:
print("\n --MENU to choose the operation to be performend--")
print("1) ADDITION")
print("2) SUBTRACTION")
print("3) DIVISION")
print("4) MULTIPLICATION")
choice=input("choose any operation to be performed:(1/2/3/4):")
a=int(input("enter first num:"))
b=int(input("enter second num:"))
if choice=="1":
    print("ADDITION is :",a+b)
    
elif choice=="2":
    print("SUBTRACTION is :",a-b)
    
elif choice=="3":
    print("DIVISION is:",a/b)
      
elif choice=="4":
    print("MULTIPLICATION is :",a*b)
    
else:
    print("INVALID OPTION")   

# factorial calculator:
num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "is", factorial)   
#POWER CALCULATOR:
num = int(input("Enter a number: "))
num1 = int(input("Enter a power: "))
result=num**num1
print("result is :",result)
#temperature converter (Celsius to Fahrenheit and vice versa):
f=int(input("enter the temperature to convert fahrenheit into celsius:"))	
result= (f-32)*5/9
c=int(input("enter the temperature to convert celsius into fahrenheit :"))
result1=(c*9/5)+32
print("convert fahrenheit into celsius:",result)
print("convert celsius into fahrenheit:",result1)
#Number system converter (binary to decimal, octal to hexadecimal etc and vice versa):
num=int(input("Enter a decimal number: "))
print("decimal to bin:",bin(num))
print("decimal to oct:",oct(num))
print("decimal to hex:",hex(num))
#QUADRATIC EQUATION SOLVER:
import cmath

def solve_quadratic(a, b, c):
    d = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + d) / (2*a)
    x2 = (-b - d) / (2*a)
    return x1, x2
#LINEAR EQUATION SOLVER:    
def solve_linear(a, b):
    return -b / a
#PERCENTAGE SOLVER:    
def percentage(part, whole):
    return (part / whole) * 100    
# Trigonometry:
import math

def trig(x):
    return math.sin(x), math.cos(x), math.tan(x)

def inverse_trig(x):
    return math.asin(x), math.acos(x), math.atan(x)

def deg_to_rad(d):
    return d * math.pi / 180

def rad_to_deg(r):
    return r * 180 / math.pi


# Conversions:

def m_to_ft(m):
    return m * 3.28084

def ft_to_m(ft):
    return ft / 3.28084

def kg_to_lb(kg):
    return kg * 2.20462

def lb_to_kg(lb):
    return lb / 2.20462

def sec_to_min(sec):
    return sec / 60

def mps_to_kmph(mps):
    return mps * 3.6

def pa_to_atm(pa):
    return pa / 101325

def w_to_hp(w):
    return w / 745.7


# Shapes AREA AND PERIMETERS :


def area_circle(r):
    return math.pi * r * r

def perimeter_circle(r):
    return 2 * math.pi * r

def area_rectangle(l, w):
    return l * w

def perimeter_rectangle(l, w):
    return 2 * (l + w)

def area_triangle(b, h):
    return 0.5 * b * h
# Volume Calculator:
def volume_cube(a):
    return a ** 3

def volume_sphere(r):
    return (4/3) * math.pi * r**3

def volume_cylinder(r, h):
    return math.pi * r**2 * h
    
    
if __name__=="__main__":
    print("QUADRATIC EQUATION:",solve_quadratic(5,6,4)) 
    print("LINEAR EQUATION:",solve_linear(5,7)) 
    print("PERCENTAGE:",percentage(5,100)) 
    print("Trigonometry:",trig(0)) 
    print("CONVERSION:",sec_to_min(60))
    print("AREA & PERIMETERS:",area_circle(5))
