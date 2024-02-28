from numpy import random
# 1. Checking Eligibility
age = int(input("Enter your age to vote: "))
if age > 17:
    print("You are able to vote")
else:
    print("You are not able to vote")
    
#2. Grading System
grade = int(input("Enter your Grade here: "))
if grade >= 90:
    print("Grade A")
elif grade >= 80 and grade < 90:
    print("Grade B")
elif grade >= 70 and grade < 80:
    print("Grade C")
elif grade >= 60 and grade < 70:
    print("Grade D")
elif grade < 60:
    print("Grade F")
#3. Even or Odd
number = int(input("Enter a number here: "))

if number % 2 != 0:
    print("This number is odd")
else:
    print("This number is even")
#4. Leap Year
year = int(input("Enter a year here: "))
#a leap year is divisible by 4 but not divisible by 100, except for years that are divisible by 400.
if year % 4 != 0 and year % 100 != 0:
    print("This is not a leap year")
elif year % 4 == 0 and year % 100 !=0:
    print("This is a leap year")
elif year % 400 == 0:
    print("This is a unique leap year")
#5. Largest Number
userNum1 = int(input("Enter the first number: "))
userNum2 = int(input("Enter the second number: "))
userNum3 = int(input("Enter the third number: "))

count = None
if userNum1 >= userNum2 and userNum1 >= userNum3:
    count = userNum1
elif userNum2 > userNum1 and userNum2 >= userNum3:
   count = userNum2
else:
    count = userNum3
print("This is the largest number",count)
#Challenges

#1. 
#Write a program that generates two integers under 100 and
#prompts the user to enter the sum of these two integers. The program then reports
#true if the answer is correct, false otherwise. Here is a sample run.
num1 = random.randint(100)
num2 = random.randint(100)
# print("This is a random number", num1)
# print("This is a random number", num2)
calcNumber = int(input(f"What will be the out put for {num1} + {num2} be: "))
if calcNumber == num1+num2:
    print(f"The sum of {num1} and {num2} is: {num1 + num2} your answer is True")
else:
    print(f"The sum of {num1} and {num2} is: {num1 + num2} your answer is False")
    
    
#2. 
import sys
# The US federal personal income tax is calculated based on the filing status and
# taxable income. There are four filing statuses: single filers, married filing jointly,
# married filing separately, and head of household. Using the taxes.py file on the LMS
# complete the program based on the following rates.

# Prompt the user to enter filing status
status = int(input("Enter the filing status: "))

# Prompt the user to enter taxable income
income = float(input("Enter the taxable income: "))

# Compute tax
tax = 0

if status == "single":  # Compute tax for single filers
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income <= 82250:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (income - 33950) * 0.25
    elif income <= 171550:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (82250 - 33950) * 0.25 + (income - 82250) * 0.28
    elif income <= 372950:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
            (income - 171550) * 0.33
    else:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
              (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
              (372950 - 171550) * 0.33 + (income - 372950) * 0.35;
elif status == "married": # Compute tax for married file jointly
    if income <= 16700:
        tax = income * 0.10
    elif income <= 67900:
        tax = 16700 * 0.10 + (income - 16700) * 0.15
    elif income <= 137050:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
            (income - 67900) * 0.25
    elif income <= 208850:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
            (137050 -  67900) * 0.25 + (income - 137050) * 0.28
    elif income <= 372950:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
            (137050 -  67900) * 0.25 + (208850 - 137050) * 0.28 + \
            (income - 171550) * 0.33
    else:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
            (137050 -  67900) * 0.25 + (208850 - 137050) * 0.28 + \
            (372950 - 208850) * 0.33 + (income - 372950) * 0.35;
elif status == "married separately": # Compute tax for married separately
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income <= 68525:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (income - 33950) * 0.25
    elif income <= 104425:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (68525 - 33950) * 0.25 + (income - 68525) * 0.28
    elif income <= 186475:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28+ \
            (income - 104425) * 0.33
    else:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28+ \
            (186475 - 104425) * 0.33 + (income - 186475) * 0.35;
elif status == "head of household": # Compute tax for head of household
    if income <= 11950:
        tax = income * 0.10
    elif income <= 45500:
        tax = 11950 * 0.10 + (income - 11950) * 0.15
    elif income <= 117450:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
            (income - 45500) * 0.25
    elif income <= 190200:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
            (117450 - 45500) * 0.25 + (117450 - 68525) * 0.28
    elif income <= 372950:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
            (117450 - 45500) * 0.25 + (117450 - 68525) * 0.28 + \
            (income - 190200) * 0.33
    else:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
            (117450 - 45500) * 0.25 + (117450 - 68525) * 0.28 + \
            (372950 - 190200) * 0.33 + (income - 372950) * 0.35;
else:
    print("Error: invalid status")
    sys.exit()

# Display the result
print("Tax is", tax)