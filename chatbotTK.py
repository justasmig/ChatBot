#from chatterbot import ChatBot
from tkinter import *
#bot = ChatBot("Riven")
from setup.settings import hparams, out_dir, preprocessing, score as score_settings
from inference import * 


def chatbotWindow():
 #   while True:
    window = Tk()

    window.geometry("500x650")

    window.title("Our Chatbot")

    # icon = PhotoImage(file="chatbot.png")
    # photo = Label(window, image=icon)
    # photo.pack(pady=5)

    frame = Frame(window)

    readBox = Scrollbar(frame)
    message = Listbox(frame,width=80,height=20)

    readBox.pack(side=RIGHT,fill=Y)

    message.pack(side=LEFT,fill=BOTH,pady=10)

    frame.pack()

    textField= Entry(window,font=("Arial",10))
    textField.pack(fill=X,pady=10)

    def ask():
        question = textField.get()
        message.insert(END, "you : " + question)
        try:
            answers = inference_internal(question)[0]#bot.get_response(question)
            if answers is None:
                print(colorama.Fore.RED + "! Question can't be empty" + colorama.Fore.RESET)
            else:
                for i, _ in enumerate(answers['scores']):
                    message.insert(END, "bot : {}".format(answers['answers'][i]))

        except:
            print("Someting wong")
        
        
        #message.insert(END, "bot : " + str(answer))
        textField.delete(0, END)


    btn = Button(window,text="Send",font=10,command=ask)
    btn.pack()

    window.mainloop()
