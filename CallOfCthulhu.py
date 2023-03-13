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
            print("You bump into a wall")
        else:
            print("Please insert a valid option")

def diningHall():
    directions = ["left", "backward"]
    print("You enter a room with a large wooden table at the center, you feel a putrid scent upon entering and look at several plates with food that looks inedible.")
    userInput = ""
    while userInput not in directions:
        print("Options: left/backward")
        userInput = input()
        if userInput == "left":
            oldGear()
        elif userInput == "right":
            print("You bump into a wall")
        elif userInput == "backward":
            introScene()
        elif userInput == "forward":
            print("You bump into a wall")
        else:
            print("Please insert a valid option")

def oldGear():
    directions = ["forward", "backward"]
    global torch
    global revolver
    if torch == False:
        print("It's pitch black, you decide to return to the previous room")
        diningHall()
    else:
        print("You enter a room full of cloth and bags scattered through the floor. It's completly dark and you shine your torch through the room.")
        userInput = ""
        while userInput not in directions:
            print("Options: forward/backward")
            userInput = input()
            if userInput == "forward":
                print("You shine your torch and walk through the room, you look around and find your backpack, you search it up and find your old revolver")
                revolver == True
            elif userInput == "backward":
                diningHall()
            elif userInput == "right":
                print("You bump into a wall")
            elif userInput == "left":
                print("You bump into a wall")
            else:
                print("Please insert a valid option")
    
def Cultists():
    directions = ["forward", "backward"]
    global revolver
    global torch
    global necronomicon
    print("You enter a room full of cultists. They are kneeling before a sharp-looking monolith. They are all wearing brown robes and are chanting the words Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn")
    userInput = ""
    while userInput not in directions:
        print("Options: forward/backward")
        userInput = input()
        if userInput == "forward":
            if revolver == True:
                print("You grab your revolver and shoot down all the cultists in the room, they all lie dead before you. You walk towards the monolith where you notice a stop that fits a book.")
                if necronomicon == True:
                    print("You grab the book you found earlier and you put it in the stop of the altar. The pages have a drawing of Cthulhu and several writings which are unreadable for men. You grab the lighter in your coat and you set fire to the pages.")
                    print("As the pages burn, you hear a nightmarish growl that echoes through the chamber. The sheer sound of it drives you insane, you collapse and fall to the ground as the whole building collapses before you.")
                    print("Taking a look to the sky just before you die, you see the cyclopean body of Cthulhu rising from the ocean before you. Cthulhu awakens")
                    quit()
                else:
                    print("You find a trap door near the monolith, you go through it and walk through kilometers of poorly lit tunnels.")
                    print("You find an exit and find yourself in the town once again. You are able to hitchhike a ride back to the police station.")
                    print("You report your findings to your boss and the police raid the cult's headquarters. All the cultists remaining were killed or arrested.")
                    print("The police find the Necronomicon there, it's confiscated and sent to the University of Miskatonic for studies.")
                    print("God knows what the consequences of your actions will be. You are sent home, as you arrive to your doorsteb you notice a letter with the same symbols you saw during that fateful day.")
                    quit()
            else:
                print("The cultists notice you and they run towards you with sacrificial knifes, they stab you multiple times and you fall to the ground dead.")
                print("Cthulhu Awakens")
                quit()

if __name__ == '__main__':
    print("Welcome to Call of Cthulhu.")
    print("You are a detective sent to a town to investigate a cult who is trying to summon Cthulhu.")
    print("While interrogating the townsfolk, you came across a strange man.")
    print("He said his name was Zobek Kell and he knew where the cult was hiding.")
    print("While following him, you were knocked out and kidnapped.")
    print("You wake up in a underground cave dimly lit by torches.")
    print("Good luck")
    introScene()