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
        if input_dir == "s" or input_dir == "S":
            status = False
            oneone()
        else:
            print("Not a valid direction!")


def onethree():
    print("poop")


def twoone():
    print("poop")


def twotwo():
    print("poop")


def twotree():
    print("poop")


def threeone():
    print("poop")


def threetwo():
    print("poop")


def threethree():
    print("poop")


def inputdir():
    direction = input("Direction: ")
    return direction
