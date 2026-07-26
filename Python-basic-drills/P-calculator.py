# # price = 19.99
# # quality = 3
# # discount_pct = 10

# # total = price * quality
# # discount_amount = total * discount_pct/100
# # final_total = round(total-discount_amount, 2)

# # print(f"Final price : {final_total}")

# ## print information

# # print("Hello Universe")
# # print("LET'S GO!!!")

# name = "yash"
# work = "Ai Engneer"
# country = "Netherland"
# age = 27
# salary = 99999.99


# print(
#     f"Hello my name is {name},"
#     f" i am a {work},"
#     f"working in {country},"
#     f"my age is {age} ,"
#     f"and my salary is  {salary}"
# )


name = "Yash"  # string
age = 27  # int
salary = 99999.99  # float
is_pro = True  # boolean
skills = ["Python", "Node.js", "Javascript", "Sql", "Linux"]  # list

location = ("Hyderabad", "India")  # tuple
tech_stack = {"Python", "Javascript", "Sql", "Python"}  # set
employee = {
    "id": 101,
    "name": "Yash",
    "department": "Engineering",
    "experience": 3,
    "salary": 99999.99,
    "is_pro": True,
}  # dictonary
# no value
manager = None

print(f"My name is : {name} | {type(name)}")
print(f"My age is : {age} | {type(age)}")
print(f"My salary is : {salary} | {type(salary)}")
print(f"My skills are  : {skills} | {type(skills)}")
print(f"I am available in following locations : {location} | {type(location)}")
print(f"My main tech_stack is : {tech_stack} | {type(tech_stack)}")
print(f"Employee details: {employee} | {type(employee)}")
print(f"Manager {manager} | {type(manager)}")
