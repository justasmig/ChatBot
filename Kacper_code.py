from random import choice
from random import randint
from time import sleep
import datetime


Greeting = [ "Welcome", "What's up", "Hello", "Nice to meet you.", "Well hello!",  ]
optionsOfChatB = ("1) Ask a question" ,  '2) Get the information about current time and date', '3) Get a joke or a fact ', '4) Run the calculator',
                  '5) Make a simulation of flipping a coin or rolling six sided dice', "6) Sort a list of number", "Finish the conversation")
invitationToAsk = [ "Give me a hard query, please", "Do you want to know the answer for any question?, ask me", "What question do you want to know answer for?" ]
i=1
def queries():
    user =input("Robot says: " +  choice(invitationToAsk) + "\n ")

    if user == "what is temperature of the sun?":
        answers = [ "temperature of the sun is 5 778 K ", "Let's google it", "Unfortunately, the temperature is too high for living there "]
        return (choice(answers) )
    elif user =="what is the homework in mathematics?":
        answers = [ "Exercises 1-10 from 95-99 pages", "why don't you ask someone else", "Oh no, I have written it down"]
        return (choice(answers))
    elif user == "when the beatles band was founded?":
        answers = [ "The Beatles was formed in 1960", " Wow, I'm not interested in such old bands", "Sorry, but I do not know the band"]
        return (choice(answers))
    elif user == "what is the best social media?":
        answers = [ "YouTube", "Aaaa, the selection is too big to choose the best one", "I am so poor I cannot afford smartphone, so I do not use any"]
        return (choice(answers))
    elif user == "are you a robot?":
        answers = [ "yeah, but despite that you can talk with me", " It does not matter. I' m the smartest here", "unfortunately, I am only your computer program"]
        return (choice(answers))
    elif user == "why are you still typing to me? ":
        answers = [ "Because, I like you", "That is just how I am programmed", "I am depressed"]
        return (choice(answers))
def timeDate():
    user = input("What would you like to know time, date or both?: ")
    if user == "time":
        return (datetime.time())
    elif user =="date":
        return  (datetime.date(2019))
    else:
        return (str(datetime.time()) + "  " + str(datetime.date(2019)))
def jokesAndFacts():
    user = input("What would you like to get a joke or a fact?: ")

    if user =="fact":
        f = open("facts.txt", "r")
        numRand = randint(0, 9)
        for num_line, line in enumerate(f.readlines()):
            if num_line == numRand:
                lineRand = line
        f.close()
        return lineRand
    else:
        j = open("jokes.txt", "r")
        numRand = randint(0, 9)
        for num_line, line in enumerate(j.readlines()):
            if num_line == numRand:
                lineRand = line
        j.close()
        return lineRand
    
#modified functions by Justas
def jokesChatbot():
    f = open("facts-Kacper.txt", "r")
    numRand = randint(0, 9)
    for num_line, line in enumerate(f.readlines()):
        if num_line == numRand:
            lineRand = line
    f.close()
    return lineRand
def factsChatbot():
    j = open("jokes-Kacper.txt", "r")
    numRand = randint(0, 9)
    for num_line, line in enumerate(j.readlines()):
        if num_line == numRand:
            lineRand = line
    j.close()
    return lineRand
def coinChatbot():
    result = randint(0, 1)
    sleep(2.5)
    if result == 1:
        return ("Your flip is head")
    else:
        return ("Your flip is tail")
def diceChatbot():
    result = randint(1, 6)
    sleep(2.5)
    return("You rolled a", result)

#end of Justas modifications


def calculator():
    num1 = float (input("Enter  first number: "))
    op = input("Enter the operator: ")
    num2 = float (input("Enter  second number: "))

    if op == "+":
        return num1+num2
    elif op =="-":
        return  num1-num2
    elif op =="*":
        return  num1*num2
    elif op =="/":
        return  num1/num2
    elif op =="%":
        return  num1%num2
    elif op =="**":
        return  num1**num2
    else:
        return "The given operator was not recognized"
def coin():
    flip=True
    while flip:
        toFlip=input("Press Enter to flip or press q to Quit ")
        if toFlip =="q":
            flip=False
        else:
            result = randint(0, 1)
            print("Coin is fliping...")
            sleep(2.5)
            if result == 1:
                print ("Your flip is head")
            else:
                print ("Your flip is tail")
    print("Thanks for the game")
def dice():
    roll=True
    while roll:
        toRoll=input("Press Enter to roll or press q to Quit ")
        if toRoll =="q":
            roll=False
        else:
            result = randint(1, 6)
            print("Dice is rolling...")
            sleep(2.5)
            print("You rolled a", result)
    print("Thanks for the game")
def quickSort(listN):
    smaller = []
    larger = []
    equal = []
    if len(listN) > 1:
        pivot = listN[0]
        for x in listN:
            if x > pivot:
                larger.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                smaller.append(x)
        return quickSort(smaller)+ equal + quickSort(larger)
    else:
        return listN
'''
while i>0:
    print(choice(Greeting) )
    for option in range (len(optionsOfChatB)):
        print (optionsOfChatB[option])
    userChoice=  input("Which of the above options would you like to choose?: ")

    if   userChoice=="1":
        print(queries())
    elif userChoice=="2":
        now = datetime.datetime.now()
        time = now.strftime("%H:%M")
        date = now.strftime("%d.%m.%Y")
        print( timeDate() )
    elif userChoice=="3":
        print( jokesAndFacts() )
    elif userChoice=="4":
        print( calculator() )
    elif userChoice=="5":
        user = input("Would you like to flip a coin or roll the dice?: ")
        if user == "flip a coin":
            coin()
        else:
            dice()
    elif userChoice=="6":
        print("How many numbers to sort?: ")
        num=int (input())
        listOfNumbers = []
        for x in range (num):
            print("Give me the " + str(x+1) + ". number")
            listOfNumbers.append(int(input()))
        print(listOfNumbers)
        print (quickSort(listOfNumbers))
    elif userChoice.lower()=="finish" or  userChoice.lower()=="finish the conversation" :
        break
    else:
        print("I don't understand, could you repeat?")
'''