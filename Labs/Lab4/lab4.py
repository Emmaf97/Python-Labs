import numpy
#1a. Create a Python function named "calculate_area_of_circle" that takes the
#radius of a circle as an argument and returns the area of the circle. Use the
#formula: area = π * radius^2.

user_input = int(input("Enter a radius to calculate area of a cirlce: "))

def calculate_area_of_circle(radius):
    area = numpy.pi * (radius ** 2)
    print(f"the area of the circle if", area)
    return area
    
calculate_area_of_circle(user_input)

#1b. Test your function by calling it with a radius of 5 and printing the result.
#result should be 78.53982 or 78.54

#1c. Create another Python function named "calculate_hypotenuse" that takes
#the lengths of two sides of a right-angled triangle as arguments and returns
#the length of the hypotenuse. Use the formula: hypotenuse = sqrt(side1^2 + side2^2), where sqrt() is the square root function.
# expected answer with angles of 5 for a and b is 7.07
angle1 = int(input("Enter a radius to calculate area of a cirlce: "))
angle2 = int(input("Enter a radius to calculate area of a cirlce: "))

def calculate_hypotenuse(angle1, angle2):
    side1 = angle1 ** 2
    side2 = angle2 ** 2
    hypotenuse =  numpy.sqrt((side1 + side2))
    print(f"the hypotenuse of angle1 and angle2 is: ", int(hypotenuse))

calculate_hypotenuse(angle1, angle2)

#1d. Test your function by calling it with side1 = 3 and side2 = 4, and printing the result.
#expected output is 5.0
#2a. Create a Python string variable named "sentence" and assign it the value "Hello, World!".
sentence = "Hello World!"

#2b. Print the length of the string using the len() function.
print(len(sentence))

#2c. Print the string in uppercase using the upper() method.
print(sentence.upper())

#2d. Create a new string variable named "modified_sentence" and assign it the value of "sentence" with "Hello" replaced by "Goodbye".
modified_sentence = sentence.replace("Hello","Goodbye")

#2e. Print the modified sentence.
print(modified_sentence)

#2f. Create a new string variable named "reversed_sentence" and assign it the
#value of "sentence" reversed using slicing.
reversed_sentence = sentence[::-1]

#2.g Print the reversed sentence.
print(reversed_sentence)


# (Financial application: payroll) Write a program that reads the following information
# and prints a payroll statement:
# Employee’s name (e.g., Smith)
# Number of hours worked in a week (e.g., 10)
# Hourly pay rate (e.g., 9.75)
# Federal tax withholding rate (e.g., 20%)
# State tax withholding rate (e.g., 9%)

def calculatePayroll(name,hours,payrate,fedtax,statetax):
    gross = hours * payrate
    fedValue =  gross * fedtax
    stateValue = gross * statetax
    totalDeductions = fedValue + stateValue
    netPay = gross - totalDeductions
    print("-----------------")
    print("-----------------")
    print(f"Employee Name: {name}")
    print(f"Hours Worked: {hours}")
    print(f"Hours Worked: {payrate}")
    print(f"Gross Pay: {gross}")
    print("-----------------")
    print("Deductions")
    print("-----------------")
    print(f"  Federal tax withholding rate: ({fedtax * 100}%) : ${fedValue}")
    print(f"  Federal tax withholding rate: ({statetax * 100}%) : ${stateValue}")
    print(f"  Total Deduction:   ${totalDeductions}")
    print(f"Net Pay: {netPay}")
    
name = input("Enter Employee Name: ")
hours = int(input("Enter hours worked: "))
payrate = int(input("Enter hourly payrate: "))
fedtax = float(input("Enter Federal tax withholding rate: "))
statetax = float(input("State tax withholding rate: "))

calculatePayroll(name, hours, payrate, fedtax, statetax)

# inclass notes on slicing
my_list = ("apple", "Orange", "Strawberries","Kiwi")

# slice l[<start>:<stop>]
my_list1 = my_list[1:3]
#print(my_list1)

# slice l[<start>:<stop>:step] #e.g. step
my_list2 = my_list[0:3:2]
#print(my_list2)

 # slice l[<start>:<stop>:-1]   #e.g. -1
my_list3 = my_list[3:0:-2]
#print(my_list3)

 # slice l[:<stop>]             #e.g. start not specified
my_list4 = my_list[:3]
#print(my_list4)

# slice l[<start>:]            #e.g. stop  not specified
my_list5 = my_list[2:]
#print(my_list5)

# slice l[::-1]                #e.g. for reverse
my_list6 = my_list[::-2]
#print(my_list6)