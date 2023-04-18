import random 
from questions import question1, question2, question3, question4, question5, question6
import time

SCORE = 0
NAME = ""

def welcome_logo():
    """
    Display ASCII game logo on the terminal,
    Display the explanation of how the game works
    """
    print('Presenting:')
    print(r"""
        
 ______ _              __  ___            __    _          
/_  __/(_)__ _  ___   /  |/  /___ _ ____ / /   (_)___  ___ 
 / /  / //  ' \/ -_) / /|_/ // _ `// __// _ \ / // _ \/ -_)
/_/  /_//_/_/_/\__/ /_/  /_/ \_,_/ \__//_//_//_//_//_/\__/ 
                                                           
        """)
    time.sleep(1)
    print("The computer will randomly choose a year in the past")
    time.sleep(0.5)
    print("You'll be given a question about an important fact of the year you're at")
    time.sleep(0.5)
    print("Type you're answer and you will travel to a new year destination")
    time.sleep(0.5)
    print("For every right question you'll earn 10 points")
    time.sleep(0.5)
    print("Guess it right and you'll be able to go back to 2023, otherwise I wish you good luck")


def username_input():
    """
    Asks for the username and if the user wants to start the game 
    """
    global NAME 
    NAME = input("Please enter your name and press Enter: \n")

    if NAME.isalnum() != True:
        print("Error: Letters and numbers only.")
    else:
        start_quiz = input(f"Hi {NAME}! Are you ready to time travel? (y/n)")
            
    while start_quiz != "y":
        start_quiz = input(f"Please enter 'y' to begin {NAME}, or, if you're not ready, "
                           "press Enter to stop and complete the quiz another time: ")
        break

    if start_quiz.lower() == "y":
        print("Engines on! Let's start. Good luck!\n")

    return NAME


def game():
    global SCORE
    questions = {question1: "a", question2: "b", question3: "a", question4: "b", question5: "c", question6: "b"}
    for i in questions:
        print(i)
        ans = input("Write your answer here(a/b/c):\n")
        if ans == questions[i]:
            print("Spot on!")
            score = SCORE+1
        else:
            print("Incorrect!")
            score = SCORE-1



def main():
    welcome_logo()
    username_input()
    game()


main()
