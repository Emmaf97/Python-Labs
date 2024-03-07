# 1. Sum of Numbers
#Write a Python program that calculates the sum of all numbers from 1 to a given number
#(inclusive). Use a for loop to iterate through the numbers.
count = 0
for x in range(1, 5):
    count += x
    print(count)

# 2. Even Numbers
#Write a Python program that prints all even numbers from 1 to a given number (inclusive).
#Use a while loop to iterate through the numbers.

even = []

for i in range(1,21):
    if i % 2 == 0:
        even.append(i)
        
print(even)

#3. Factorial
#Write a Python program that calculates the factorial of a given number using a for loop.

#4.# Reverse String
#Write a Python program that takes a string as input and prints the reverse of that string
#using a while loop.

#5. Prime Numbers
#Write a Python program that prints all prime numbers from 2 to a given number (inclusive)
#using a for loop.