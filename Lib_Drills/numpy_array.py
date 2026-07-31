import numpy as np

# NumPy Arrays  → Fast numerical operations
# creating an array
arrs = np.array(
    [10, 20, 30, 40, 50, 60]
)  # np.array is a function, so you must call it using ()

print(arrs)


student_marks = [80, 55, 46, 24, 78]  # python list

print(student_marks)

student_age = np.array([27, 28, 18, 19, 22])  # numpy array
# why?????????????? bcos numpy can perform calc on all elements at once

print(student_age)


# Vectorized Operations  --> perform the same operation on every element without writing loops

arr = np.array([5, 10, 15])

print(arr + 1000)
