# 🔥 Problem 1: Student Info
# Create:
# name, age, marks
# Print all values

student_info = {
    "name": "Fizzy",
    "age" : 22,
    "city" : "mumbai",
    "marks": 250
}


# 🔥 Problem 2: Update Marks
# Increase marks by 10
student_info["marks"] = student_info["marks"] + 10

# 🔥 Problem 3: Add City
# Add new key city

student_info["city"] = "ranchi"

# 🔥 Problem 4: Remove Age
# Delete age key

del student_info["age"]

# 🔥 Problem 5: Print Keys Only
# 👉 Output:
# name
# marks
# city

print(student_info)

for key in student_info:
    print(key, ":" , student_info[key])
