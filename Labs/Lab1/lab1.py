# Prompt the user for input
#seconds = int(input("Enter an integer for seconds: "))

# Get minutes and remaining seconds
#minutes          = 0    # Find minutes in seconds
#remaining_seconds = 0   # Seconds remaining
#print(seconds, "seconds is", minutes,  
#   "minutes and", remaining_seconds, "seconds")


#TASK: Now alter to import time and use time.time()
#       instead of user input of seconds
import time

currentTime = time.time() # Get current time

# # Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)

# # Get the current second 
currentSecond = totalSeconds % 60 

# # Obtain the total minutes
totalMinutes = totalSeconds // 60 

# # Compute the current minute in the hour
currentMinute = totalMinutes % 60

# # Obtain the total hours
totalHours = totalMinutes // 60

# # Compute the current hour
currentHour = totalHours % 24

# # Display results
print("Total Seconds is: ", totalSeconds)
print("Current Second: ", currentSecond)
print("Total Minutes is: ", totalMinutes)
print("Current Minute: ", currentMinute)
print("Total Hours: ", totalHours)
print("Current Hour: ", currentHour)
print("Current time is", currentHour, ":", 
    currentMinute, ":", currentSecond, "GMT")


"""
Write a program to let a first grader practice additions. 

The program randomly generates two single-digit integers 
number1 and number2 and displays a question such as:
 “What is 7 + 9?” 
 to the student. 

After the student types the answer, 
the program displays a message to indicate whether the answer
is true or false
"""
import random 

# Generate random numbers
num1 = random.randint(0,10)
num2 = random.randint(0,10)

# Prompt the user to enter an answer
user_input = int(input(f"What is {num1} + {num2}?: "))

# Display result 
if user_input == num1 + num2:
    print("Your answer is True")
else:
    print("Your answer is False")  
    
    
"""
Write a program that prompts the user to enter an integer. 
If the number is a multiple of 5, print HiFive. 
If the number is divisible by 2, print HiEven.

"""
number = int(input("Enter an integer: "))

if number % 5 == 0:
    print("HiFive")
elif number % 2 == 0:
    print("HiEven")
else:
    print("not a valid number")
    
    
"""
Write a program to show a beginner new to subtraction
how to do random subtractions of single digit numbers.

The program should randomly generate two single-digit integers 
number1 and number2 (with number1 >= number2) and 
displays a question such as 
“What is 9 minus 2?” to the student. 

After the student types the answer, the program displays a message 
to indicate whether the answer is correct.
"""
import random

# 1. Generate two random single-digit integers
num1 = random.randint(0,9)
num2 = random.randint(0,9)

# 2. If number1 < number2, swap number1 with number2
if num1 > num2:
    num1 = num1

# 3. Otherwise number1, number2 order
if num2 > num1:
    num1, num2 = num2, num1

# 4. Prompt the student to answer "what is number1 - number2?"
user_input = int(input(f"what is {num1} + {num2}? "))

# 5. Check the answer and display the result
if user_input == num1 + num2:
    print("Your answer is True")
else:
    print("Your answer is False")
    
"""
Body Mass Index (BMI) is a measure of health on weight. 
It can be calculated by taking your weight in kilograms and 
dividing by the square of your height in meters. 
The interpretation of BMI for people 16 years or older is as follows:
+-------------+-----------------------+
| BMI         | Category              |
+-------------+-----------------------+
| < 18.5      | Underweight           |
| 18.5 - 24.9 | Normal weight         |
| 25 - 29.9   | Overweight            |
| >= 30       | Weight Issue (Class 1)|
+-------------+-----------------------+
"""
def KG_PER_POUND():
    return 0.45359237   # Constant
def MTR_PER_INCH():
    return 0.0254       # Constant 

# Prompt the user to enter weight in pounds
pounds = float(input("Enter your weight in pounds: "))
    
# Prompt the user to enter height in inches
inches = float(input("Enter your height in inches: "))
    
  
# Compute BMI
#   bmi = weightInKilograms divided-by heightInMeters-squared)
weight = pounds *  KG_PER_POUND() #* 2.205 # kg conversion
height = inches * MTR_PER_INCH() #39.37) ** 2  # meter conversion
print("Weight is: ", weight)
print("Height is: ", height)
bmi = weight / (height ** 2)
print("BMI is: ", bmi)
# Display result according to above table
if bmi < 18.5:
    print("Underweight")
elif  18.5 < bmi < 24.9:
    print("Normal Weight")
elif bmi > 25 and bmi < 29.9:
    print("Overweight")
elif bmi >= 30:
    print("Weight Issue (class 1)")
    
"""
The US federal personal income tax is calculated based on the filing status 
and taxable income. 
Suppose we look at just one filing status: 
    single filers 
Example tax rates for are shown below.
+----------------------+-----------------------+---------------------------------+
| Taxable Income Range | Single Filer Rate (%) | Married Filing Jointly Rate (%) |
+----------------------+-----------------------+---------------------------------+
| $0 - $9,950          | 10                    | 10                              |
| $9,951 - $40,525     | 12                    | 12                              |
| $40,526 - $86,375    | 22                    | 22                              |
| $86,376 - $164,925   | 24                    | 24                              |
| $164,926 - $209,425  | 32                    | 32                              |
| $209,426 - $523,600  | 35                    | 35                              |
| Over $523,600        | 37                    | 37                              |
+----------------------+-----------------------+---------------------------------+

Write a program to ask a user a series of 
questions taking in their details and 
using the data from the above table, 
show their tax breakdown (% rate)

Ignore other tax details from the real-world for now

"""
import sys
# Prompt the user to enter filing status
status = input("Enter the filing status: ")

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