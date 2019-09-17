"""
Gera fall fyrir hvert tile og skilgreina hvort hægt sé að fara north, south, west eða south. Nota IF commands sem segja hver maður getur farið
Dæmi:

def 1,1():
    Print("you can travel: (N)orth.")
    input = ("direction:")
    if input == 'n' or input == 'N':
        1,2()
    else:
        print("Not a valid direction")



"""


def dog():
    print("dog poop")


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
            onethree()
        elif input_dir == "w" or input_dir == "W":
            status = False
            threethree()
        else:
            print("Not a valid direction!")


def threeone():
    print("Victory!")


def threetwo():
    print("poop")


def threethree():
    print("poop")


def inputdir():
    direction = input("Direction: ")
    return direction
