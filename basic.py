# def printname(name):
#   print("your name is ",name[4])
# printname("habib")

def sub(a, b):
    c = abs(a-b)
    print("the sub is", c)


def add(a, b):
    c = a+b
    print("the sum is", c)
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    print("1.....addition")
    print("2.....subtraction")
    choice = int(input("Enter your choice"))
    if choice == 1:
        add(num1, num2)
    else:
        sub(num1, num2)


# from datetime import datetime
# habib=datetime.now()
# print("This s current date and time",habib.strftime("%d/%m/%Y %I:%M %A"))
