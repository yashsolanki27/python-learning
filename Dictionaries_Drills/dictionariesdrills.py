# Create
employee = {"id": 101, "name": "Yash", "role": "Python Developer", "salary": 90000}

# Access
print(employee["name"])

# Safe Access
print(employee.get("salary"))

# Add
employee["city"] = "Hyderabad"

# Update
employee["salary"] = 100000

# Remove
employee.pop("role")

# Keys
print(employee.keys())

# Values
print(employee.values())

# Key-Value Pairs
print(employee.items())

# Check Key
print("name" in employee)

# Loop
for key, value in employee.items():
    print(f"{key} : {value}")

# Nested Dictionary
employee["address"] = {"city": "Hyderabad", "country": "India"}

print(employee["address"]["city"])
