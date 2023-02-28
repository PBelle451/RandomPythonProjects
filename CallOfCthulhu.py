def introScene():
    directions = ["left", "right", "forward"]
    print("You are at the crossroads, four hallways stand before you. What will you do?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            pissChamber()
        elif userInput == "right":
            diningHall()
        elif userInput == "forward":
            altarChamber()
        elif userInput == "backward":
            print("You look back to find a wall behind you.")
        else:
            print("Please insert a valid input.")

if __name__ == '__main__':
    print("Welcome to Call of Cthulhu.")
    print("You are a detective sent to investigate a cult who is trying to summon Cthulhu.")
    print("While interrogating the townsfolk, you came across a strange man.")
    print("He said his name was Zobek Kell and he knew where the cult was hiding.")
    print("While following him, you were knocked out and kidnapped.")
    print("You wake up in a underground cave dimly lit by torches.")
    print("Good luck")
    introScene()