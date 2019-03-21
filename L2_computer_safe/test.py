try:
    mode = int(input("choose selected mode by entering one of the formentioned numbers: "))
    while (mode>=1) or (mode<=4):
        break
except ValueError:
        print("That is not a number, please enter a number.")
else:
    print("range")


