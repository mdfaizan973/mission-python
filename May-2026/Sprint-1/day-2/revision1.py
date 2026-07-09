# Factiruak if a number

def fact(number):
        if number == 0:
            return 1
        else:
            return number * fact(number-1)


print(fact(5))

# Fibonacci Series

# formula for fibonacci series is 
# f(n) = f(n-1) + f(n-2)

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


for i in range(10):
    print(fib(i))
