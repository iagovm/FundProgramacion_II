import sys

def run(path):
 
    with open(path) as f:
        pjs = f.readlines()
        for pj in pjs:
            parse_params(pj.split())

    #TODO: Implement simulation here



def parse_params(params):

    name, life, strength, protection = params[1], int(params[2]), int(params[3]), int(params[4])

    if params[0].lower() == "warrior":
        shield = int(params[5])
        fury = int(params[6])
        print ("Create Warrior  [todo]")
    elif params[0].lower() == "mage":
        mana = int(params[5])
        print ("Create Mage [todo]")
    elif params[0].lower() == "priest":
        mana = int(params[5])
        print ("Create Priest [todo]")
    elif params[0].lower() == "chaman":
        shield = int(params[5])
        mana = int(params[6])
        print ("Create Chaman [todo]")
    else:
        raise ValueError("Avatar '{}' is not valid".format(params[0]))



if __name__ == "__main__":

    run(sys.argv[1])

