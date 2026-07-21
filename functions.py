
# def greet(): 
#     print("Hello!!")
#     print("Hello!! yashh")
#     print("Hello!! yashh againn");


# greet(); 


# def caculcate_total():


# def send_email():

# def validate_password():        


# def check_weather():
#     temperature = 30

#     if temperature > 25:
#         print("it's hot!")
#     else:
#         print("It's nice weather!") 


# check_weather()
# print(check_weather())

def greet_alice():
    print("hello alice!")


# def greet(first_name, last_name):
#     print(f"hello, {first_name} {last_name}")

# greet(first_name = "yash",  last_name = "solanki")
# greet("yash", "boss" )    
# greet(last_name = "solanki", first_name = "ysash"  )


# def greet(last_name, first_name = "Yash"):
#     print(f"Hii, {first_name} {last_name}")


# greet("Boss")    




# def calculate_total(price, tax_rate, discount):
#     tax = price * tax_rate
#     final_price = price + tax - discount
#     print(f"Total: ${final_price}")

# # Order matters!
# calculate_total(price = 100,tax_rate= 0.08,discount= 10)  # $98

# discount = 20

# def calculate_total(price):
# #default values
#     tax_rate = 0.08
#     discount = 10

# #calculation
#     tax = tax_rate * price
#     final_price = price + tax - discount
# #print the final price
#     print(f"total: $ {final_price}")


# calculate_total(price=100)

# discount



# def add_num (a,b):
#     print(a+b)


# print_result = add_num(a=5 ,b =10) 


# def add_return(a,b):
#     return (a+b)
# print_result = add_return(a=10,b=20)



# def calc_area (lenght,width):
#     area = lenght*width
#     area = area * 1.05
#     return area

# def double(number):
#     return number * 2

# # Store in variable
# result = double(5)

# # Use in expressions
# total = double(5) + double(3)  # 10 + 6 = 16

# # Pass to other functions
# print(double(10))  # 20

# # Use in conditions
# if double(7) > 10:
#     print("Big number!")



def simple_function():
    numbers = [1,2,3,4,5]

    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number ,last_number

 

f,l = simple_function()

print(f)
print(l)