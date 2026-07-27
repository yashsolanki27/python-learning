# file = open ("filename", "mode")
#   ##do some operations
# file.close()


# with open("hat.txt", "r") as file:
#     print(file.read())


try:
    with open("students.txt", "x") as file:
        print("File Created successfuly")

except FileExistsError:
    print("file already exists")


with open("students.txt", "w") as file:
    file.write("name: Ysash\n")
    file.write("age: 217\n")
    file.write("role: Py dedv\n")
print("Safely writes")

with open("stud.txt", "a") as file:
    file.write("country: India\n")
    file.write("experties: coding\n")

print("Safely apped")


with open("stud.txt", "r") as file:
    data = file.read()

print("\nFile Content:")
print(data)
