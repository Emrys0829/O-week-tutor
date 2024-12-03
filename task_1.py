# This file gives solution to determine an integer that a list represent
# Created by: Emrys Pham
# Created date: 03/12/2024
# Version 3.12.4

"""
An integer 8745 can be rewrited as 8000 + 700 + 40 + 5
The digit of the first number of the list is length of the list minus one and the digit of the second number is the length of the list minus two and so on until the last number
To go through each number of the list we use a for loop and for each loop we add the numbers together.
"""

def convert_to_int(list_of_numbers: list) -> int:
    """
    This function convert a list of numbers to a single integer
        @para: list_of_numbers
            A list of integers
        @return: 
            An interger
    """ 
    digit_of_the_number = len(list_of_numbers) - 1 #Get the digit of the first number
    solution_integer = 0 #Assign 0 to the solution integer
    for number in list_of_numbers:
        solution_integer = solution_integer + number * (10 ** digit_of_the_number) #Add the all the number up to get the final solution_integer
        digit_of_the_number = digit_of_the_number - 1
    return solution_integer    

#Examples  
print(convert_to_int([0]))
print(convert_to_int([3,2,1,8,9,7]))



