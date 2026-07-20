#exception handling


try:
    num = int(input("Enter a number: "))
    print(num)

except ValueError:
    print("Please enter a valid number.")


    #advance 

    try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print(result)

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program Finished")