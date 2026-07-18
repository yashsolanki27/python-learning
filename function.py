# 1. Simple Function
def welcome():
    print("Welcome to Python")

welcome()


# 2. Function with Parameters
def greet(name):
    print("Hello", name)

greet("John")


# 3. Function with Multiple Parameters
def employee(name, age):
    print("Name:", name)
    print("Age :", age)

employee("Alex", 28)


# 4. Function Returning Value
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum =", result)


# 5. Function with Default Parameter
def country(name="India"):
    print("Country:", name)

country()
country("Netherlands")


# 6. Function with Keyword Arguments
def student(name, age):
    print(name, age)

student(age=25, name="David")