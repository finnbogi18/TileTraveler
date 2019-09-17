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
        input_dir = input()
        if input_dir == 'n' or input_dir == 'N':
            status = False
            onetwo()
        else:
            print("Not a valid direction!")

def onetwo():
    print("poop")

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
    direction = input('Direction: ')
    return direction