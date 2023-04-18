import random 
from questions import QUESTIONS

score = 0

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
    print("The computer will randomly choose a year in the past")
    print("You'll be given a question about an important fact of the year you're at")
    print("Type you're answer and you will travel to a new year destination")
    print("For every right question you'll earn 10 points")
    print("Guess it right and you'll be able to go back to 2023, otherwise I wish you good luck")

def start_game():
    """
    Asks for the username and start the game 
    """
    username = " "
    while True:
        username = input("Please enter your Name: \n")

        if username.isalnum() != True:
            print("Error: Letters and numbers only.")
            continue
        else:
            print(f"Hi {username}!")
            input("When you are ready to time travel, press the Enter key")
            return username

    print(f"Hi {username}!")
    input("When you're ready to time travel, press the Enter key")


def game():
    for key in QUESTIONS:
        print(key)
    answer_input = answer()

    if answer() == QUESTIONS.values():
        print("Spot on!")
    else:
        print("Incorrect!")


def answer():
    """
    Get the answer input from user
    """
    
    answer = input("Write your answer here:\n")
    answer_input = answer

    return answer_input


def main():
    welcome_logo()
    start_game()
    game()
    answer()


main()
