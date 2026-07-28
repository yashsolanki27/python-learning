# # normal loops
# #
# numbers = [1, 2, 3, 4, 5, 6]
# square = []

# for n in numbers:
#     square.append(n * n)

# print(square)

# # list comprehension
# # [new_value] for [item] in [iterable]

# numbers = [1, 2, 3, 4, 5, 6]
# square = [n * n for n in numbers]
# print(square)


# # list comprehension with if
# # nrmal
# numbers = [1, 2, 3, 4, 5, 6]
# even = []

# for n in numbers:
#     if n % 2 == 0:
#         even.append(n)

# print(even)
# # list comprehension with if

# # [new_value] for [item] in [iterable] [if] condition
# numbers = [1, 2, 3, 4, 5, 6]
# even = [n for n in numbers if n % 2 == 0]
# print(even)

# # list comprehension with if-else condition
# # normal
# numbers = [1, 2, 3, 4, 5, 6]
# result = []

# for n in numbers:
#     if n % 2 == 0:
#         result.append("even")
#     else:
#         result.append("odd")

# print(result)

# # list comprehension with if-else condition
# # [value_if_true if condition else value_if_false for item in iterable]

# numbers = [1, 2, 3, 4, 5, 6]
# result = ["even" if n % 2 == 0 else "odd" for n in numbers]
# print(result)


# numbers = [2, 4, 6, 8]

# double = []

# for n in numbers:
#     double.append(n * 2)


# numbers = [2, 4, 6, 8]

# double = [n * 2 for n in numbers]

# print(double)


# # Convert strings to uppercase


# names = ["john", "alice", "bob"]

# upper_name = [name.upper() for name in names]

# # Get the length of each string

# names = ["John", "Alexander", "Tom"]
# lengths = [len(name) for name in names]


# # Remove extra spaces

# names = [" John ", " Alice ", " Bob "]

# stripp = [name.strip() for name in names]

# # Convert strings to integers

# numbers = ["1", "2", "3"]

# rs = [int(n) for n in numbers]


# # # Basic(Transform)
# # # Filter
# # # Conditional Transform

# # # if at the end → Filter (include or skip items).
# # #if...else before for → Transform (every item stays, but its value may change).

# # # normal

# # numbers = [1, 2, 3, 4]
# # square = {}

# # for n in numbers:
# #     square[n] = n * n

# # print(square)

# # # Dictionary
# # square = {n: n * n for n in numbers}


numbers = [1, 2, 3, 4]
square = {}

for n in numbers:
    if n % 2 == 0:
        square[n] = n * n

print(square)
square = {n: n * n for n in numbers if n % 2 == 0}

print(square)


# name to length

names = ["John", "Alice", "Bob"]

length = {name: len(name) for name in names}

# word to upper case
names = ["john", "alice"]

result = {name: name.upper() for name in names}

# List  - stores everything and fast to access
# square = [n * n for n in numbers]
# generator  - stores one value at a time and use less memory
# square = (n * n for n in numbers)
# unique  -- {value for item in iterable}  remove duplicates
numbers = [1, 2, 2, 3, 3, 555, 555, 555, 555, 444, 444, 444, 444]
unique = set()

for n in numbers:
    unique.add(n)

unique = {n for n in numbers}
print(unique)
