print('Welcome to treasure Island ')
choice1=input ("choose left or right: \n")
if choice1=="right":
    print ("fall into a hole \n Game Over")
elif choice1=="left":
    choice2=input("choose swim or wait: \n")
    if choice2=="swim":
        print("game over")
    elif choice2=="wait":
        choice3=input("choose a colour red yellow or blue: \n ")
        if choice3=="red":
            print("game over")
        elif choice3=="blue":
            print ("game over")
        elif choice3=="yellow":
            print("you won")

    
    
