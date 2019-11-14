def textAdventure():
    user_input= input("Do you want to play a RPG adventure? ")
    if user_input == "yes":
        return story()
    else:
        print("OK,out of game now")
def story():
    opt1 = ["tap","mirror","ceiling","door","closestool"]
    print("When you wake up , you find that you don't know where you are\n"
          "and you don't know when you came but the only thing you know \n"
          "is that you need  trying to get out of here\n"
          "You find yourself in a tiny room that seems to be a toilet\n"
          "In this room there is a tap, mirror, ceiling and door\n"
          "You can choose one to cheek if there is a clue")
    showopt(opt1)
    part1()
def part1():
    user_input = input("Choose one thing to check: ")
    if user_input == "tap" or user_input == "1":
        print("You look at the tap, thinking that I need to clear my mind,\n" \
               "but you turn on the faucet to wash your face with cold water,\n" \
               "but what comes out is blood!!!!")
        part1()
    elif user_input == "mirror" or user_input == "2":
        print ("A man emerged from the mirror, \n" \
               "You nervous look back but nothing in sight \n" \
               "and the man disappeared when looked back the mirror\n" \
               "when you glance through the mirror to find that\n" \
               "up on the ceiling glass you have found a shadow like keys")
        part1()
    elif user_input == "ceiling" or user_input == "3":
        print ("You look at the ceiling which seems to be made of glass\n" \
               "and there's a lot of stuff on the ceiling but you can't see it because of the shadow")
        part1()
    elif user_input == "door" or user_input == "4":
        print ("You find that the only door was  locked")
        part1()
    elif user_input == "closestool" or user_input == "5":
        print ("you try to stand on the closestool use hand to broken the glass to get the key\n" \
               "you got the key to successfully")
        part2()
    else:
        print("Please choose one of the object correctly.")
        part1()

def part2():
    user_input = input("What do you want to do with the key? ")
    if user_input == "open the door" or user_input == "open" or user_input == "door":
        print("You open the door but only find that a wall is behind the door\n" \
               "You step back in surprise but find that the room you're in has been changed\n" \
               "And this room is even bigger also in the middle of the room is a cup with a person's eyeball in it\n" \
               "You walk to it, you look at the eyeball suddenly stare at you \n" \
               "The world goes round and round and you feel dizzy\n" \
               "And then you find yourself in the bathroom again\n" \
               "And the ceiling above you has  became a wooden one also you found this door is locked\n\n" \
               "SORRY, you lost your key when transfer the room, you can't get out this door\n" \
               "(tick: open the door and keep the key)\n\n"
               "You lost so you return to first room now.")
        part1()
    elif user_input == "open the door and keep the key" or user_input =="keep the key after open the door":
        print("You open the door but only find that a wall is behind the door\n" \
               "You step back in surprise but find that the room you're in has been changed\n" \
               "And this room is even bigger also in the middle of the room is a cup with a person's eyeball in it\n" \
               "You walk to it, you look at the eyeball suddenly stare at you \n" \
               "The world goes round and round and you feel dizzy\n" \
               "And then you find yourself in the bathroom again\n" \
               "And the ceiling above you has  became a wooden one also you found this door is locked\n\n")
        end()
    else:
        print("You can only open the door")
        part2()



def end():
    user_input = input("Do you want to open the door with your key? ")
    if user_input == "yes" or user_input == "sure" or user_input == "yeah":
        print("You are ate by the monster behind the door!\n"
              "Don't worried this story only have bad end XD.")
    else:
        print("What you want to do if you don't open the door?")
        end()


def showopt(list):
    print("Here are your options:")
    count = 1
    for opt in list:
        print(str(count) + ". " + opt)
        count = count + 1
    print("What would you like to do? ")

#textAdventure()