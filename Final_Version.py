from tkinter import *
import hashlib
import os
from inference import * #importing Justas' ML chatbot inference.


# The idea of how to make the interface throughout this project was taken from - https://www.youtube.com/watch?v=Xt6SqWuMSA8&t=7s
#This section of the code is used for the popup window after the user has sucessfully logged in
#I have created my own variables that is different from the source code; i have also added extra buttons to play games and to
#chat to the bot
def LoggedIn_Sucessfully():
    GUI_Screen_03 = Toplevel(Interface)
    GUI_Screen_03.title("You are in!")
    GUI_Screen_03.geometry("570x470")
    Label(GUI_Screen_03, text="Hey, you have logged In", font=("calibri", 15)).pack()
    Label(GUI_Screen_03, text="\n").pack()
    Label(GUI_Screen_03, text="\n").pack()
    #When this button is clicked it will pop up with the chatbot interface, where the users are able to chat
    #to the bot.
    Button(GUI_Screen_03, text="Chat To Bot", width=20, height=3, command=chat, font=("calibri", 15)).pack()
    Label(GUI_Screen_03, text="\n").pack()
    Label(GUI_Screen_03, text="\n").pack()
    #When clicked the Play a Game button it will take the user to a guessing game screen.
    Button(GUI_Screen_03, text="Play a Game", width=20, height=3, command=guessing_game, font=("calibri", 15)).pack()
    Label(GUI_Screen_03, text="\n").pack()
    Label(GUI_Screen_03, text="\n").pack()
    # I have programmed a logout button that will allow the user to close the window they are on.
    Button(GUI_Screen_03, text="Logout", command=GUI_Screen_03.destroy).pack()

#This section of the code is where the chatbot interface is; it allows you to type inputs and depending on those inputs it will display
#it will display a suitable output.
def chat():
    chatBotInference(Interface) #Justas' ML chatbot inference combined with other's
'''    
    GUI_Screen_03 = Toplevel(Interface)
    GUI_Screen_03.geometry("720x520")
    Label(GUI_Screen_03, text="Chat with our Bot", font=("calibri", 15)).pack()
'''

#This is a guessing game that i build myself using my own knowledge of python, I have set a guessing word to "Hey"
#This code displays a title guess, an input for the user to guess the word and a button that validates wheather if its
#the right word.
def guessing_game():
    global words
    global guessing_word
    global write_word
    global GUI_Screen_03
    guessing_word = ["Hey", "hey"]
    words = StringVar()
    GUI_Screen_03 = Toplevel(Interface)
    GUI_Screen_03.title("Guessing Game")
    GUI_Screen_03.geometry("720x520")
    Label(GUI_Screen_03, text="||Guess the word!||", font=("calibri", 15)).pack()
    Label(GUI_Screen_03, text="\n").pack()
    write_word = Entry(GUI_Screen_03, textvariable=words)
    write_word.pack()
    Label(GUI_Screen_03, text="").pack()
    Button(GUI_Screen_03, text="Enter", width=10, height=1, command=validate_chatbot).pack()

# Here is a code that i wrote taht will validate whether its the correct word, if it is then it will output a possitive message
# if the input isnt corrent then it will output a negative message with a red colour font.
def validate_chatbot():
    word = write_word.get()
    if word in guessing_word:
        Label(GUI_Screen_03, text="Well done you could have guessed from : ", fg="blue", font=("calibri", 11)).pack()
        # this for loop that i created will display all of the possible words user could have guessed from the list guessing_word.
        # for loop will only activate once the answer is correct as it is under the if statement
        for different_words in guessing_word:
            Label(GUI_Screen_03, text=different_words, fg="red", font=("calibri", 11)).pack()
        # After the user guesses the word they can wish to close the screen by clicking the end button.
        # This button will only appear when the user has guessed the correct word.
        Button(GUI_Screen_03, text="End", command=GUI_Screen_03.destroy).pack()
    elif write_word != guessing_word:
        Label(GUI_Screen_03, text="failed", fg="red", font=("calibri", 11)).pack()
    else:
        pass




#This section of the code will display a message saying that the user hasn't been registered.
#This may be due to inputting inncorrect username or someone trying to input a username thats not
#in the text file.
#These 2 section not_registered & failed_pass of the code were from the youtube video however i have made a slight change on the
#messagees that they will output.
def not_registered():
    GUI_Screen_05 = Toplevel(Interface)
    GUI_Screen_05.title("Failed")
    GUI_Screen_05.geometry("220x140")
    Label(GUI_Screen_05, text="There's no user with that username registered!").pack()

#Just like the validation check for the username this section checks for the password, if the user has inputted the
#correct username however not the correct password then the program will call out this function.
def failed_pass():
    GUI_Screen_05 = Toplevel(Interface)
    GUI_Screen_05.title("Failed")
    GUI_Screen_05.geometry("220x140")
    Label(GUI_Screen_05, text="Password is incorrect").pack()


# This function is called out whenever the register button is pressed, validating whether the username and password
# is in the file was used from --  https://www.youtube.com/watch?v=Xt6SqWuMSA8&t=7s
#Other validatations such as ammount of characters needed in the password and checking if the input sections are empty were
#coded by me.
#Here I have also used hashing to hash the password when users register, parts of hashing algorithm were used from --
# https://stackoverflow.com/questions/38667724/python-tkinter-password-checker-gui-hashing-issue
def sucessfully_registered():
    global md5pw
    hash_obj1 = hashlib.md5()
    md5pw = StringVar()
    pwmd5 = users_password_register.get().encode('utf-8')
    hash_obj1.update(pwmd5)
    md5pw.set(hash_obj1.hexdigest())
    loghash = md5pw.get()
    store_username = users_username.get()
    store_password = users_password.get()
    #I coded these nested if statements so it checks for the length of the password, it checks whether the password and the
    #username fields have been inputted.
    if len(store_password) >= 8:
        if not store_username:
            Label(GUI_Screen_01, text="Please Enter a UserName", fg="red", font=("calibri", 11)).pack()
        elif not store_password:
            Label(GUI_Screen_01, text="Please Enter a Password", fg="red", font=("calibri", 11)).pack()
            #These first few lines were used from -- https://www.youtube.com/watch?v=Xt6SqWuMSA8&t=7s to store the password
            #sucessfully into a text file after it has passed all of the validations, however i have used my own variable name
            #to carry out the operation.
        else:
            file = open(store_username, "w")
            file.write(store_username + "\n")
            file.write(store_password + "\n")
            file.close()
            users_username_register.delete(0, END)
            users_password_register.delete(0, END)
            Label(GUI_Screen_01, text="You have Successfully Logged In!", fg="blue", font=("calibri", 11)).pack()

            # This section of the code is used from -- https://stackoverflow.com/questions/38667724/python-tkinter-password-checker-gui-hashing-issue
            # it basically creates a new file called hashed password if there isn't already one
            #and stores the passwords in here. from the original code i have made a few changes by using my own variable name and adding
            #extra texts in order to make it look more neat.
        if os.path.isfile('Hashed_Passwords.txt'):
            hashing_file = open('Hashed_Passwords.txt', 'a')
            hashing_file.write("=========================" + "\n")
            hashing_file.write("Username = " + store_username + "\n")
            hashing_file.write("Password = " + loghash)
            hashing_file.write("\n")
            hashing_file.write("=========================" + "\n")

            # This section of the code is the sameone as at the top but this one is executed if there is already a file
            #called Hashed_password.txt to store username and hashed passwords.
        else:
            hashing_file = open('Hashed_passwords.txt', 'w')
            hashing_file.write("=========================" + "\n")
            hashing_file.write("Username = " + store_username + "\n")
            hashing_file.write("Password = " + loghash)
            hashing_file.write("\n")
            hashing_file.write("=========================" + "\n")
            #The bottom elif and else statements are just validation checks to see if there is data in the input field passwords,
            #and the else statement is to see if the password user inputted is over 8 characters long.
    elif not store_password:
        Label(GUI_Screen_01, text="Please Enter a Password", fg="red", font=("calibri", 11)).pack()
    else:
        Label(GUI_Screen_01, text="Password Must be over 8 Characters", fg="red", font=("calibri", 11)).pack()


#Most of this section of the code was used from - https://www.youtube.com/watch?v=Xt6SqWuMSA8&t=7s, but i have changed variable names
#that make more sense when reading, this program here is only executed when the user clicks the login button after inpuuting data.
def validating_login():
    validate_username = username_verify.get()
    validate_password = password_verify.get()
    users_username_login.delete(0, END)
    users_password_login.delete(0, END)
    #it will read the username and password that the user inputted in the username and password field and will then compare it to the one
    #in the text file, if the inputs match then it will run the LoggedIn_Sucessfully function. otherwise it will run the not_regisered function.
    User_Details_files = os.listdir()
    if validate_username in User_Details_files:
        file1 = open(validate_username, "r")
        validate = file1.read().splitlines()
        if validate_password in validate:
            LoggedIn_Sucessfully()
        else:
            failed_pass()
    else:
        not_registered()

#Most of this code is used from -- https://www.youtube.com/watch?v=Xt6SqWuMSA8&t=7s, variable names and text are moslty the
#only thing that i have changed throughout this section.
def new_user_registration():
    global GUI_Screen_01
    GUI_Screen_01 = Toplevel(Interface)
    GUI_Screen_01.title("New Registrations")
    GUI_Screen_01.geometry("350x305")
    #I have used multiple global variables as they are all used in different function throughout the program
    #most of them are used to validate the username/password, they are also used to store username/password and are used to take inputs from the user.
    global users_username
    global users_password
    global users_username_register
    global users_password_register
    users_username = StringVar()
    users_password = StringVar()
    Label(GUI_Screen_01, text="Enter the Following details Below to Register!").pack()
    Label(GUI_Screen_01, text="").pack()
    #The code below are inputs that the user needs to give so they need to input a username and a password.
    Label(GUI_Screen_01, text="Username :").pack()
    users_username_register = Entry(GUI_Screen_01, textvariable=users_username)
    users_username_register.pack()
    Label(GUI_Screen_01, text="").pack()
    Label(GUI_Screen_01, text="Password : ").pack()
    #The line below is what i wrote down inorder for the password input to not be vissiable when typing, it will now
    #display a star when user types something in the password input.
    users_password_register = Entry(GUI_Screen_01, show="*", textvariable=users_password)
    users_password_register.pack()
    Label(GUI_Screen_01, text="").pack()
    #The button here will start execute the function sucessfully_registered; where it will validate the user inputs.
    Button(GUI_Screen_01, text="Register", width=10, height=1, command=sucessfully_registered).pack()

#Just like the new_user_registration function at the top sectionMost of this code is used from
# -- https://www.youtube.com/watch?v=Xt6SqWuMSA8&t=7s, variable names and text are moslty the only thing that i have changed throughout this section.
def existing_user_login():
    global GUI_Screen_02
    GUI_Screen_02 = Toplevel(Interface)
    #The code below are the titles of the GUI screens.
    GUI_Screen_02.title("Login")
    GUI_Screen_02.geometry("350x305")
    Label(GUI_Screen_02, text="Registered? You can Login in!").pack()
    Label(GUI_Screen_02, text="").pack()
    # Gloable variable are used here because need to verify whether or not username and password that the user typed is in the
    #text file, the smae variable name will be used in the function in the top section of the program called validating_login.
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global users_username_login
    global users_password_login
    #Section below is where the user will input their username and password that they registered with at the start.
    Label(GUI_Screen_02, text="Username : ").pack()
    users_username_login = Entry(GUI_Screen_02, textvariable=username_verify)
    users_username_login.pack()
    Label(GUI_Screen_02, text="").pack()
    Label(GUI_Screen_02, text="Password : ").pack()
    #Just like line in register new user function i have used the same line here again to hide the users password when typing,
    #this provides security aboud them.
    users_password_login = Entry(GUI_Screen_02, show="*", textvariable=password_verify)
    users_password_login.pack()
    Label(GUI_Screen_02, text="").pack()
    #After all of the inputs are written by the user, they can then press the Login Now! button to run the validating_login function
    #inside that fuction it digs deeper to see if the username and password that they typed match the one on the textfile.
    Button(GUI_Screen_02, text="Login Now!", width=10, height=1, command=validating_login).pack()

#All the code in this about_chatbot fuction was coded by me and it displays the texts written below about what this chatbot contains.
def about_chatbot():
    GUI_Screen_02 = Toplevel(Interface)
    GUI_Screen_02.title("About ChatBot")
    GUI_Screen_02.geometry("350x305")
    Label(GUI_Screen_02, text="Here's what you need to know :").pack()
    Label(GUI_Screen_02, text="\n").pack()
    Label(GUI_Screen_02, text="This ChatBot is similar to Google Home or Siri to help people \n communicate whenever they feel lonely or Depressed. ").pack()
    Label(GUI_Screen_02, text="\n").pack()
    Label(GUI_Screen_02, text="|| Fetures || \n  World weather Forecast \n Display Date and Time \n General Facts \n Jokes \n Rooling 6 sided Dice \n Fliping Coin \n Setting Reminders \n Guessing word Game ").pack()

'''
Code from this part has been added by Justas
'''
def anime_screen():
    GUI_anime_screen = Toplevel(Interface)
    GUI_anime_screen.title("Anime")
    GUI_anime_screen.geometry("500x600")


'''
Code by Justas finished
'''

#This is the screen that first opens up when you run the program, this displays the login button, register button and about chatbot button.
#Each button is linked to one of the functions at the top as i hhave used the command function to direct it to the corret function.
#This section of the code contains the global variable Interface which is used in every function above to give output window when run.
def main_screen():
    global Interface
    Interface = Tk()
    Interface.geometry("300x250")
    Interface.title("ChatBot")
    Label(text="Welcome Humans", bg="skyblue", width="300", height="1", font=("Hasty", 20)).pack()
    Label(text="").pack()
    #All the code below are outputs 3 buttons that the user can press, they can choose if they want to login,
    #or if they want to register and theres even a button if they want to see about the chatbot, each button has
    #a different cammand link that runs cretian functions when pressed.
    Button(text="Login", height="2", width="32", command=existing_user_login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="32", command=new_user_registration).pack()
    Label(text="").pack()
    Button(text="About", height="1", width="15", command=about_chatbot).pack()
    #The 2 code below are important becasue they allow us to see the window pop up of Tkinter.
    Interface.mainloop()
main_screen()


#Refrences - https://stackoverflow.com/questions/38667724/python-tkinter-password-checker-gui-hashing-issue
#Refrenses - https://www.youtube.com/watch?v=Xt6SqWuMSA8&t=7s
