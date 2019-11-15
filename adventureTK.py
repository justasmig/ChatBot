from tkinter import *

state = 0
def addToState():
    global state
    state += 1
def textAdventure(interface):
    global state
    needsToAnswer = False

    window = Toplevel(interface)

    window.geometry("500x650")

    window.title("Adventure")

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
    
    user_input = textField.get()

    if state == 0:
        message.insert(END, "Do you want to play a RPG adventure? ")
        needsToAnswer = False
        state += 1
    elif state == 2:
        opt1 = ["tap","mirror","ceiling","door","closestool"]
        message.insert(END, "When you wake up , you find that you don't know where you are\n"
          "and you don't know when you came but the only thing you know \n"
          "is that you need  trying to get out of here\n"
          "You find yourself in a tiny room that seems to be a toilet\n"
          "In this room there is a tap, mirror, ceiling and door\n"
          "You can choose one to cheek if there is a clue")
        showopt(opt1)
        message.insert(END, "Choose one thing to check: ")
        needsToAnswer = False
        state += 1
    elif state == 4:
        message.insert(END,"What do you want to do with the key? ")
        needsToAnswer = False
        state += 1
        
    
    elif state == 6:
        message.insert(END, "Do you want to open the door with your key? ")
        needsToAnswer = False
        state += 1

    def ask():
        if state == 1:
                if user_input == "yes":
                    state += 1
                else:
                    message.insert(END, "OK,out of game now")                
        elif state == 3:
            if user_input == "tap" or user_input == "1":
                message.insert(END, "You look at the tap, thinking that I need to clear my mind,\n" \
                "but you turn on the faucet to wash your face with cold water,\n" \
                "but what comes out is blood!!!!")
            elif user_input == "mirror" or user_input == "2":
                message.insert(END, "A man emerged from the mirror, \n" \
                    "You nervous look back but nothing in sight \n" \
                    "and the man disappeared when looked back the mirror\n" \
                    "when you glance through the mirror to find that\n" \
                    "up on the ceiling glass you have found a shadow like keys")
            elif user_input == "ceiling" or user_input == "3":
                message.insert(END, "You look at the ceiling which seems to be made of glass\n" \
                    "and there's a lot of stuff on the ceiling but you can't see it because of the shadow")
            elif user_input == "door" or user_input == "4":
                message.insert(END, "You find that the only door was  locked")
            elif user_input == "closestool" or user_input == "5":
                message.insert(END, "you try to stand on the closestool use hand to broken the glass to get the key\n" \
                    "you got the key to successfully")
                state += 1
            else:
                message.insert(END, "Please choose one of the object correctly.")
        elif state == 5:
            if user_input == "open the door" or user_input == "open" or user_input == "door":
                message.insert(END, "You open the door but only find that a wall is behind the door\n" \
                    "You step back in surprise but find that the room you're in has been changed\n" \
                    "And this room is even bigger also in the middle of the room is a cup with a person's eyeball in it\n" \
                    "You walk to it, you look at the eyeball suddenly stare at you \n" \
                    "The world goes round and round and you feel dizzy\n" \
                    "And then you find yourself in the bathroom again\n" \
                    "And the ceiling above you has  became a wooden one also you found this door is locked\n\n" \
                    "SORRY, you lost your key when transfer the room, you can't get out this door\n" \
                    "(tick: open the door and keep the key)\n\n"
                    "You lost so you return to first room now.")
                state = 2
            elif user_input == "open the door and keep the key" or user_input =="keep the key after open the door":
                message.insert(END, "You open the door but only find that a wall is behind the door\n" \
                    "You step back in surprise but find that the room you're in has been changed\n" \
                    "And this room is even bigger also in the middle of the room is a cup with a person's eyeball in it\n" \
                    "You walk to it, you look at the eyeball suddenly stare at you \n" \
                    "The world goes round and round and you feel dizzy\n" \
                    "And then you find yourself in the bathroom again\n" \
                    "And the ceiling above you has  became a wooden one also you found this door is locked\n\n")
                state += 1
            else:
                message.insert(END, "You can only open the door")                
        elif state == 7:
            if user_input == "yes" or user_input == "sure" or user_input == "yeah":
                message.insert(END, "You are ate by the monster behind the door!\n"
                "Don't worried this story only have bad end XD.")
                state = 10
            else:
                message.insert(END, "What you want to do if you don't open the door?")

    btn = Button(window,text="Send",font=10,command=ask)
    btn.pack()
    
    window.mainloop()

# def part1():
#     if user_input == "tap" or user_input == "1":
#         message.insert(END, "You look at the tap, thinking that I need to clear my mind,\n" \
#                "but you turn on the faucet to wash your face with cold water,\n" \
#                "but what comes out is blood!!!!")
#         part1()
#     elif user_input == "mirror" or user_input == "2":
#         message.insert(END, "A man emerged from the mirror, \n" \
#                "You nervous look back but nothing in sight \n" \
#                "and the man disappeared when looked back the mirror\n" \
#                "when you glance through the mirror to find that\n" \
#                "up on the ceiling glass you have found a shadow like keys")
#         part1()
#     elif user_input == "ceiling" or user_input == "3":
#         message.insert(END, "You look at the ceiling which seems to be made of glass\n" \
#                "and there's a lot of stuff on the ceiling but you can't see it because of the shadow")
#         part1()
#     elif user_input == "door" or user_input == "4":
#         message.insert(END, "You find that the only door was  locked")
#         part1()
#     elif user_input == "closestool" or user_input == "5":
#         message.insert(END, "you try to stand on the closestool use hand to broken the glass to get the key\n" \
#                "you got the key to successfully")
#         part2()
#     else:
#         message.insert(END, "Please choose one of the object correctly.")
#         part1()

# def part2():
#     user_input = input("What do you want to do with the key? ")
#     if user_input == "open the door" or user_input == "open" or user_input == "door":
#         message.insert(END, "You open the door but only find that a wall is behind the door\n" \
#                "You step back in surprise but find that the room you're in has been changed\n" \
#                "And this room is even bigger also in the middle of the room is a cup with a person's eyeball in it\n" \
#                "You walk to it, you look at the eyeball suddenly stare at you \n" \
#                "The world goes round and round and you feel dizzy\n" \
#                "And then you find yourself in the bathroom again\n" \
#                "And the ceiling above you has  became a wooden one also you found this door is locked\n\n" \
#                "SORRY, you lost your key when transfer the room, you can't get out this door\n" \
#                "(tick: open the door and keep the key)\n\n"
#                "You lost so you return to first room now.")
#         part1()
#     elif user_input == "open the door and keep the key" or user_input =="keep the key after open the door":
#         message.insert(END, "You open the door but only find that a wall is behind the door\n" \
#                "You step back in surprise but find that the room you're in has been changed\n" \
#                "And this room is even bigger also in the middle of the room is a cup with a person's eyeball in it\n" \
#                "You walk to it, you look at the eyeball suddenly stare at you \n" \
#                "The world goes round and round and you feel dizzy\n" \
#                "And then you find yourself in the bathroom again\n" \
#                "And the ceiling above you has  became a wooden one also you found this door is locked\n\n")
#         end()
#     else:
#         message.insert(END, "You can only open the door")
#         part2()



# def end():
#     #user_input = input("Do you want to open the door with your key? ")
#     if user_input == "yes" or user_input == "sure" or user_input == "yeah":
#         message.insert(END, "You are ate by the monster behind the door!\n"
#               "Don't worried this story only have bad end XD.")
#     else:
#         message.insert(END, "What you want to do if you don't open the door?")
#         end()


def showopt(list):
    message.insert(END, "Here are your options:")
    count = 1
    for opt in list:
        message.insert(END,str(count) + ". " + opt)
        count = count + 1
    message.insert(END,"What would you like to do? ")

#textAdventure()