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


# 1. (Count positive and negative numbers and compute the average of numbers) Write a
# program that reads an unspecified number of integers, determines how many
# positive and negative values have been read, and computes the total and average of
# the input values (not counting zeros). Your program ends with the input 0. Display
# the average as a floating-point number.
def numberCheck():
    countpos = 0
    countneg = 0
    totalInputs = 0
    total = 0
    
    while True:
        user_input = input("Enter a number or type 'done' to finish: ")
        
        if user_input.lower() == "done":
            break
        
        number  = int(user_input)
        total += number
        totalInputs += 1
        

        if number > 0:
             countpos +=1
        if number < 0:
            countneg +=1
        
    
        average = total / totalInputs
    
    if totalInputs > 0:
        print(f"The number of positive numbers is: {countpos}")
        print(f"The number of negative numbers is: {countneg}")
        print(f"Total is equal to: {total}")
        print(f"The average is: {average}")
    else:
        ("No Numbers Entered")
        
    
numberCheck()


# 2. (Conversion from kilograms to pounds and pounds to kilograms) Write a program
# that displays the following two tables side by side (note that 1 kilogram is 2.2 pounds
# and that 1 pound is .45 kilograms): Your solution should have 199 rows.
def convertkg():
    pounds = 20
    One_pound = 2.2
    One_KG = 0.45
    print("---------------------------------------------")
    print("Kilograms    Pounds      ||       Pounds       Kilograms")
    for i in range(1, 200):
        new_pound = One_KG * pounds
        #print("Kilograms          Pounds                ||        Pounds         Kilograms")
        print(f"{i:<13} {f'{One_pound:.1f}':<10} {f'||':<10} {pounds:<12} {new_pound:.2f}")
        i += 1
        pounds += 5
        One_pound += 2.2
        
    print("---------------------------------------------")
convertkg()


#(Display a pyramid) Write a program that prompts the user to enter an integer from
# 1 to 15 and displays a pyramid.
