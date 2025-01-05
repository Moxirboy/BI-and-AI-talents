import random
attempts = 0
number = random.randint(1,100)
found = False
while (True):
    if attempts == 9:
        print("You lost")
    if attempts == 9 or found:
        ok = ["Yes", "Y", "ok"]
        ch = input("do you wanna play again:")
        if ch in ok:
            number = random.randint(1,100)
            attempts = 0
        else:
            print("bye")
            break
    choice = int(input("enter your choice: "))
    if choice == number:
        print("you are correct")
        found = True
    elif choice > number:
        print("too high")
    else:
        print("too low")
    attempts = attempts + 1
    
