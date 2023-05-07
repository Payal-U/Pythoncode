#Calculate areas
l=float(input("Enter length:"))
b=float(input("Enter breadth:"))
h=float(input("Enter height:"))
#rectangleArea
Rectangle=l*b
print("Area of a rectangle is:",Rectangle)
#SquareArea
s=float(input("Enter side:"))
Square=s*s
print("Area of a square is:",Square)
#TriangleArea
B=float(input("Enter base of triangle:"))
H=float(input("Enter height of triangle:"))
Triangle=(B*H)/2
print("Area of triangle is:",Triangle)
#circleArea
r=float(input("Enter radius of circle:"))
Circle=(22/7)*(r*r)
print("Area of circle is:",Circle)

#BaiscSalary
Basic=int(input("Enter employee basic salary:"))
DA=0.05*Basic
HRA=0.07*Basic
PF=0.03*Basic
#AfterDeductions
Net=Basic-(DA+HRA+PF)
print("Net salary of the employee is:",Net)

#CalculatePowerOfNumber
print(pow(10,3))

#Pythonversion
import sys
print("Python version")
print(sys.version)
