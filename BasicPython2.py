#swapping of two numbers
x=int(input("Enter x:"))
y=int(input("Enter y:"))
temp=x
x=y
y=temp
print("x after swap:",x)
print("y after swap:",y)

#swapping without third variable
p=int(input("Enter p:"))
q=int(input("Enter q:"))
p,q=q,p
print("after swap p:",p)
print("after swap q:",q)

#calculateinterest
p=float(input("Enter principal:"))
r=float(input("Enter rate:"))
t=float(input("Enter time:"))
#simpleinterest
si=(p*r*t)/100
print("simple interest is rs:",si)

#AverageOfFirstFivenumbers
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter third number:"))
n4=int(input("Enter fourth number:"))
n5=int(input("Enter fifth number:"))

Average=(n1+n2+n3+n4+n5)/5
print("Average is found to be:",Average)

#DiscriminantFinding
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
#discriminant,D
D=b**2-(4*a*c)
print("Discriminant is:",D)

