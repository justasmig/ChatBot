from tkinter import *
import os
import hashlib
from inference import *

def LoggedIn_Sucessfully():
    GUI_Screen_03 = Toplevel(Interface)
    GUI_Screen_03.title("You are in!")
    GUI_Screen_03.geometry("570x470")
    Label(GUI_Screen_03, text="Hey, you have logged In", font=("calibri", 15)).pack()
    Label(GUI_Screen_03, text="\n").pack()
    Label(GUI_Screen_03, text="\n").pack()
    Button(GUI_Screen_03, text="Chat To Bot", width=20, height=3, command=chat, font=("calibri", 15)).pack()
    Label(GUI_Screen_03, text="\n").pack()
    Label(GUI_Screen_03, text="\n").pack()
    Button(GUI_Screen_03, text="Play a Game", width=20, height=3, command=guessing_game, font=("calibri", 15)).pack()
    Label(GUI_Screen_03, text="\n").pack()
    Label(GUI_Screen_03, text="\n").pack()
    Button(GUI_Screen_03, text="Logout", command=GUI_Screen_03.destroy).pack()

def chat():
    # GUI_Screen_03 = Toplevel(Interface)
    # GUI_Screen_03.geometry("720x520")
    # Label(GUI_Screen_03, text="Chat with our Bot", font=("calibri", 15)).pack()
    chatBotInference()


def guessing_game():
    global words
    global guessing_word
    global write_word
    global GUI_Screen_03
    guessing_word = ["Hey"]
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

def validate_chatbot():
    if write_word in guessing_word:
        Label(GUI_Screen_03, text="WellDone You guessed it", fg="blue", font=("calibri", 11)).pack()
    elif write_word != guessing_word:
        Label(GUI_Screen_03, text="failed", fg="red", font=("calibri", 11)).pack()
    else:
        pass

def not_registered():
    GUI_Screen_05 = Toplevel(Interface)
    GUI_Screen_05.title("You are in!")
    GUI_Screen_05.geometry("220x140")
    Label(GUI_Screen_05, text="There's no user with that username registered!").pack()

def sucessfully_registered():

    print("It Works!")

    store_username = users_username.get()
    store_password = users_password.get()

    file = open(store_username, "w")
    file.write(store_username + "\n")
    file.write(store_password + "\n")
    file.close()

    users_username_register.delete(0, END)
    users_password_register.delete(0, END)

    Label(GUI_Screen_01, text="You have Successfully Logged In!", fg="blue", font=("calibri", 11)).pack()

def validating_login():
    validate_username = username_verify.get()
    validate_password = password_verify.get()
    users_username_login.delete(0, END)
    users_password_login.delete(0, END)

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


def new_user_registration():

    global GUI_Screen_01
    GUI_Screen_01 = Toplevel(Interface)
    GUI_Screen_01.title("New Registrations")
    GUI_Screen_01.geometry("350x305")
    global users_username
    global users_password
    global users_username_register
    global users_password_register
    users_username = StringVar()
    users_password = StringVar()

    Label(GUI_Screen_01, text="Enter the Following details Below to Register!").pack()
    Label(GUI_Screen_01, text="").pack()
    Label(GUI_Screen_01, text="Username :").pack()
    users_username_register = Entry(GUI_Screen_01, textvariable=users_username)
    users_username_register.pack()
    Label(GUI_Screen_01, text="").pack()
    Label(GUI_Screen_01, text="Password : ").pack()
    users_password_register = Entry(GUI_Screen_01, show="*", textvariable=users_password)
    users_password_register.pack()
    Label(GUI_Screen_01, text="").pack()
    Button(GUI_Screen_01, text="Register", width=10, height=1, command=sucessfully_registered).pack()
    Button(GUI_Screen_01, text="Log Hash", command=hashlog, height=2, width=25, ).pack()
    # Button(GUI_Screen_01, text="Generate Hash", command=passwordHash, height=2, width=25, ).pack()
def hashlog():
    global md5pw
    hash_obj1 = hashlib.md5()
    md5pw = StringVar()
    pwmd5 = users_password_register.get().encode('utf-8')
    hash_obj1.update(pwmd5)
    md5pw.set(hash_obj1.hexdigest())
    loghash = md5pw.get()

    if os.path.isfile('password_hash_log.txt'):
        obj1 = open('password_hash_log.txt', 'a')
        obj1.write(loghash)
        obj1.write("\n")
        obj1.close()
    else:
        obj2 = open('password_hash_log.txt', 'w')
        obj2.write(loghash)
        obj2.write("\n")
        obj2.close()



def existing_user_login():
    global GUI_Screen_02
    GUI_Screen_02 = Toplevel(Interface)
    GUI_Screen_02.title("Login")
    GUI_Screen_02.geometry("350x305")
    Label(GUI_Screen_02, text="Registered? You can Login in!").pack()
    Label(GUI_Screen_02, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global users_username_login
    global users_password_login
    Label(GUI_Screen_02, text="Username : ").pack()
    users_username_login = Entry(GUI_Screen_02, textvariable=username_verify)
    users_username_login.pack()
    Label(GUI_Screen_02, text="").pack()
    Label(GUI_Screen_02, text="Password : ").pack()
    users_password_login = Entry(GUI_Screen_02, show="*", textvariable=password_verify)
    users_password_login.pack()
    Label(GUI_Screen_02, text="").pack()
    Button(GUI_Screen_02, text="Login Now!", width=10, height=1, command=validating_login).pack()

def about_chatbot():
    GUI_Screen_02 = Toplevel(Interface)
    GUI_Screen_02.title("About ChatBot")
    GUI_Screen_02.geometry("350x305")
    Label(GUI_Screen_02, text="Here's what you need to know :").pack()
    Label(GUI_Screen_02, text="\n").pack()
    Label(GUI_Screen_02, text="This ChatBot is similar to Google Home or Siri to help people \n communicate whenever they feel lonely or Depressed. ").pack()
    Label(GUI_Screen_02, text="\n").pack()
    Label(GUI_Screen_02, text="|| Fetures || \n  World weather Forecast \n Display Date and Time \n General Facts \n Jokes \n Rooling 6 sided Dice \n Fliping Coin \n Setting Reminders \n Guessing word Game ").pack()

def main_screen():
    global Interface
    Interface = Tk()
    Interface.geometry("300x250")
    Interface.title("ChatBot")
    Label(text="Welcome Humans", bg="skyblue", width="300", height="1", font=("Hasty", 20)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="32", command=existing_user_login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="32", command=new_user_registration).pack()
    Label(text="").pack()
    Button(text="About", height="1", width="15", command=about_chatbot).pack()
    Interface.mainloop()
main_screen()
