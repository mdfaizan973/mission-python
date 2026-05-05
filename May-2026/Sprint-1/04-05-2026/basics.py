# Learning

# print("Hello World")
# print(10)

# str = "faizan"
# print(str)

# num = 100
# print(num)

# name = input("Enter name: ")
# print("Hello "+ name)

# money = input("Enter money: ")
# print(money + " rs")

# input_num = int(input("Enter Num: "))
# pring(input_num)

# -------------------------------***********Excercise**********------------------------------


# 🔥 Problem 1: Personalized Greeting

# Take user name and age, then print:

# 👉 Example:
# Enter name: Faizan
# Enter age: 22

# 👉 Output:
# Hello Faizan, you are 22 years old

# Solution

# user_name = "Faizan"
# user_age = 22
# print("Hello " + user_name + ", you are " + str(user_age) + " years old")

# using input
# input_name = input("Enter Name: ")
# input_age = input("Enter age: ")
# print("Hello " + input_name + " you are " + input_age + " years old")


# 🔥 Problem 2: Year of Birth

# Take age as input and calculate:

# 👉 Formula:
# birth_year = 2026 - age

# 👉 Output:
# You were born in 2004
# ⚠️ Hint: use int(input())

# Solution

# age = int(input("Enter your age: "))
# birth_year = 2026 - age
# print(birth_year)


# 🔥 Problem 3: Swap Two Values (Important 🔥)

# Take two numbers from user and print them swapped

# 👉 Example:

# a = 5
# b = 10

# 👉 Output:

# a = 10
# b = 5

# ⚠️ Think before coding

# solution
# a = 5
# b = 10

# temp = a
# a = b
# b = temp
# ----
# b = b - a
# a = a + b

# print(a, b)


# 🔥 Problem 4: Simple Interest

# Take:

# principal
# rate
# time

# 👉 Formula:

# SI = (P * R * T) / 100

# 👉 Output:

# Simple Interest is: 500

# solution
# P = int(input("Enter P: "))
# R = int(input("Enter R: "))
# T = int(input("Enter T: "))

# SI = (P * R * T) / 100

# print(SI)


# 🔥 Problem 5: Full Name Formatter

# Take:

# first name
# last name

# 👉 Output:

# Your full name is: Faizan Khan

# 👉 Bonus:
# Print in uppercase (if you know)

# Solution

# first_name = "md"
# last_name = "faiZan"

# print(first_name.upper() + last_name.upper()) # MDFAIZAN
# print(first_name.lower() + last_name.lower()) # mdfaizan
# print(first_name.title() + last_name.title()) # MdFaizan


# 🔥 Problem 6: Total Marks

# Take marks of 3 subjects:

# 👉 Output:

# Total = 240
# Average = 80

# solution

# math = 80
# english = 90
# hindi = 70

# sum = math + english + hindi
# print("Total = " + str(sum))
# print("Average = " + str(sum / 3))


# 🔥 Problem 7: String + Number Mix (Important Concept)

# Take user name and number of items:

# 👉 Output:

# Faizan bought 3 items

# 👉 Learn:
# Mixing text + number in print

# solution
# userName = "Faizan"
# userItems = 3
# print(userName , "bought" , userItems , "items" )


# 🔥 Problem 8: Area of Rectangle

# Take:

# length
# width

# 👉 Output:

# Area = 50

# l = 10
# b = 5

# print(l*b)
