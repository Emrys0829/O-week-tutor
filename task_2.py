# A guessing game of a number between 1 and 100
# Created by: Emrys Pham
# Created date: 03/12/2024
# Version 3.12.4

'''
The solution to the problem is staightfoward. If the guess is higher than the secret number. 
We print 'lower' if not we print 'higher'.
When the guess number is equal to the secret number we print 'Correct!'.
In this solution, instead of write a big block of code we write distinct functions that perform the tasks that we want to make the program more comprehesible.
The code in the function only run when the function is called, so first in the main block we generate the secret number using randint from random library.
Then we call the validation function to check and validate
Then we check if the guess is lower, higher or correct.
Then we print the message.
The last three processes would keep running until the user guess the correct number
'''

#Imports
import random #Python has built in library that we can use. In these libraries python has built in functions. In this case we use the 'random' library

#Functions   
def get_and_validate_input() -> int:
    """
    This function get input from user and validate that this input is an integer.
    This function is a void function that doesn't require arguments. It will keep asking for input until get a valid one
        @para: None
        @return: input_number
            This number is the guess of the user
    """
    while True: #An infinite loop that would run forever until the the conditions are met and the program break out of it
        input_integer = input("Please enter an integer: ")
        try: #Try and except is a method to validate the input. The block of code in 'try' will run until the 'except' catch an error and ignored the rest.
            input_integer = int(input_integer) #Convert the input to an integer because input from user is a string
            if input_integer > 100 or input_integer < 1:
                print("The number lies in the (1,100) range both included.")
                continue
            else: 
                break
        except ValueError: #A type of error that will be raised if you try to convert the wrong value. Example: int('6.5')
            print("The provided input is not valid!")
            continue #This syntax forces the while to start again
    return input_integer

def check_the_guess(guess_number: int, secret_number: int) -> str:
    '''
    This function check the guess and return either 0, 1, 2
        @para: 
            guess_number: the number that the user guess
            secret_number: a random integer that is generated at the beginning of the game
        @return: status_check
            An interger  that will decide the message to be printed out to the user
    '''
    if guess_number < secret_number: 
        status_check = 1
        return status_check
    elif guess_number > secret_number:
        status_check = 2
        return status_check
    elif guess_number == secret_number:
        status_check = 0
        return status_check


#Main
if __name__ == '__main__': #This part only runs when this file run directly. if __name__ == '__main__' is a special syntax
    secret_number = random.randint(1,100) #randint(x,y) will return an integer between x and y (both ends included)
    while True: 
        guess_number = get_and_validate_input()
        status_check = check_the_guess(guess_number, secret_number)
        if status_check == 0:
            print("Correct!") 
            break
        elif status_check == 1:
            print('higher')
        elif status_check == 2:
            print('lower')
        

