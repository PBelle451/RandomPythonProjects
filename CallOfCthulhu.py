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

def pissChamber():
    directions = ["left", "forward", "backward"]
    global torch
    print("You enter a chamber that smells like urine, you look around but you can barely see what is in front of you. What do you do?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/forward/backward")
        userInput = input()
        if userInput == "left":
            Cultists()
        elif userInput == "forward":
            print("You find a torch barely lit in the ground, you pick it up and now you can see more clearly")
            torch = True
        elif userInput == "backward":
            introScene()
        elif userInput == "right":
            print("You blindly walk to the right but bumps into a wall")
        else:
            print("Please insert a valid option")
        
def altarChamber():
    directions = ["forward", "backward"]
    global torch
    global necronomicon
    print("You enter an altar chamber, dimly lit torches fashion the walls but you can still notice a stone statue at the very end of the hall")
    userInput = ""
    while userInput not in directions:
        print("Options: forward/backward")
        userInput = input()
        if userInput == "forward":
            if torch == True:
                print("You walk towards the stone statue, you brandish your torch over it and notice it's an altar for the deity Cthulhu. Looking at the feet of the statue, you find a book bound in leather, you pick it up")
                necronomicon = True
            else:
                print("You walk towards to the statue but you can't see anything.")
        elif userInput == "backward":
            introScene()
        elif userInput == "left":
            print("You bump into a wall")
        elif userInput == "right":
            print("YOu bump into a wall")
        else:
            print("Please insert a valid option")

def diningHall():
    directions = ["left", "right", "backward"]
    print("You enter a room with a large wooden table at the center, you feel a putrid scent upon entering and look at several plates with food that looks inedible.")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/backward")
        userInput = input()
        if userInput == "left":
            oldGear()
        elif userInput == "right":
            Pantry()
        elif userInput == "backward":
            introScene()
        elif userInput == "forward":
            print("You bump into a wall")
        else:
            print("Please insert a valid option")


if __name__ == '__main__':
    print("Welcome to Call of Cthulhu.")
    print("You are a detective sent to investigate a cult who is trying to summon Cthulhu.")
    print("While interrogating the townsfolk, you came across a strange man.")
    print("He said his name was Zobek Kell and he knew where the cult was hiding.")
    print("While following him, you were knocked out and kidnapped.")
    print("You wake up in a underground cave dimly lit by torches.")
    print("Good luck")
    introScene()