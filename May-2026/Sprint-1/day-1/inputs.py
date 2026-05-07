
# string = input("Enter Name: ")
# print(string)

# number = int(input("Enter Number: "))
# print(number)

# string_Arr = input("Enter numbers separated by space: ").split()
# print(string_Arr)

# num_arr = list(map(int, input("Enter numbers: ").split()))
# print(num_arr)


arr = []

n = int(input("How many numbers? "))

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

print(arr)