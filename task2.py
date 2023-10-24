#! python3

# SD Computing Studies Assignment
"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""

def title():
    print("Gess the number!\nEnter a number between 0 and 100\nif wrong enter a new number\nyou have no liment to your atempts\n")

def game():
    count = 1
    anser = '54'
    gess = input("Enter number: ")
    while True:
        if gess == anser:
            break
        elif gess > anser:
            print(f"{gess} is too big")
        elif gess < anser:
            print(f"{gess} is too small")
        count = count + 1
        gess = input("Enter a new number: ")
    print(f"you win in {count} atempts{'!' * count}")

if __name__ == "__main__":
    title()
    game()