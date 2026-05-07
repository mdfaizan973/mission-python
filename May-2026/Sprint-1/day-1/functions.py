# def → define function
# greet → function name
# () → parameters (empty for now)
# greet() → calling function

# # Normal Function
# def greet():
#     print("Hello World")

# greet()

# # Function with parameter 
# def greet1(name):
#     print("Hello ", name)

# greet1("Faizan")

# # Function with degault parameter
# def greet2(name = "Jhon"):
#     print("Hello ", name)

# greet2()
# greet2("Faizan")

# # Function with input
# input_name = input("Enter Name: ")

# def greet(name):
#     print("Hello", name)

# greet(input_name)


# Function with Return
# def add(a,b):
#     add = a+b
#     return add

# print(add(3,5))

# # --------------------- ************* Excercise ************* ---------------------

# 🔥 Problem 1: Greeting Function

# 👉 Create function:

# Takes name
# Prints greeting

# def greeting_function(name = "Jhon"):
#     greet = "Hello " + name
#     print(greet)

# greeting_function("Faizan")


# 🔥 Problem 2: Add Two Numbers

# 👉 Function:
# Takes 2 numbers
# Returns sum


# def add_to_number(a,b):
#     sum = a + b
#     return sum

# res = add_to_number(5 , 10)
# print(res)


# 🔥 Problem 3: Even or Odd Function

# 👉 Input number
# 👉 Return:

# "Even"
# "Odd"

# def check_even_or_odd(num):
#     if num%2==0:
#         return "Even"
#     else:
#         return "Odd"

# number = int(input("Enter Number: "))
# print(check_even_or_odd(number))


# 🔥 Problem 4: Maximum Number

# 👉 Take 2 numbers
# 👉 Return bigger number

# def find_max_number(a, b):
#     if a > b:
#         return f"{a} Is Big"
#     elif b > a:
#         return f"{b} is Big"
#     else:
#         return "Both are equal"

# num_input1 = int(input("Enter Num1: "))
# num_input2 = int(input("Enter Num2: "))

# print(find_max_number(num_input1, num_input2))



# 🔥 Problem 5: Square Function

# 👉 Input number
# 👉 Return square


# def square_function(num):
#     res = num * num
#     return res

# print(square_function(7))