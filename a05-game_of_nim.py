######################################################################
# Author: Lydia Bodine, Yryskeldi Emilbek uulu
# Username: bodinel, emilbekuuluy
#
# Assignment: A05: The Game of Nim
#
# Purpose: To create the game of Nim
#
######################################################################
# Acknowledgements:
#
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import random


def ask_the_number_of_balls():
    """
   Asks how many balls the user wants to take.
   :return:
   """
    number_of_balls = int(input("How many balls do you want to start off with (Minimum 15)? "))
    while number_of_balls < 15:
        number_of_balls = input("Sorry, you entered a number less than 15. Please, enter the number higher than 15: ")
    return number_of_balls


def play_the_game(number_of_balls):
    while int(number_of_balls) >= 1:
        user_take = int(input("How many balls would you like to take? (between 1 and 4) "))
        while user_take > 4 or user_take < 1:
            user_take = int(input("Sorry! You entered too high or too low of a number. Please enter a number between 1 and 4: "))
        number_of_balls -= user_take
        computer_take = number_of_balls % 5
        if computer_take % 5 == 0:
            computer_take = random.randint(1, 4)
        print("The computer takes " + str(computer_take) + " balls")
        number_of_balls -= computer_take
        print("You have " + str(number_of_balls) + " balls left")
        if number_of_balls == 0:
            print("Computer won!")
        if number_of_balls < 0:
            print("Oh, your neighbor stole " + str(computer_take) + " nonexistent balls from you, so now you have a negative number of balls (XD)")
            print("You won!")



def main():
    number_of_balls = ask_the_number_of_balls()
    play_the_game(number_of_balls)

main()
