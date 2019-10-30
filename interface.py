from tkinter import *
from tkinter import scrolledtext
from random import choice

# I called this interface frame
frame = Tk()
user = StringVar()

ask=["hi","How are you?","Hello"]
ans=["Fine","I am ok, how are you?"]
error=["I didn't have that answer in my database!"]

def chatbotinter():

#this is the title of the frame
frame.title("Our chatbot")

#this is the size of frame
frame.geometry('400x550')

#this is label set
label1=Label(frame, text="user")
label1.grid(row=1,column=0)

user_text=StringVar()
text=Entry(frame,textvariable=user_text)
text.grid(row=1,column=2)

txt = scrolledtext.ScrolledText(frame)
massages = Listbox(frame,width=40,height=20)

txt.grid(row=0,column=2)
chatbotinter()

# def clicked():
#     question=user_text.get()
#     if question in ask:
#         massages.insert(END,"you : " + choice(ans))
#     #else:



button1=Button(frame, text="send",command=clicked, bg="blue", fg="white")
button1.grid(row=1,column=3)

frame.mainloop()