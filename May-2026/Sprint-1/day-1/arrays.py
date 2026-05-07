# numbers = [10, 20, 30, 40]

# print(numbers) # print array
# print(numbers[0])   # first element
# print(numbers[1])   # second element
# print(numbers[2])   # third element
# print(numbers[-1])   # last element

# modify array element
# numbers[0] = 100

# # Add Element
# numbers.append(99) # adds at the end
# numbers.insert(0, 5) # adds at the 0th position

# # Remove Element
# numbers.remove(20) # removes mentioned element
# numbers.pop() # removes last element | pop(0) here 0th index element will be removed

# print(numbers)


# Array with input and loop
arr = []
n = int(input("How many numbers? "))

for i in range(n):
    num = int(input("Enter Number: "))
    arr.append(num)

print(arr)
