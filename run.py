import time
import sys
import colorama
import os
from colorama import Fore
colorama.init(autoreset=True) 
from questions import question1, question2, question3, question4, question5, question6

SCORE = 0
NAME = ""


def typing_print(text):
    """
    Creates effects of Typing for the text
    taken from https://www.101computing.net/python-typing-text-effect/
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def clear_screen():
    """
    Clear the terminal
    """
    os.system("clear")


def welcome_logo():
    """
    Display ASCII game logo on the terminal,
    Display the explanation of how the game works
    """
    print(Fore.GREEN + 'Presenting:')
    print(Fore.RED + r"""
        
 ______ _              __  ___            __    _          
/_  __/(_)__ _  ___   /  |/  /___ _ ____ / /   (_)___  ___ 
 / /  / //  ' \/ -_) / /|_/ // _ `// __// _ \ / // _ \/ -_)
/_/  /_//_/_/_/\__/ /_/  /_/ \_,_/ \__//_//_//_//_//_/\__/ 
                                                           
        """)
    time.sleep(1)
    typing_print("The computer will randomly choose a year in the past")
    time.sleep(0.5)
    typing_print("\nYou'll be given a question about an important fact")
    time.sleep(0.5)
    typing_print("\nof the year you're at")
    time.sleep(0.5)
    typing_print("\nType your answer and you will travel to a new destination")
    time.sleep(0.5)
    typing_print("\nFor every right question you'll earn 1 point")
    time.sleep(0.5)
    typing_print("\nAnd for every wrong question you'll loose 1 point")
    time.sleep(0.5)
    typing_print("\nGuess it right and you'll be able to go back to 2023")
    time.sleep(0.5)
    typing_print("\nOtherwise I wish you a good luck\n")


def username_input():
    """
    Asks for the username and if the user wants to start the game 
    """
    global NAME 
    NAME = input("\nPlease enter your name and press Enter: \n")

    if NAME.isalnum() != True:
        print("Error: Letters and numbers only.")
        username_input()
    else:
        start_quiz = input(f"Hi {NAME}! Are you ready to time travel?(y/n) ")
            
    while start_quiz != "y":
        start_quiz = input(f"Please enter 'y' to begin {NAME}, or, if you're not ready, "
                           "press enter and complete the quiz another time: ")
        print(' ')
        clear_screen()
        print(Fore.GREEN + 'Maybe next time!\n')
        time.sleep(1)
        print(Fore.GREEN + 'Powering down Time Machine....\n')
        exit()

    if start_quiz.lower() == "y":
        typing_print("\nStarting engines!\n")
        typing_print("\nJust one more second....\n")
        typing_print("\nLet's play!!")
        time.sleep(3.0)
        os.system('cls' if os.name == 'nt' else 'clear')

    return NAME


def game():
    global SCORE
    questions = {question1: "a", question2: "b", question3: "a", question4: "b", question5: "c", question6: "b"}
    for i in questions:
        print(Fore.GREEN + i)
        ans = input("Write your answer here(a/b/c):\n")
        if ans == questions[i]:
            print("Spot on!")
            SCORE = SCORE+1
            print("Current score is:", SCORE)
            time.sleep(3.5)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Incorrect!")
            SCORE = SCORE-1
            print("Current score is:", SCORE)
            time.sleep(3.5)
            os.system('cls' if os.name == 'nt' else 'clear')
    print("Final score is:", SCORE)

    if SCORE == 6:
        typing_print("Well Done! You are now able to go back to 2023...")
        typing_print("Have a safe journey!\n")


def replay_game():
    """
    Asks if the user wants to restart the game
    if yes the game runs again
    if no it terminates the applicationtatu
    """
    replay = input(Fore.RED + "\nWould you like to try again? (y/n)\n")
    if replay == "y":
        print(Fore.GREEN + 'Restarting game...\n')
        time.sleep(1)
        clear_screen()
        welcome_logo()
        username_input()
        game()
        replay_game()
        return True
    elif replay == "n":
        print(' ')
        clear_screen()
        print(Fore.GREEN + 'Powering down Time Machine...\n')
        time.sleep(1)
        print(Fore.GREEN + 'Thank you for playing.\n')
        return False
    elif input not in {replay == "y", replay == "n"}:
        print(Fore.RED + "Invalid input submitted. Please enter 'y' or 'n'")
        time.sleep(1)
        replay_game()


def main():
    welcome_logo()
    username_input()
    game()
    replay_game()

main()
