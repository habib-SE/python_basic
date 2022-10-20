class Employee:
    _empName = None
    _empAddress = None
    _empId = None
    _empExperiance = None
    _empSalary = None

    def __init__(self):
        self._empName = "Habib"
        self._empAddress = "Swabi"
        self._empId = 201167
        self._empExperiance = "4 Years"
        self._empSalary = 100000

    def displayInfo(self):
        print("Employee Information")
        print("Employee name is ",self._empName)
        print("Emp Address",self._empAddress)
        print("Emp id is",self._empId)
        print("Emp Exp",self._empExperiance)
        print("Emp Salary is",self._empSalary)

emp = Employee()
emp.displayInfo()


# def printname(name):
#   print("your name is ",name[4])
# printname("habib")

# def sub(a, b):
#     c = abs(a-b)
#     print("the sub is", c)


# def add(a, b):
#     c = a+b
#     print("the sum is", c)
#     num1 = int(input("Enter first number"))
#     num2 = int(input("Enter second number"))
#     print("1.....addition")
#     print("2.....subtraction")
#     choice = int(input("Enter your choice"))
#     if choice == 1:
#         add(num1, num2)
#     else:
#         sub(num1, num2)


# from datetime import datetime
# habib=datetime.now()
# print("This s current date and time",habib.strftime("%d/%m/%Y %I:%M %A"))

#  Class Declaration
# class Employee:
#     def _init_(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def Display(self):
#         print("first name is", self.fname)
#         print("Last name is", self.lname)

#     def getName(self, fname, lname):
#         self.fname = fname
#         self.lname = lname


# emp = Employee("habib", "Raja")
# emp.getName("saeed","Ahmad")
# emp.Display()


# class Employee:
#     def Employee_name(name):
#         input("enter name")
