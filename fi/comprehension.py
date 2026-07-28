# normal loops
#
numbers = [1, 2, 3, 4, 5, 6]
square = []

for n in numbers:
    square.append(n * n)

print(square)

# list comprehension
# [new_value] for [item] in [iterable]

numbers = [1, 2, 3, 4, 5, 6]
square = [n * n for n in numbers]
print(square)


# list comprehension with if
# nrmal
numbers = [1, 2, 3, 4, 5, 6]
even = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)

print(even)
# list comprehension with if

# [new_value] for [item] in [iterable] [if] condition
numbers = [1, 2, 3, 4, 5, 6]
even = [n for n in numbers if n % 2 == 0]
print(even)

# list comprehension with if-else condition
# normal
numbers = [1, 2, 3, 4, 5, 6]
result = []

for n in numbers:
    if n % 2 == 0:
        result.append("even")
    else:
        result.append("odd")

print(result)

# list comprehension with if-else condition
# [value_if_true if condition else value_if_false for item in iterable]

numbers = [1, 2, 3, 4, 5, 6]
result = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(result)


numbers = [2, 4, 6, 8]

double = []

for n in numbers:
    double.append(n * 2)


numbers = [2, 4, 6, 8]

double = [n * 2 for n in numbers]

print(double)
