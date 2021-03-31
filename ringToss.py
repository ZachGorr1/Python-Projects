def Main():
    welcome()

    if userInput == True:
        print("You tossed a ring.")
        for _ in range(1):
            value = randint(0, 3)
        
        if value == 1:
            SmallPrize()
        
        elif value == 2:
            MediumPrize()
        
        elif value == 3:
            LargePrize()

    elif userInput == False:
        print("You decided not to throw a ring.")

    if userInput != True or False:
        print("That is not a valid response...")
    
def welcome():
    print("Welcome to Ring Toss!")
    print("You may toss one ring.")

    print("There are three bottles, teir 1, 2, and 3.")
    print("Teir 1 being the easiest, and Teir 3 being the hardest.")

    print("Would you like to toss a ring?")
    print("Enter YES or NO.")

    userInput = input()

    if userInput == "YES":
        userInput == True
    
    elif userInput == "NO"
        userInput == False
    
    else if userInput != "YES" or "NO":
        print("Not a vaild awnser...")

    return userInput

def SmallPrize():

    for _ in range(1):
        value = randint(0, 3)
    if value == 3:
        print("You won a Small Prize!")
    else:
        print("You hit zero bottles, Sorry...")

def MediumPrize():

    for _ in range(1):
        value = randint(0, 7)
    if value == 7:
        print("You won a Medium Prize!")
    else:
        print("You hit zero bottles, Sorry...")

def LargePrize():

    for _ in range(1):
        value = randint(0, 10)
    if value == 10:
        print("You won a Large Prize!")
    else:
        print("You hit zero bottles, Sorry...")
