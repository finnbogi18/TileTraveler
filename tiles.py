# Finnbogi Jakobsson og Hákon Hákonarson

""" This function tells you which directions and calls
the next function if input is correct,
if not the user will be asked for a new input.
This is the case for all the functions except inputdir()."""


def oneone():
    print("You can travel: (N)orth.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "n" or input_dir == "N":
            status = False
            onetwo()
        else:
            print("Not a valid direction!")


def onetwo():
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "n" or input_dir == "N":
            status = False
            onethree()
        elif input_dir == "e" or input_dir == "E":
            status = False
            twotwo()
        elif input_dir == "s" or input_dir == "S":
            status = False
            oneone()
        else:
            print("Not a valid direction!")


def onethree():
    print("You can travel: (E)ast or (S)outh.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "e" or input_dir == "E":
            status = False
            twothree()
        elif input_dir == "s" or input_dir == "S":
            status = False
            onetwo()
        else:
            print("Not a valid direction!")


def twoone():
    print("You can travel: (N)orth.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "n" or input_dir == "N":
            status = False
            twotwo()
        else:
            print("Not a valid direction!")


def twotwo():
    print("You can travel: (S)outh or (W)est.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "w" or input_dir == "W":
            status = False
            onetwo()
        elif input_dir == "s" or input_dir == "S":
            status = False
            twoone()
        else:
            print("Not a valid direction!")


def twothree():
    print("You can travel: (E)ast or (W)est.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "e" or input_dir == "E":
            status = False
            threethree()
        elif input_dir == "w" or input_dir == "W":
            status = False
            onethree()
        else:
            print("Not a valid direction!")


# If this function is called, "Victory!" gets printed out.
def threeone():
    print("Victory!")


def threetwo():
    print("You can travel: (N)orth or (S)outh.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "n" or input_dir == "N":
            status = False
            threethree()
        elif input_dir == "s" or input_dir == "S":
            status = False
            threeone()
        else:
            print("Not a valid direction!")


def threethree():
    print("You can travel: (S)outh or (W)est.")
    status = True
    while status == True:
        input_dir = inputdir()
        if input_dir == "w" or input_dir == "W":
            status = False
            twothree()
        elif input_dir == "s" or input_dir == "S":
            status = False
            threetwo()
        else:
            print("Not a valid direction!")


# Asks the user for a direction he wishes to move in.
def inputdir():
    direction = input("Direction: ")
    return direction


# Starts the game with the player in box [1, 1]
oneone()
