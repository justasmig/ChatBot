from tkinter import *
import os
import PIL
from PIL import Image,ImageTk
import pytesseract
import cv2

width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

def LoggedIn_Sucessfully():
    global GUI_Screen_03
    GUI_Screen_03 = Toplevel(Interface)
    GUI_Screen_03.title("You are in!")
    GUI_Screen_03.geometry("720x520")
    Label(GUI_Screen_03, text="User Has Been Successfully Logged In!").pack()




def failed_pass():
    global GUI_Screen_04
    GUI_Screen_04 = Toplevel(Interface)
    GUI_Screen_04.title("You are in!")
    GUI_Screen_04.geometry("220x140")
    Label(GUI_Screen_04, text="There's Something wrong with your Password").pack()


def not_registered():
    global GUI_Screen_05
    GUI_Screen_05 = Toplevel(Interface)
    GUI_Screen_05.title("You are in!")
    GUI_Screen_05.geometry("220x140")
    Label(GUI_Screen_05, text="There's no user with that username registered!").pack()

Interface = Tk()
mainInt = Label(Interface)
mainInt.pack()

def launch_face():
    ret, frame = cap.read()
    rgbImg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(rgbImg)
    imgtk = ImageTk.PhotoImage(image=img)
    mainInt.imgtk = imgtk
    mainInt.configure(image=imgtk)
    mainInt.after(10, launch_face)


def sucessfully_registered():
    print("It Works!")

    store_username = users_username.get()
    store_password = users_password.get()

    file = open(store_username, "w")
    file.write(store_username + "\n")
    file.write(store_password)
    file.close()

    users_username_register.delete(0, END)
    users_password_register.delete(0, END)

    Label(GUI_Screen_01, text="You have Successfully Logged In!", fg="yellow", font=("calibri", 11)).pack()


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
    global name_entry
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
    users_password_register = Entry(GUI_Screen_01, textvariable=users_password)
    users_password_register.pack()
    Label(GUI_Screen_01, text="").pack()
    Button(GUI_Screen_01, text="Register", width=10, height=1, command=sucessfully_registered).pack()

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
    users_password_login = Entry(GUI_Screen_02, textvariable=password_verify)
    users_password_login.pack()
    Label(GUI_Screen_02, text="").pack()
    Button(GUI_Screen_02, text="Login Now!", width=10, height=1, command=validating_login).pack()

def about_chatbot():
    global GUI_Screen_02
    GUI_Screen_02 = Toplevel(Interface)
    GUI_Screen_02.title("About ChatBot")
    GUI_Screen_02.geometry("350x305")
    Label(GUI_Screen_02, text="Here's what you need to know").pack()

def main_screen():
    global Interface
    Interface = Tk()
    Interface.geometry("300x300")
    Interface.title("ChatBot")
    Label(text="Welcome Humans", bg="skyblue", width="300", height="1", font=("Hasty", 20)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="32", command=existing_user_login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="32", command=new_user_registration).pack()
    Label(text="").pack()
    Button(text="About", height="1", width="15", command=about_chatbot).pack()
    Label(text="").pack()
    Button(text="Login using face!", height="1", width="32", command=launch_face).pack()
    Interface.mainloop()
main_screen()
