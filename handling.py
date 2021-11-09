def sonutime():
    import datetime
    return datetime.datetime.now()


def lock():
    selectguy=int(input("select your self.........\n1 : Surendra Kushwaha\n2 : Rohit Kushwaha\n3 : Sachin kushwaha\n"))
    if selectguy==1:
        lockitem=int(input("What do you want to lock   1 : for Food   2 : for Gym =   "))
        if lockitem==1:
            food=open("surendrafood.txt","a")
            value=input("Type here : ")
            food.write(str(sonutime())+"  :  "+value+"\n")
            food.close()
            print("Your Food Activity is locked")
        else:
            gym=open("surendragym.txt","a")
            value=input("Type here : ")
            gym.write(str(sonutime())+"  :   "+value+"\n")
            gym.close()
            print("Your Gym Activity is locked")
    elif selectguy==2:
        lockitem = int(input("What do you want to lock   1 : for Food   2 : for Gym =   "))
        if lockitem == 1:
            food = open("rohitfood.txt", "a")
            value = input("Type here : ")
            food.write(str(sonutime()) + "  :  " + value + "\n")
            food.close()
            print("Your Food Activity is locked")
        else:
            gym = open("rohitgym.txt", "a")
            value = input("Type here : ")
            gym.write(str(sonutime()) + "  :   " + value + "\n")
            gym.close()
            print("Your Gym Activity is locked")
    elif selectguy==3:
        lockitem = int(input("What do you want to lock   1 : for Food   2 : for Gym =   "))
        if lockitem == 1:
            food = open("sachinfood.txt", "a")
            value = input("Type here : ")
            food.write(str(sonutime()) + "  :  " + value + "\n")
            food.close()
            print("Your Food Activity is locked")
        else:
            gym = open("sachingym.txt", "a")
            value = input("Type here : ")
            gym.write(str(sonutime) + "  :   " + value + "\n")
            gym.close()
            print("Your Gym Activity is locked")
    else:
        print("Chose the vailed the option..")

def retrive():
    """This is retrive function...."""
    selectguy=int(input("select your self.........\n1 : Surendra Kushwaha\n2 : Rohit Kushwaha\n3 : Sachin kushwaha\n"))
    if selectguy==1:
        lockitem=int(input("What do you want to Retrive   1 : for Food   2 : for Gym =   "))
        if lockitem==1:
            print("\n---------------- Your Food Activity Is --------------")
            food=open("surendrafood.txt","r")
            print(food.read())
            food.close()
        else:
            print("\n----------------- Your Gym Activity is -----------------")
            gym=open("surendragym.txt","r")
            print(gym.read())
            gym.close()
    elif selectguy==2:
        lockitem=int(input("What do you want to  Retrive   1 : for Food   2 : for Gym =   "))
        if lockitem==1:
            print("\n---------------- Your Food Activity Is --------------")
            food=open("rohitfood.txt","r")
            print(food.read())
            food.close()
        else:
            print("\n----------------- Your Gym Activity is -----------------")
            gym=open("rohitgym.txt","r")
            print(gym.read())
            gym.close()
    elif selectguy==3:
        lockitem=int(input("What do you want to  Retrive   1 : for Food   2 : for Gym =   "))
        if lockitem==1:
            print("\n---------------- Your Food Activity Is --------------")
            food=open("sachinfood.txt","r")
            print(food.read())
            food.close()
        else:
            print("\n----------------- Your Gym Activity is -----------------")
            gym=open("sachingym.txt","r")
            print(gym.read())
            gym.close()
    else:
        print("Chose the vailed the option..")
def exit():
    print("\nTHANKS FOR USINGGGGG.....")
try:
    print("-------------------This is my Helth Management---------------------------\n")
    while(1):
        a=int(input("You want to lock press - 1 \nYou want to Retrive press - 2\nYou Want To Exit - 3"))
        if a==1:
            lock()
        elif a==2:
            print(retrive.__doc__)  #For calling to docstring..............
            retrive()
        else:
            exit()
            break
except Exception as e:
    print(e)

