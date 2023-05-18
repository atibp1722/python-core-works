import random

def diceRoll():

    dices={
        1: (
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),
    }

    ans=input("Do you want to roll the dice? ").lower()
    while ans=='y':
        dice=random.randint(1,6)
        dice1=random.randint(1,6)

        print(f"Dice rolled {dice} and {dice1}")
        print("\n".join(dices[dice]))
        print("\n".join(dices[dice1]))

        ans=input("Do you want continue?[y/n]: ").lower()
        if ans=='y':
            diceRoll()
        elif ans=='n':
            print("Thank you and goodbye")
            quit()
        else:
            print("Oops, somethinh went wrong")

diceRoll()