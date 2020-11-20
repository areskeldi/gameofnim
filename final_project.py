######################################################################
# Author: Yryskeldi Emilbek uulu
# Username: emilbekuuluy
#
# P01 - Final Project
#
# Purpose: To reimplement the Game of Nim assignment in an object oriented style with several modifications
# including the visualization of the balls
#
#######################################################################
# Acknowledgements:
# Original code taken from the CSC 226 class taught by Dr. Brian Schack and Dr. Scott Heggen
# I used tkinter library tutorial on
# https://www.tutorialspoint.com/python3/python_gui_programming.htm
# Mahmoud Amer , a CS TA, was an instrumental help in this project.
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import random
import turtle
from turtle import *
import tkinter as tk
from tkinter import *


class Nim:
    def __init__(self):
        """
        Initializes the Nim class: opens a new GUI window
        """
        self.window = tk.Tk()                   # creates a window object
        self.window.geometry('1200x900')        # creates window coordinates
        self.bgimage = PhotoImage(file=r"background.gif")       # stores an image in the variable
        Label(self.window, image=self.bgimage).place(relwidth=1,relheight=1)        # places the image on the screen
        self.title = Label(self.window, text="Game of Nim", bd=8, width=50, relief=RAISED, padx=50, pady=30, font="Revamped 30")
        self.title.grid(row=0, column=0)        # initializes the row, grid system
        self.var=IntVar()                       # stores values for radiobuttons

        # Starting
        self.firstquestion = Label(self.window, text="How many balls do you want to start with? (min 16)", font=("Helvetica 35", 16))
        self.firstquestion.grid(row=1, column=0)

        self.firstinputbox = tk.Entry()     # creates an input box
        self.firstinputbox.grid(row=2, column=0)

        self.check_button = tk.Button(self.window, text="Set", command=self.check_total_balls)  # creates a button to set the total number of balls
        self.check_button.grid(column=0, row=3)
        self.window.mainloop()
        self.tess = turtle.Turtle


    def check_total_balls(self):
        """
        Checks whether user inputted a correct number of balls
        :return: None
        """
        if int(self.firstinputbox.get()) > 15:
            self.right_warning_statement = Label(self.window, text="You're good to go! Press 'Start'", font=("Helvetica 35", 16))
            self.right_warning_statement.grid(row=4, column=0)
            self.total_balls = int(self.firstinputbox.get())
            self.game_button = tk.Button(self.window, text="Start", command=lambda: [self.user_turn(),
                                                                                     self.firstinputbox.destroy(), self.firstquestion.destroy(),
                                                                                     self.check_button.destroy(),
                                                                                     self.right_warning_statement.destroy(), self.wrong_warning_statement.destroy(),
                                                                                     self.open_turtle_window()])
            self.game_button.grid(row=5, column=0)
        else:
            self.wrong_warning_statement = Label(self.window, text="Enter a number (!) higher than 15!", font=("Helvetica 35", 16))
            self.wrong_warning_statement.grid(row=4, column=0)

    def open_turtle_window(self):
        """
        Opens a window where the user can see how many balls are on the table at each moment of the game
        :return: None
        """
        self.total_balls_statement = turtle.Turtle()        # creates a turtle that displays a text
        self.total_balls_statement.penup()
        self.total_balls_statement.goto(-190, 150)
        self.total_balls_statement.pendown()
        self.total_balls_statement.color('black')
        self.total_balls_statement.write("There's " + str(self.total_balls) + " ball/-s on the table, \n as of now.", font=("Courier", 14))
        self.total_balls_statement.hideturtle()
        self.tess = turtle.Screen()
        self.tess.setup(430, 400, startx=35, starty=150)
        self.ball = turtle.Turtle()                         # creates a turtle that represents each ball on the table
        self.ball.fillcolor("black")
        self.ball.speed(-1)
        self.ball.hideturtle()
        self.ball.penup()
        y = 100
        self.ball.setpos(-130,y)
        for i in range(self.total_balls):                   # iterates through self.total_balls
            self.ball.pendown()
            self.ball.begin_fill()
            self.ball.circle(10)
            self.ball.end_fill()
            self.ball.penup()
            self.ball.forward(30)
            if i%10==0 and i!=0:
                y -= 30
                self.ball.setpos(-150, y)
                self.ball.pendown()
                self.ball.begin_fill()
                self.ball.circle(10)
                self.ball.end_fill()
                self.ball.penup()
                self.ball.forward(30)


    def user_turn(self):
        """
        Creates radiobuttons to enable user to take 1 to 4 balls from the pile.
        :return: None
        """
        self.userturn_statement = Label(self.window, text="It's your turn! How many balls do you want to take?", font=("Helvetica 35", 16))
        self.userturn_statement.grid(row=4, column=0)
        self.var = StringVar()  # stores the value of Radio button
        self.var.set("")
        self.r = Radiobutton(self.window, text="1 ball", value="1 ball", variable=self.var, font="Lucida 24", bg="white", fg="orange", command=self.user_select,
                        indicatoron=0)          # creates a radiobutton
        self.r.grid(row=5, column=0)
        self.r1 = Radiobutton(self.window, text="2 balls", value="2 balls", variable=self.var, font="Lucida 24", bg="white", fg="orange",
                         command=self.user_select, indicatoron=0)
        self.r1.grid(row=6, column=0)
        self.r2 = Radiobutton(self.window, text="3 balls", value="3 balls", variable=self.var, font="Lucida 24", bg="white", fg="orange",
                         command=self.user_select, indicatoron=0)
        self.r2.grid(row=7, column=0)
        self.r3 = Radiobutton(self.window, text="4 balls", value="4 balls", variable=self.var, font="Lucida 24", bg="white", fg="orange",
                         command=self.user_select, indicatoron=0)
        self.r3.grid(row=8, column=0)

    def user_select(self):
        """
        Creates a command for when user clicked on a radiobutton, it gives a user a second chance to confirm their choice.
        :return: None
        """
        selection = "Do you want to take " + str(self.var.get()) + "?"
        self.select_confirmation = Label(self.window, text=selection,
                           font=("Helvetica 35", 16))       # creates a message to ask the user whether they want to take x number of balls
        self.select_confirmation.grid(row=9, column=0)
        self.confirm = StringVar()
        self.confirm.set("")
        self.confirm_button = Radiobutton(self.window, text="Confirm", value="confirm", variable=self.confirm, font="Lucida 24", bg="white", fg="orange", command=self.user_confirm,
                        indicatoron=0)
        self.confirm_button.grid(row=10, column=0)

    def user_confirm(self):
        """
        Creates a command for when the user confirms number of balls they want to take.
        :return: None
        """
        if self.var.get() == "1 ball":
            self.total_balls -= 1               # updates the value of self.total_balls to keep the score
        elif self.var.get() == "2 balls":
            self.total_balls -= 2
        elif self.var.get() == "3 balls":
            self.total_balls -= 3
        elif self.var.get() == "4 balls":
            self.total_balls -= 4
        elif self.var.get() == "confirm":
            self.total_balls -= 5
        self.tess.clear()               # clears the turtle window containing info on current total number of balls
        self.open_turtle_window()       # reopens the turtle window with new values of self.total_balls
        # sequence of statements to completely clear unnecessary statements during computer's turn on tkinter window:
        self.userturn_statement.destroy()
        self.r.destroy()
        self.r1.destroy()
        self.r2.destroy()
        self.r3.destroy()
        self.select_confirmation.destroy()
        self.confirm_button.destroy()
        self.game_button.destroy()
        self.computer_wait()

    def computer_wait(self):
        """
        Creates an illusion of computer waiting to take a turn
        :return: None
        """
        self.computer_waiting = Label(self.window, text="Computer is thinking...",
                                      font=("Helvetica 35", 16))
        self.computer_waiting.grid(row=4, column=0)
        self.window.after(6000, self.computer_turn)         # this method waits for 6000 ms and then performs the computer_turn method

    def computer_turn(self):
        """
        Either takes a random (1 to 4) number of balls from the pile, or the total balls modulus five.
        :return: None
        """
        self.computer_take = self.total_balls % 5           # this helps maximize computer wins
        if self.computer_take % 5 == 0:
            self.computer_take = random.randint(1,4)
        self.computerturn_statement = Label(self.window, text="Computer takes " + str(self.computer_take) + " ball/-s.",
                                                font=("Helvetica 35", 16))
        self.computerturn_statement.grid(row=4, column=0)
        self.total_balls -= self.computer_take              # updates the value of total balls
        self.tess.clear()
        self.open_turtle_window()
        self.computerturn_statement.destroy()
        self.user_turn()
        if self.total_balls == 0:                           # sets a sequence of operations if computer wins
                self.userturn_statement.destroy()
                self.r.destroy()
                self.r1.destroy()
                self.r2.destroy()
                self.r3.destroy()
                self.select_confirmation.destroy()
                self.confirm_button.destroy()
                self.game_button.destroy()
                self.bgimage = PhotoImage(file=r"lose.gif")
                Label(self.window, image=self.bgimage).place(relwidth=1, relheight=1)
                self.tess.clear()
                self.total_balls_statement.write("Computer won!", font=("Courier", 14))
        if self.total_balls < 0:                            # sets sequence of operations if user wins
                self.computerturn_statement.destroy()
                self.userturn_statement.destroy()
                self.r.destroy()
                self.r1.destroy()
                self.r2.destroy()
                self.r3.destroy()
                self.select_confirmation.destroy()
                self.confirm_button.destroy()
                self.game_button.destroy()
                self.tess.clear()
                self.bgimage = PhotoImage(file=r"win.gif")
                Label(self.window, image=self.bgimage).place(relwidth=1, relheight=1)
                self.tess.clear()
                self.total_balls_statement.write("You won!", font=("Courier", 14))


# Start button
if __name__ == "__main__":
    game = Nim()                                                # this is where magic happens!