# ==========================================
# LISTS

# 1. Indexing
# 2. Negative Indexing
# 3. Slicing
# 4. append()
# 5. insert()
# 6. remove()
# 7. pop()
# 8. sort()
# 9. reverse()
# 10. Nested Lists
# 11. List Comprehension


# ----------------------------
# Create a List
# ----------------------------

skills = ["Python", "Java", "SQL", "Linux"]

print("Original List:")
print(skills)


# ----------------------------
# 1. Indexing
# ----------------------------

print("\nFirst Skill:")
print(skills[0])

print("\nSecond Skill:")
print(skills[1])


# ----------------------------
# 2. Negative Indexing
# ----------------------------

print("\nLast Skill:")
print(skills[-1])

print("\nSecond Last Skill:")
print(skills[-2])


# ----------------------------
# 3. List Slicing
# ----------------------------

print("\nFirst Two Skills:")
print(skills[0:2])

print("\nMiddle Skills:")
print(skills[1:3])

print("\nComplete List:")
print(skills[:])

print("\nLast Two Skills:")
print(skills[-2:])


# ----------------------------
# 4. append()
# Adds one item at the end
# ----------------------------

skills.append("Docker")

print("\nAfter append():")
print(skills)


# ----------------------------
# 5. insert()
# Insert at specific position
# ----------------------------

skills.insert(1, "Git")

print("\nAfter insert():")
print(skills)


# ----------------------------
# 6. remove()
# Removes by VALUE
# ----------------------------

skills.remove("SQL")

print("\nAfter remove():")
print(skills)


# ----------------------------
# 7. pop()
# Removes by INDEX
# ----------------------------

removed_skill = skills.pop(2)

print("\nRemoved Skill:")
print(removed_skill)

print("\nRemaining Skills:")
print(skills)


# ----------------------------
# 8. sort()
# Sort Alphabetically
# ----------------------------

skills.sort()

print("\nSorted List:")
print(skills)


# ----------------------------
# 9. reverse()
# Reverse Order
# ----------------------------

skills.reverse()

print("\nReversed List:")
print(skills)


# ----------------------------
# 10. Nested Lists
# ----------------------------

employees = [["Yash", 27], ["Rahul", 30], ["Priya", 25]]

print("\nNested List:")
print(employees)

print("\nFirst Employee:")
print(employees[0])

print("\nFirst Employee Name:")
print(employees[0][0])

print("\nSecond Employee Age:")
print(employees[1][1])


# ----------------------------
# 11. List Comprehension
# ----------------------------

numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print("\nOriginal Numbers:")
print(numbers)

print("\nSquared Numbers:")
print(squares)
