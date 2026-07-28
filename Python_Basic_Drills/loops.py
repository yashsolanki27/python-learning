#for loop
# Print numbers 1 to 5

##for i in range(1, 6):
  ##  print(i)


# List of employees
employees = ["John", "Alex", "David"]

# -------- FOR LOOP --------
print("=== FOR LOOP ===")

for employee in employees:
    print("Employee:", employee)


# -------- FOR LOOP WITH RANGE --------
print("\n=== RANGE LOOP ===")

for i in range(1, 6):
    print("Day", i)


# -------- NESTED LOOP --------
print("\n=== NESTED LOOP ===")

for employee in employees:
    for task in range(1, 3):
        print(employee, "- Task", task)


# -------- WHILE LOOP --------
print("\n=== WHILE LOOP ===")

count = 1

while count <= 5:
    print("Attempt", count)
    count += 1


# -------- CONTINUE --------
print("\n=== CONTINUE ===")

for number in range(1, 6):

    if number == 3:
        continue

    print(number)


# -------- BREAK --------
print("\n=== BREAK ===")

for number in range(1, 6):

    if number == 4:
        break

    print(number)


# -------- PASS --------
print("\n=== PASS ===")

for number in range(1, 6):

    if number == 3:
        pass

    print(number)