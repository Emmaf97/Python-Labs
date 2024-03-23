# 1. Sum of Even Numbers
# Write a function named "sum_of_even_numbers" that takes a list of numbers as input.
# The function should calculate and return the sum of all even numbers in the list.
# Test the function using a sample list of numbers and print the result.
def SumEven():
    original_list = [1,2,3,4,5,6]
    number = 0
    for x in original_list:
        if x % 2 == 0:
            number += x**2
    x+=1
    print(number)
        

SumEven()

# 2. Reverse a List
# Write a function named "reverse_list" that takes a list as input.
# The function should reverse the order of elements in the list and return the reversed list.
# Test the function using a sample list and print the reversed list.
def reverseList():
    sample_list = ["Apple","Banana","Pear","Mango"]
    reverse_list = sample_list[::-1]
    print(reverse_list)

reverseList()


# 3. List Comprehension
# Write a function named "squared_numbers" that takes a list of numbers as input.
# The function should use list comprehension to return a new list containing
# the squares of all the numbers.
# Test the function using a sample list of numbers and print the resulting list of squared numbers.


# 4. Largest and Smallest Numbers
# Write a function named "find_largest_smallest" that takes a list of numbers as input.
# The function should find and return the largest and smallest numbers from the list as a tuple.
# Test the function using a sample list of numbers and print the largest and smallest numbers.

# 5. List Sorting
# Write a function named "sort_list" that takes a list of numbers as input.
# The function should sort the list in ascending order and return the sorted list.
# Test the function using a sample list of numbers and print the sorted list.


# Challenges
# 1. (Count occurrence of numbers) Write a program that reads some integers between 1
# and 100 and counts the occurrences of each. Here is a sample run of the program:


# 2. (Analyze scores) Write a program that reads an unspecified number of scores and
# determines how many scores are above or equal to the average and how many
# scores are below the average. Assume the input numbers are separated by one space in one line.


# 3. (Print distinct numbers) Write a program that reads in numbers separated by a space
# in one line and displays distinct numbers (i.e., if a number appears multiple times, it
# is displayed only once). (Hint: Read all the numbers and store them in list1. Create a
# new list list2. Add a number in list1 to list2. If the number is already in the list, ignore it.)
