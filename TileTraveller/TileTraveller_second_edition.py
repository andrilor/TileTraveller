# tile3 tile6 tile9
# tile2 tile5 tile8
# tile1 tile4 tile7
# 
# forritið keyrir endalaust þar til þú vinnur eða hættir 
#
# svo verður skoðað hvar notandin er staddur í kóðanum í hverju hring 
# og fær input samkvæmt því 
###############################################################################################################################
# 1. Which implementation was easier and why?
#
# Fyrri var einfaldari þar sem maður var bara ælla út kóða til að láta þetta virka án falla en eftir að hafa klárað seinna 
# þá er ég miklu sáttari með það þar sem það er miklu fallegra og ekki nálægt því eins mikil spaghetti kóði og fyrra.
#
# 2. Which implementation is more readable and why?
#
# Seinni út af því að ef þú lokar föllunum með því að ýtta á - takkan við hliðin á def þá er miklu einfaldara að fatta 
# hvað forritið á að vera að gera.
#
# 3. Which problems in the first implementations were you able to solve with the latter implementation?
# 
# fyrir utan að gera kóðan meira lesanlegri þá var það ekkert sérstakt. Setti "while not Victory" í staðin fyrir "while 1==1" 
# og break-a mann út sem ég fyla betur.
# 
###############################################################################################################################
list_of_Directions = "NSWE"
Position = 1
Victory = False
def Directions(way,locationation):
    """ 
    ---------------------------------------------------------------------------------------------------------------------------
    Fallið Directions er reiknings hluti forritisins þar sem reyknað er í hvaða reitt þú ert stadur eftir að hafa gefið átt.
    ---------------------------------------------------------------------------------------------------------------------------
    """
    if way == "N":
        locationation += 1
    elif way == "S":
        locationation -= 1
    elif way == "W":
        locationation -= 3
    elif way == "E":
        locationation += 3
    return locationation
def error(locationation):
    """ 
    ---------------------------------------------------------------------------------------------------------------------------
    Fallið error tekur  þig til hliðar ef þú gerir villu í fyrstur tilraun og lætur þig reyna aftur og aftur þar til þú slærð 
    inn átt sem hægt er að fara í frá tiltekturm reitt.
    ---------------------------------------------------------------------------------------------------------------------------
    """
    if locationation == 1 or locationation == 4:
        while locationation == 1 or locationation == 4:
            print("Not a valid direction!")
            Direction = input("Direction: ").upper()
            if Direction == list_of_Directions[0]:
                locationation = Directions(Direction, locationation)
                return locationation
    elif locationation == 2:
        while locationation == 2:
            print("Not a valid direction!")
            Direction = input("Direction: ").upper()
            if Direction == list_of_Directions[0] or Direction == list_of_Directions[1] or Direction == list_of_Directions[3]:
                locationation = Directions(Direction, locationation)
                return locationation
    elif locationation == 3:
        while locationation == 3:
            print("Not a valid direction!")
            Direction = input("Direction: ").upper()
            if Direction == list_of_Directions[1] or Direction == list_of_Directions[3]:
                locationation = Directions(Direction, locationation)
                return locationation
    elif locationation == 5 or locationation == 9:
        while locationation == 5 or locationation == 9:
            print("Not a valid direction!")
            Direction = input("Direction: ").upper()
            if Direction == list_of_Directions[1] or Direction == list_of_Directions[2]:
                locationation = Directions(Direction, locationation)
                return locationation
    elif locationation == 6:
        while locationation == 6:
            print("Not a valid direction!")
            Direction = input("Direction: ").upper()
            if Direction == list_of_Directions[2] or Direction == list_of_Directions[3]:
                locationation = Directions(Direction, locationation)
                return locationation
    elif locationation == 8:
        while locationation == 8:
            print("Not a valid direction!")
            Direction = input("Direction: ").upper()
            if Direction == list_of_Directions[0] or Direction == list_of_Directions[1]:
                locationation = Directions(Direction, locationation)
                return locationation
""" 
---------------------------------------------------------------------------------------------------------------------------
Forritið keyrir þar til Victory verður True sem gerist eingöngu ef þú nærð á reitt 7
---------------------------------------------------------------------------------------------------------------------------
"""
while not Victory:
    if Position == 1 or Position == 4:
        print("You can travel: (N)orth.")
        Direction = input("Direction: ").upper()
        if Direction == list_of_Directions[0]:
            Position = Directions(Direction, Position)
        else:
            Position = error(Position)
    elif Position == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        Direction = input("Direction: ").upper()
        if Direction == list_of_Directions[0] or Direction == list_of_Directions[1] or Direction == list_of_Directions[3]:
            Position = Directions(Direction, Position)
        else:
            Position = error(Position)
    elif Position == 3:
        print("You can travel: (E)ast or (S)outh.")
        Direction = input("Direction: ").upper()
        if Direction == list_of_Directions[1] or Direction == list_of_Directions[3]:
            Position = Directions(Direction, Position)
        else:
            Position = error(Position)
    elif Position == 5 or Position == 9:
        print("You can travel: (S)outh or (W)est.")
        Direction = input("Direction: ").upper()
        if Direction == list_of_Directions[1] or Direction == list_of_Directions[2]:
            Position = Directions(Direction, Position)
        else:
            Position = error(Position)
    elif Position == 6:
        print("You can travel: (E)ast or (W)est.")
        Direction = input("Direction: ").upper()
        if Direction == list_of_Directions[2] or Direction == list_of_Directions[3]:
            Position = Directions(Direction, Position)
        else:
            Position = error(Position)
    elif Position == 7:
        print("Victory!")
        Victory = True
    elif Position == 8:
        print("You can travel: (N)orth or (S)outh.")
        Direction = input("Direction: ").upper()
        if Direction == list_of_Directions[0] or Direction == list_of_Directions[1]:
            Position = Directions(Direction, Position)
        else:
            Position = error(Position)