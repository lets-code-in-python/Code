#today we will see how to write a program for maths calculations in python

a=int(input("enter first number"))
b=int(input("enter second number"))
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    try:
        z=a/b
        return z
    except ArithmeticError:
        print("there is arithmetic error")
def mul(a,b):
    return a*b

print("sum is",add(a,b))
print("sub is",sub(a,b))
print("div is",div(a,b))
print("mul is",mul(a,b))