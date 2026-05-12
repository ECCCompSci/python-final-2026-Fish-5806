# ============================================================
# Python Final Project 2026
# Name: 
# Date: 
# Project Title: 
# Description: (Write 1-2 sentences explaining what your program does)
# ============================================================


# ---- SECTION 1: Setup / Variables ----
# Create your starting variables here.
# Example: player_name = ""
import random
easy = random.randint(1, 10)
hard = random.randint(1, 100)




# ---- SECTION 2: Welcome Message ----
# Greet the user and explain what your program does.

print("Welcome to the Number Guessing Game!")
print("In this game you will try to guess a random number")


# ---- SECTION 3: Get Input from User ----
# Use input() to ask the user for information.
# Remember: input() always returns a string.
# Use int() or float() if you need a number.

# Example:
# player_name = input("What is your name? ")
# score = int(input("Enter a number: "))

gamemode = input("easy mode or hard mode?").strip().lower()
guessE = ''
guessH = ''



# ---- SECTION 4: Logic (if / elif / else) ----
# Use if/elif/else to make decisions based on user input or variables.

# Example:
# if score >= 90:
#     print("Great job!")
# elif score >= 70:
#     print("Good work!")
# else:
#     print("Keep practicing!")


if gamemode == "easy":
    while guessE != easy:
        guessE = int(input("pick a number 1-10"))
        if guessE > easy and guessE < 10:
            print("Lower, try again")
        elif guessE < easy and guessE > 0:
            print("Higher, try again")
        elif guessE > 10:
            print("Out of range, try again.")
        elif guessE < 0:
            print("Out of range, try again.")
        elif guessE == easy:
            print(f"You Win!, the secret number was {easy}! reset to play again")
        else:
            print("Invalid input")
        
elif gamemode == "hard":
 
    while guessH != hard:
        guessH = int(input("pick a number 1-100"))
        if guessH > hard and guessH < 100:
            print("Lower, try again")
        elif guessH < hard and guessH > 0:
            print("Higher, try again")
        elif guessH > 10:
            print("Out of range, try again.")
        elif guessH < 1:
            print("Out of range, try again.")
        elif guessH == hard:
            print(f"You Win!, the secret number was {hard}! reset to play again")
        else:
            print("Invalid input")
else:
    print("Invalid input, reset")



# ---- SECTION 5: Final Output ----
# Print a final message, result, or summary to the user.

