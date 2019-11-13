from tkinter import *
from chatbotUtils.setup.settings import hparams, out_dir, preprocessing, score as score_settings
from chatbotUtils.inference import * 


def chatbotWindow():
    inference = start_inference("test")
    while True:
        window = Tk()

        window.geometry("500x650")

        window.title("Our Chatbot")


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
            answers = start_inference(question)[0]#bot.get_response(question)
            if answers is None:
                print(colorama.Fore.RED + "! Question can't be empty" + colorama.Fore.RESET)
            else:
                for i, _ in enumerate(answers['scores']):
                    message.insert(END, "bot : " + "{}- {}{} [{}] {}{}{}".format(colorama.Fore.GREEN if answers['scores'][i] == max(answers['scores']) and answers['scores'][i] >= score_settings['bad_response_threshold'] else colorama.Fore.YELLOW if answers['scores'][i] >= score_settings['bad_response_threshold'] else colorama.Fore.RED, answers['answers'][i], colorama.Fore.RESET, answers['scores'][i], colorama.Fore.BLUE, answers['score_modifiers'][i] if score_settings['show_score_modifiers'] else '', colorama.Fore.RESET))

            
            textField.delete(0, END)


        btn = Button(window,text="Send",font=10,command=ask)
        btn.pack()

        window.mainloop()
