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
def even():
    even = []

    for i in range(1,21):
        if i % 2 == 0:
            even.append(i)
        
    print(even)

even()

#3. Factorial
#Write a Python program that calculates the factorial of a given number using a for loop.
def factorial():
    num = 7
    numStore = []
    for j in range(0, num + 1):
        if j > 0:
            if numStore !=0:
                numStore.append(j)
    print(f"Factorial of {num} is: {j}")
factorial()

#4.# Reverse String
#Write a Python program that takes a string as input and prints the reverse of that string
#using a while loop.

def reverseString():
    user_str = input("Enter a string to reverse: ")
    check = True
    
    while check:
        user_str = list(reversed(user_str))
        check = False
        print(user_str)
        
reverseString()

#5. Prime Numbers
#Write a Python program that prints all prime numbers from 2 to a given number (inclusive)
#using a for loop.
def primeCalc():
    primNumbers = []
    number =12
    for t in range(2, number+1):
        is_prime = True
        for i in range(2,int(t ** 0.5) +1):         # checking the square root of t, if it has any other value then it has factors other than itself and 1.
            if t % i == 0:
                is_prime = False
        if is_prime:
           primNumbers.append(t)
    print(primNumbers)
primeCalc()