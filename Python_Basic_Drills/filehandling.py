

#write
file = open("demo.txt", "w")

file.write("Hello Python")

file.close()


#read

file = open("demo.txt", "r")

print(file.read())

file.close()



#advance
with open("employee.txt", "w") as file:
    file.write("Name: Yash\n")
    file.write("Role: Python Developer\n")

with open("employee.txt", "r") as file:
    print(file.read())