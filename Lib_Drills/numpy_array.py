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

arr * 2  # multiply same value with every element


# Indexing
# Index = position number of a array

tea = [10, 20, 30]
# in python
print(tea[1])


# Slicing -- extracting a portion of data

arr2 = np.array([10, 20, 30, 40, 50, 60, 400])
# means start at index 0 and stop before index 4
arr2[1:4]


# shape -- how data is organized means
# how many dimensions your data has
# and how many items exists in each dimension


# python
# arr.shape

jira = np.array([100, 546, 4888, 23131, 46542118])

print(jira.shape)

# 4 elements
# 1 dimension


twor = np.array([[10, 20, 30], [40, 50, 60]])  # 3 elements
# 2 dimension

three_d_arr = np.array([[10, 20, 3, 30], [40, 232, 50, 60], [70, 3534, 80, 90]])
# 4 elements
# 3 dimension


print(twor.shape)

print(three_d_arr.shape)


my_marks = np.array([80, 90, 70, 60, 100])

# sum   --add values together

print(my_marks.sum())

# Mean   - Sum of values / Number of values
print(my_marks.mean())

# Max - returns the largest value
print(my_marks.max())
# Min - Returns the smallest value.
print(my_marks.min())


salary = np.array([30000, 40000, 50000, 60000, 70000])

print("Total Salary:", salary.sum())
print("Average Salary:", salary.mean())
print("Highest Salary:", salary.max())
print("Lowest Salary:", salary.min())
