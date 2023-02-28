def introScene():
    directions = ["left", "right", "forward"]
    print("You are at the crossroads, four hallways stand before you. Where will you go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            showShadowFigure()
        elif userInput == "right":
            showSkeletons()
        elif userInput == "forward":
            hauntedRoom()
        elif userInput == "backward":
            print("You find that this door opens into a wall.")
        else:
            print("Please enter a valid option.")

def showShadowFigure():
    directions = ["right", "backward"]
    print("You see a dark shadowy figure appear in the distance. You are creeped out. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/left/backward")
        userInput = input()
        if userInput == "right":
            cameraScene()
        elif userInput == "left":
            print("You find that this door opens into a wall.")
        elif userInput == "backward":
            introScene()
        else:
            print("Please enter a valid option")

def cameraScene():
    directions = ["forward", "backward"]
    print("You see a camera that has been dropped on the ground. Someone has been here recently. Where would you like to do?")
    userInput = ""
    while userInput not in directions:
         print("Options: forward/backward")
         userInput = input()
         if userInput == "forward":
             print("You made it! You've found the exit.")
             quit()
         elif userInput == "backward":
             showShadowFigure()
         else:
             print("Please enter a valid option")

def hauntedRoom():
    directions = ["right", "left", "backward"]
    print("You hear strange voices. You think you have awoken some of the dead. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/left/backward")
        userInput = input()
        if userInput == "right":
            print("Multiple ghoul-like creatures start emerging as you enter the room. You are killed.")
            quit()
        elif userInput == "left":
            print("You made it! You've found an exit.")
            quit()
        elif userInput == "backward":
            introScene()
        else:
            print("Please enter a valid option.")

def showSkeletons():
    directions = ["backward","forward"]
    global weapon
    print("You see a wall of skeletons as you walk into the room. Someone is watching you. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/backward/forward")
        userInput = input()
        if userInput == "left":
            print("you find that this door opens into a wall. You open some of the drywall to discover a hydra dildo")
            weapon = True
        elif userInput == "backward":
            introScene()
        elif userInput == "forward":
            strangeCreature()
        else:
            print("Please enter a valid option")

def strangeCreature():
    actions = ["fight","flee"]
    global weapon
    print("A strange ghoul-like creature has appeared. You can either run or fight it. What would you do?")
    userInput = ""
    while userInput not in actions:
        print("Options: flee/fight")
        userInput = input()
        if userInput == "fight":
            if weapon:
                print("You kill the ghoul with the knife you found earlier. After moving forward, you find one of the exits. Congrats!")
            else:
                print("The ghoul-like creature has killed you.")
                quit()
        elif userInput == "flee":
            showSkeletons()
        else:
            print("Please enter a valid option.")

if __name__ == '__main__':
    while True:
        print("Welcome to the Adventure Game!")
        print("As an avid traveler, you have decided to visit the Catacombs of Paris.")
        print("However, during your exploration, you find yourself lost.")
        print("You can choose to walk in multiple directions to find a way out.")
        print("Let's start with your name: ")
        name = input()
        print("Good luck, ", name, ".")
        introScene()