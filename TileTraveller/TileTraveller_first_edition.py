# tile3 tile6 tile9
# tile2 tile5 tile8
# tile1 tile4 tile7
# 
# forritið keyrir endalaust þar til þú vinnur eða hættir 
#
# svo verður skoðað hvar notandin er staddur í kóðanum í hverju hring 
# og fær input samkvæmt því 
#####################################################
Position = 1
print("You can travel: (N)orth.")
while 1 == 1:
    #tile1
    if Position == 1:
        Direction = input("Direction: ")
        Direction = Direction.upper()
        if Direction == "N":
            Position += 1
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        else:
            print("Not a valid direction!")
    #tile2
    elif Position == 2:
        Direction = input("Direction: ")
        Direction = Direction.upper()
        if Direction == "N":
            Position += 1
            print("You can travel: (E)ast or (S)outh.")
        elif Direction == "E":
            Position += 3
            print("You can travel: (S)outh or (W)est.")
        elif Direction == "S":
            Position -= 1
            print("You can travel: (N)orth.")
        else:
            print("Not a valid direction!")
    #tile3
    elif Position == 3:
        Direction = input("Direction: ")
        Direction = Direction.upper()
        if Direction == "E":
            Position += 3
            print("You can travel: (E)ast or (W)est.")
        elif Direction == "S":
            Position -= 1
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        else:
            print("Not a valid direction!")
    #tile4
    elif Position == 4:
        Direction = input("Direction: ")
        Direction = Direction.upper()
        if Direction == "N":
            Position += 1
            print("You can travel: (S)outh or (W)est.")
        else:
            print("Not a valid direction!")
    #tile5
    elif Position == 5:
        Direction = input("Direction: ")
        Direction = Direction.upper()
        if Direction == "S":
            Position -= 1
            print("You can travel: (N)orth.")
        elif Direction == "W":
            Position -= 3
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        else:
            print("Not a valid direction!")
    #tile6
    elif Position == 6:
        Direction = input("Direction: ")
        Direction = Direction.upper()
        if Direction == "E":
            Position += 3
            print("You can travel: (S)outh or (W)est.")
        elif Direction == "W":
            Position -= 3
            print("You can travel: (E)ast or (S)outh.")
        else:
            print("Not a valid direction!")
    #tile7
    elif Position == 7:
        break
    #tile8
    elif Position == 8:
        Direction = input("Direction: ")
        Direction = Direction.upper()
        if Direction == "N":
            Position += 1
            print("You can travel: (S)outh or (W)est.")
        elif Direction == "S":
            Position -= 1
        else:
            print("Not a valid direction!")
    #tile9
    elif Position == 9:
        Direction = input("Direction: ")
        Direction = Direction.upper()
        if Direction == "S":
            Position -= 1
            print("You can travel: (N)orth or (S)outh.")
        elif Direction == "W":
            Position -= 3
            print("You can travel: (E)ast or (W)est.")
        else:
            print("Not a valid direction!")
        
print("Victory!")