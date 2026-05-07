# 🔥 Problem 1: Even / Odd + Zero Case

# 👉 Input:

# A number

# 👉 Output:

# If number = 0 → "Zero"
# If even → "Even Number"
# If odd → "Odd Number"
# num = int(input("Enter num: "))

# if num == 0:
#     print("Zero")
# elif num % 2 ==0:
#     print("Even Number")
# else: 
#     print("Odd Number")



# 🔥 Problem 2: Pass / Fail + Distinction

# 👉 Input:

# Marks

# 👉 Rules:

# ≥ 75 → "Distinction"
# ≥ 40 → "Pass"
# < 40 → "Fail"

# 👉 Output example:

# Enter marks: 80
# Distinction

# solution
# math_marks = int(input("Enter Math Marks: "))

# if math_marks >= 75:
#     print("Distinction")
# elif math_marks >= 40:
#     print("Pass")
# elif math_marks < 40:
#     print("Fail")




# 🔥 Problem 3: Largest of Two Numbers

# 👉 Input:

# Two numbers

# 👉 Output:

# Enter first number: 10
# Enter second number: 20

# 20 is greater

# 👉 Edge case:

# If both equal → "Both are equal"

# largest_first_numbers = int(input("Enter First Number: "))
# largest_second_numbers = int(input("Enter Second Number: "))

# if largest_first_numbers == largest_second_numbers:
#     print("Both are equal")
# elif largest_first_numbers > largest_second_numbers:
#     print(largest_first_numbers , "is greater")
# else:
#     print(largest_second_numbers , "is greater")




# 🔥 Problem 4: Positive / Negative / Zero

# 👉 Input:

# A number

# 👉 Output:

# "Positive"
# "Negative"
# "Zero"

# number = int(input("Enter Number: "))

# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")



# 🔥 Problem 5: Simple Login Check (Important 🔥)

# 👉 Input:

# username
# password

# 👉 Conditions:

# username = "admin"
# password = "1234"

# 👉 Output:

# Correct → "Login Successful"
# Wrong → "Invalid Credentials"

# username = input("Enter User Name ")
# password = input("Enter Password ")

# if username == "admin" and password == "1234":
#     print("Login Successful")
# else:
#     print("Invalid Credentials")