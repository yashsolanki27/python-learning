import pandas as pd

# # pandas stores it as a dataframe

# # Read CSV files   comma seprated value
# df = pd.read_csv("employees.csv")

# print(df)

# # head()--->  Shows first 5 rows.
# print(df.head(2))

# # Shape  ---> tells (row and column)
# print(df.shape)


# # Select One Column  ---> df["column_name"]

# df = pd.read_csv("employees.csv")

# print(df["Age"])


# # Filter Rows  --->> df[df["column"] > value]

# high_salary = df[df["Salary"] >= 50000]

# print(high_salary)


# # group by

data = {
    "Name": ["Yash", "John", "Ram", "Amit"],
    "Department": ["IT", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 40000, 50000],
}


emp_df = pd.DataFrame(data)


print(emp_df.groupby("Department")["Salary"].mean())
print(emp_df.groupby("Department")["Salary"].sum())


##final program to cover all stuff


# Read CSV
df = pd.read_csv("employees.csv")

# Preview first 5 rows
print("\nHEAD")
print(df.head())

# Rows and columns
print("\nSHAPE")
print(df.shape)

# Select one column
print("\nSALARY COLUMN")
print(df["Salary"])

# Filter
print("\nSALARY > 50000")
print(df[df["Salary"] > 50000])

# Group By Average
print("\nAVERAGE SALARY BY DEPARTMENT")
print(df.groupby("Department")["Salary"].mean())
