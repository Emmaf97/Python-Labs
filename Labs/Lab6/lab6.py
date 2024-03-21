# 1. Celsius to Fahrenheit Conversion
# Write a Python function that converts a temperature from Celsius to Fahrenheit. The
# function should take a temperature in Celsius as an argument and return the
# equivalent temperature in Fahrenheit.

def tempConvert():
    user_input = int(input("Enter a temperature in celsius: "))
    fahrenheit = (user_input * 9/5) + 32
    
    print(f"{user_input} degrees Celsius is {fahrenheit} degrees Fahrenheit")

tempConvert()

#2. Maximum of Three Numbers
# Write a Python function that takes three numbers as arguments and returns the
# maximum of the three numbers.


#3. Palindrome Check
# Write a Python function that checks whether a given string is a palindrome or not.
# The function should take a string as an argument and return True if it is a
# palindrome, and False otherwise.
def palindrome_Check():
    string1 = input("Enter String1: ")
    reversed_string = string1[::-1]
    
    if reversed_string == string1:
        print(f"{string1} is a palindrome")
    else:
        print(f"{string1} this is not a palindrome")
    

palindrome_Check()

#4. Factorial Calculation
# Write a Python function that calculates the factorial of a given number. The function
# should take an integer as an argument and return its factorial.

#5. Sum of Squares
# Write a Python function that calculates the sum of squares of numbers from 1 to a
# given number. The function should take a positive integer as an argument and return
# the sum of squares.