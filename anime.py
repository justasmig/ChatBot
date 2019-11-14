import webbrowser

anime_name = ["Dr. STONE","Ascendance of a Bookworm","Naruto"]

def anime():
    print("Ok, here's some Anime I know:")
    count=1
    for name in anime_name:
        print(str(count) + ". " + name)
        count = count + 1
    user_input = input("Which one would you like to know? ""\n")
    if user_input == "Dr. STONE" or user_input =="1" or user_input =="1. Dr. STONE":
        return story1()
    elif user_input == "Ascendance of a Bookworm" or user_input =="2" or user_input =="2. Ascendance of a Bookworm":
        return story2()
    elif user_input == "Naruto" or user_input =="3" or user_input =="3. Naruto":
        return story3()
    elif user_input == "Any other animes?" or user_input =="Do you know other animes" or user_input =="I want to know other animes":
        print("Ok, I have a website have video of  Dr. STONE, do you want to open it?")
        user_input = input()
        if user_input == "Sure" or user_input == "Ok" or user_input == "Yes" or user_input == "Yeah" or user_input == "sure" or user_input == "ok" or user_input == "yes" or user_input == "yeah":
            webbrowser.open("https://www.crunchyroll.com/videos/anime")
    else:
        print("Please type the number or the name of these three anime.")
        anime()
def story1():
    print("Introduction of Dr. STONE: ""\n"
          "Several thousand years after a mysterious phenomenon that turns all of humanity to stone,""\n"
          " the extraordinarily intelligent, science-driven boy, Senku Ishigami, awakens.""\n"
          " Facing a world of stone and the total collapse of civilization,""\n"
          " Senku makes up his mind to use science to rebuild the world. ""\n"
          "Starting with his super strong childhood friend Taiju Oki, ""\n"
          "who awakened at the same time, they will begin to rebuild civilization from nothing... ""\n"
          "Depicting two million years of scientific history from the Stone Age to present day, ""\n"
          "the unprecedented crafting adventure story is about to begin!")
    user_input = input()
    if user_input == "I want to see the video." or user_input =="Do you have video of this?" or user_input =="How about video?":
        print( "Ok, I have a website have video of  Dr. STONE, do you want to open it?")
        user_input = input()
        if user_input == "Sure" or user_input == "Ok" or user_input == "Yes" or user_input == "Yeah" or user_input == "sure" or user_input == "ok" or user_input == "yes" or user_input == "yeah":
            webbrowser.open("https://www.crunchyroll.com/dr-stone")
def story2():
    print("Introduction of Ascendance of a Bookworm :""\n"
          " Avid bookworm and college student Motosu Urano ends up dying in an unforeseen accident.""\n"
          " This came right after the news that she would finally be able to work as a librarian like she had always dreamed of. ""\n"
          "When she regained consciousness, she was reborn as Myne, the daughter of a poor soldier. She was in the town of Ehrenfest, ""\n"
          "which had a harsh class system. But as long as she had books, she didn't really need anything else. However, ""\n"
          "books were scarce and belonged only to the nobles. But that doesn't stop her, so she makes a decision... ""\n"
          "'If there aren't any books, I'll just create some.'")
    user_input = input()
    if user_input == "I want to see the video." or user_input == "Do you have video of this?" or user_input == "How about video?":
        print("Ok, I have a website have video of  Dr. STONE, do you want to open it?")
        user_input = input()
        if user_input == "Sure" or user_input == "Ok" or user_input == "Yes" or user_input == "Yeah" or user_input == "sure" or user_input == "ok" or user_input == "yes" or user_input == "yeah":
            webbrowser.open("https://www.crunchyroll.com/ascendance-of-a-bookworm")
def story3():
    print("Introduction of Naruto :""\n"
          " The Village Hidden in the Leaves is home to the stealthiest ninja. But twelve years earlier,""\n"
          " a fearsome Nine-tailed Fox terrorized the village before it was subdued and its spirit sealed within the body of a baby boy.")
    user_input = input()
    if user_input == "I want to see the video." or user_input == "Do you have video of this?" or user_input == "How about video?":
        print("Ok, I have a website have video of  Dr. STONE, do you want to open it?")
        user_input = input()
        if user_input == "Sure" or user_input == "Ok" or user_input == "Yes" or user_input == "Yeah" or user_input == "sure" or user_input == "ok" or user_input == "yes" or user_input == "yeah":
            webbrowser.open("https://www.crunchyroll.com/naruto")

#anime()



