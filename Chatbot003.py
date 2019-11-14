# Module Imports
import random
import time
import tkinter
from Weatherapp import *
from alarmclock import *
from Kacper_code import *

# Declaring Variables
name = ""
greetings = ["Hello " + name + ". What can I do for you?", "What do you need?", "What now!"]
flag=True
command_list=["Alarm clock","Weather","Date and time","Ask a question" ,
              'Get a joke or a fact ',
              'Run the calculator','Make a simulation of flipping a coin or rolling six sided dice',
              "Sort a list of number", "Got to go" ]

#Function to be called by other code when required
def response(name):
    print(random.choice(greetings))
    flag=True
    #A while loop to keep the chat going until certain criteria are met.
    while flag==True:
        print("What can I do for you?")
        userInput = input().upper()
        #If statements to do the specific baked in function of the bot.

        if "DEPRESSED" in userInput:
            time.sleep(3)
            print(name + " I'm sorry to hear that. Find somebody to talk to it will help you feel better :) .")
        elif "COMPLIMENT ME" in userInput:
            time.sleep(1)
            print("You don't need to be complimented.")
        elif "RELAX" in userInput:
            time.sleep(1)
            print("Hey its not my fault, I was born this way.")
        elif "COMMAND LIST" in userInput:
            print("My current command list is:")
            print(command_list)
        elif "HELLO" in userInput or "HI" in userInput:
            time.sleep(2)
            print(random.choice(greetings))
        elif "I HAVE TO GO" in userInput:
            time.sleep(2)
            print("Goodbye, " + name + ". Have a good day.")
            flag=False

        elif "WEATHER" in userInput:
            country()
        elif "ALARM CLOCK" in userInput:
            runner()
        elif "QUESTION" in userInput:
            queries()
        elif "JOKE" in userInput or "FACTS" in userInput:
            jokesAndFacts()
        elif "CALCULATOR" in userInput:
            calculator()
        elif "COIN FLIP" in userInput:
            coin()
        elif "ROLL DICE" in userInput:
            dice()
        else:
            print("Sorry " + name + ", currently I don't know how to respond to that.")
response("Test")