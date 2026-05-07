# # starts from 0
# for i in range(5):
#     print(i)

# # start from 1
# for i in range(1, 10):
#     print(i)

# # print Hello World 5 times
# for i in range(5):
#     print("Hello World :", i+1) 


# print no using while

# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1



# # --------------------- ************* Excercise ************* ---------------------

# 🔥 Problem 1: Count Numbers

# 👉 Print numbers from 1 to N

# Input:
# Enter number: 5
# Output:
# 1 2 3 4 5

# 👉 Try:

# Using for
# Using while

# # solution

# number1 = int(input("Enter No: "))

# for i in range(number1):
#     print(i+1)



# 🔥 Problem 2: Sum of Numbers

# 👉 Find sum from 1 to N

# Input:
# Enter number: 5
# Output:
# Sum = 15

# # solution

# number2 = int(input("Enter No: "))

# sum = 0
# for i in range(number2):
#     sum = sum + (i+1)

# print(sum)



# 🔥 Problem 3: Even Numbers in Range

# 👉 Print all even numbers from 1 to N

# Input:
# Enter number: 10
# Output:
# 2 4 6 8 10

# # solution

# number3 = int(input("Enter Number: "))

# for i in range(1, number3+1):
#     if i % 2 == 0:
#         print(i)


# 🔥 Problem 4: Multiplication Table

# 👉 Print table of a number

# Input:
# Enter number: 3
# Output:
# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 10 = 30

# # solution

# number4 = int(input("Enter Number: "))

# for i in range(1, 11):
#     print(number4, "x", i, "=", number4 * i)


# 🔥 Problem 5: Reverse Counting

# 👉 Print numbers from N to 1

# Input:
# Enter number: 5
# Output:
# 5 4 3 2 1

# number5 = int(input("Enter Number: "))

# for i in range(number5, 1, -1):
#     print(i)

