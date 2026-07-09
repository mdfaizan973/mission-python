
# ? 1. Maximum of Three Numbers

# Write a program to find the maximum among three numbers.

# Solution-1
# num1 = 20
# num2 = 34
# num3 = 45

# if num1 > num2 and num1 > num3:
#     print(f"Miximum is {num1}")
# elif num2 > num1 and num2 > num3:
#     print(f"Miximum is {num2}")
# else:
#     print(f"Miximum is {num3}")

# Solution-2
# num = [20, 40, 25]

# max = num[0]

# for i in num:
#     if max < i:
#         max = i

# print(max)


# ? 2. Element present in the List

# Write a function to check if the number/element is present in list.

# Solution

# def check_number_in_list(ele):
#     list = [2,4,6,34]
#     if ele in list:
#         return "Yes"
#     else:
#         return "No"

# print(check_number_in_list(20))



# ? 3. Even or Odd

# Write a Python function to check whether a number is even or odd.

# Solution

# def check_even_odd(num):
#     if num == 0:
#         return f"{num} is Zero"
#     elif num % 2 == 0:
#         return f"{num} is Even Number"
#     else:
#         return f"{num} is Odd Number"


# print(check_even_odd(9))
# print(check_even_odd(12))


# ? 4. Positive, Negative or Zero

# Write a program to check whether a number is positive, negative, or zero.

# Solution

# def check_pove_neve(num):
#     if num == 0:
#         return "This is Zero"
#     elif num > 0:
#         return "This is +Ve"
#     else:
#         return "This is -Ve"

# print(check_pove_neve(-23))
# print(check_pove_neve(67))

# ? 5. Vowel or Consonant

# Write a Python function to check whether a character is a vowel or consonant.

# Solution

def check_vowel_cons(char):
    vowels = "aeiou"
    # return "vowels" if char in vowels else "consonant" 
    if char in vowels:
        return "vowel"
    else:
        return "consonant"

# print(check_vowel_cons("a"))
# print(check_vowel_cons("b"))

# ? 6. Leap Year Check

# Write a function to check whether a given year is a leap year or not.

# def check_leap_year(year):
#     if year % 400 == 0:
#         return f"{year} is Leap year"
#     elif year % 4 == 0 and year % 100 != 0:
#         return f"{year} is Leap year"
#     else:
#         return f"{year} is Not Leap year"

# print(check_leap_year(2001))  # Not a leap year
# print(check_leap_year(2004))  # Leap year
# print(check_leap_year(1900))  # Not a leap year
# print(check_leap_year(2000))  # Leap year
# print(check_leap_year(2024))  # Leap year

# Solution

# ? 7. Factorial of a Number

# Write a Python program to find the factorial of a number.

# Solution

# def fectorial_of_number(num):
#     if num <= 1:
#        return num

#     return num * fectorial_of_number(num-1)

# print(fectorial_of_number(4))

# ? 8. Reverse a String

# Write a program to reverse a given string.

# Solution

# string = "helloworld"
# reversed_string = ""

# for char in string:
#     reversed_string = char + reversed_string

# print(reversed_string)

# ? 9. Sort a List in Ascending Order

# Write a program to display a list in ascending order.
# listArr = [3,7,2,5,9,1,6]
# # listArr.sort()
# print(sorted(listArr))

# Solution

# ? 10. Sum of First N Natural Numbers

# Write a program to find the sum of first N natural numbers.

# def sum_of_natural_numbers(num):
#     sum = 0
#     for i in range(1, num+1):
#         sum += i
    
#     return sum
    
# print(sum_of_natural_numbers(10))

# Solution

# ? 11. Swap Two Numbers

# Write a program to swap two numbers without using a third variable.

# Solution

# num1 = 5
# num2 = 4

# temp = num1
# num1 = num2
# num2 = temp


# # num1 = num1 + num2
# # num2 = num1 - num2
# # num1 = num1 - num2

# print(num1)
# print(num2)

# ? 12. Check Prime Number

# Write a program to check whether a number is prime or not.

def check_prime(num):
    if num <= 1:
        return f"{num} Not Prime"

    for i in range(2, num):
        if num % i == 0:
            return f"{num} Not Prime"

    return f"{num} Prime"

# print(check_prime(0))
# print(check_prime(1))
# print(check_prime(2)) 
# print(check_prime(3))
# print(check_prime(4))
# print(check_prime(5))
# print(check_prime(6))
# print(check_prime(7))
# print(check_prime(8))
# print(check_prime(9))

# Solution

# ? 13. Fibonacci Series

# Write a program to generate Fibonacci series up to N terms.

# Solution

# def fibbonacci_series(num):
#     if num <= 1:
#         return num

#     return fibbonacci_series(num-1) + fibbonacci_series(num-2)


# for i in range(5):
#     print(fibbonacci_series(i))

# ? 14. Find Smallest Among Three Numbers

# Write a program to find the smallest among three numbers.

# Solution

# ? 15. Count Digits in a Number

# Write a program to count the number of digits in a given number.

# nums = 343233434

# temp = len(str(nums))

# # for i in range
# print(temp)

# Solution

# ? 16. Sum of Digits

# Write a program to find the sum of digits of a number.

# Solution

# ? 17. Palindrome Number Check

# Write a program to check whether a number is a palindrome or not.

# Solution

# ? 18. Palindrome String Check

# Write a program to check whether a string is a palindrome or not.

# Solution

# ? 19. Find Maximum Element in a List

# Write a program to find the largest element in a list.

# Solution

# ? 20. Count Vowels in a String

# Write a program to count the number of vowels in a given string.

# Solution

string = "hfeoisdfhoieunfdsf"
vowels = "aeiou"
count = 0
v = ""
for i in string:
    if i in vowels:
       count = count+1
       v = v+i

print(count)
print(v)
