# create functions like add, subtract, divide, multiply
# input the numbers e.g a and b
# ask for operation like +,-,/,* 


def add_num(a,b):
    return a+b

def sub_num(a,b):
    return a-b

def div_num(a,b):
    return a/b

def mul_num(a,b):
    return a*b


print("Calculator")

num1 = int(input("Enter Num-1: "))
num2 = int(input("Enter Num-2: "))

print("1 For Add")
print("2 For Subtraction")
print("3 For Divide")
print("4 For Multiply")

operation = int(input("Enter Operation Number: "))


if operation == 1:
    print(add_num(num1, num2))

elif operation == 2:
    print(sub_num(num1, num2))

elif operation == 3:
    print(div_num(num1, num2))

elif operation == 4:
    print(mul_num(num1, num2))

else:
    print("Invalid Opetration")

