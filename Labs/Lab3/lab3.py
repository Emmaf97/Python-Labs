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
if userNum1 > userNum2 and userNum3:
    count = userNum1
elif userNum3 > userNum1 and userNum2:
   count = userNum3
elif userNum2 > userNum1 and userNum3:
    count = userNum2
print(count)
#Challenges

#1. 

#2. 

#3. 