import math ;


#Exercise 1 calculate area of a rectangle


# length = float(input("Enter the length : "));
# width = float(input("Enter the width : "));


# area = length*width;

# print(f"The area is :{area} cm²")
# # print(area);


#Exercise 2 Shopping Cart Program

# item = input("what item you want to buy: ");
# price = float(input("What is the price of the item: "));
# quantity = int(input("How many you want to buy: "));

# total = quantity*price;

# print(f"You bought {quantity} {item}/s your grand total price is ${total}");
# print(f"Your total is ${total} Pay and enjoy your {item}/s");


#Exercise 3:  Calculate the circumference of the circle 

# # c = 2 pie r
# import math

# radius = float(input("Enter the radius of the circle: "));
# circumference =  2* math.pi * radius ;

# print(f"The circumference of the circel is: {round(circumference,2)} cm");

#Exercise 4 Calculate the area of a circle 

# radius = float(input("Write the area of a circle : "));

# area =  math.pi * pow (radius, 2);

# print(f"The area of a cricle is {round(area,3)} cm^2");

#Exercise 5 Calculate the Hypotenuse of a right angle triangle 

#c = (a²+b²)²
     
# a = float(input("Enter side A: "));
# b = float(input("Enter side B: "));

# c = math.sqrt (pow(a,2)+pow(b,2));

# print(f"Side C : {round(c,2)}");


#Exercise 6 Calculator using if-elif


# operator = input("Select the Operator (+, -, *, /): ")

# num1 = float(input("Enter your first Number: "))
# num2 = float(input("Enter your Second Number: "))

# if operator == "+":
#     result = num1 + num2
#     print(f"Total sum is: {round(result, 3)}")

# elif operator == "-":
#     result = num1 - num2
#     print(f"Total difference is: {round(result, 3)}")

# elif operator == "*":
#     result = num1 * num2
#     print(f"Total product is: {round(result, 3)}")

# elif operator == "/":
#     if num2 != 0:
#         result = num1 / num2
#         print(f"Total quotient is: {round(result, 3)}")
#     else:
#         print("Error: Division by zero is not allowed.")

# else:
#     print("Invalid operator! Please choose +, -, *, or /.")


#Ternary / conditional operator
num = float(input("enter the number: "));


result = "even" if num%2 == 0 else "odd";

print(f"Number is {result}");