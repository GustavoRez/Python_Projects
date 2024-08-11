def sum(x, y):
    print(x + y)

def Sub(x, y):
    print(x - y)

def Mult(x, y):
    print(x * y)

def Div(x, y):
    calc = float(x) / float(y)
    print(calc)

num1 = int(input("Insert the first number: "))
num2 = int(input("Insert the second number: "))

SC = input("Wich operation you want to do? ")

if SC == "Sum":
    sum(num1, num2)
elif SC == "Subtraction":
    Sub(num1, num2)
elif SC == "Multiplication":
    Mult(num1, num2)
elif SC == "Division":
    Div(num1, num2)
else:
    print ("Insert a valid operation. (Remember using capital letter on the first letter)")