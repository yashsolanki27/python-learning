import pandas as pd

# pandas stores it as a dataframe

# Read CSV files   comma seprated value
df = pd.read_csv("employees.csv")

print(df)

# head()--->  Shows first 5 rows.
print(df.head(2))

# Shape  ---> tells (row and column)
print(df.shape)


# Select One Column  ---> df["column_name"]

df = pd.read_csv("employees.csv")

print(df["Age"])
