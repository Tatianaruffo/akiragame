def welcome_logo():
    """
    Display ASCII game logo on the terminal.
    """
    print('Presenting:')
    print(r"""
        
 ______ _              __  ___            __    _          
/_  __/(_)__ _  ___   /  |/  /___ _ ____ / /   (_)___  ___ 
 / /  / //  ' \/ -_) / /|_/ // _ `// __// _ \ / // _ \/ -_)
/_/  /_//_/_/_/\__/ /_/  /_/ \_,_/ \__//_//_//_//_//_/\__/ 
                                                           
        """)

def game_rules():
    """
    Display the explanation of how the game works 
    """
    print("Press any key to start\n")
    print("The computer will randomly choose a year in the past")
    print("You'll be given a question about an important fact of the year you're at")
    print("Type you're answer and you will travel to a new year destination")
    print("For every right question you'll earn 10 points")
    print("Guess it right and you'll be able to go back to 2023, otherwise I wish you good luck")



print(welcome_logo())
print(game_rules())
