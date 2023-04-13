import random 

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

def choose_year():
    """
    Loop through the list of years to randomly choose a year
    """
    years = [1859, 1920, 1939, 1961, 1983, 2001]
    chosen_year = random.choice(years)

    return chosen_year


def show_question():
    """
    Show the question about the respective year 
    """
    if chosen_year == 1859:
        print("In 1859 the 'Origin of Species' was published, what's the name pf it's author?")
        ans = input("Write your answer here: \n")
        if ans == "Charles Darwin":
            score += 10
            print("Spot on!")
        else:
            print("Incorrect!")
    elif chosen_year == 1920:
        print("In 1920 the 19th amendment granted women the right to vote. What was the name of the movement that fought for this right?")
        ans = input("Write your answer here: \n")
        if ans == "suffrage" or "suffragists":
            score += 10
            print("Spot on!")
        else:
            print("Incorrect!")
    elif chosen_year == 1939:
        print("1st of September of 1939 was the beggining of World War II")
        print("Danzing Harbor was the first place attacked by the Germans")
        print("In which country is Danzing Harbor located?")
        ans = input("Write your answer here: \n")
        if ans == "Poland":
            score += 10
            print("Spot on!")
        else:
            print("Incorrect!")
    elif chosen_year == 1961:
        print("In 1961 the Berlin Wall was built")
        print("The wall would serve as an enduring symbol of which war?")
        ans = input("Write your answer here: \n")
        if ans == "cold war":
            score += 10
            print("Spot on!")
        else:
            print("Incorrect!")
    elif chosen_year == 1983:
        print("At the beginning of 1983, the Internet was born.")
        print("The Advanced Research Projects Agency Network (ARPANET), transitions to the standard TCP/IP protocol of the WWW, what WWW stands for?")
        ans = input("Write your answer here: \n")
        if ans == "World Wide Web":
            score += 10
            print("Spot on!")
        else:
            print("Incorrect!")
    elif chosen_year == 2001:
        print("On the 11th of September, 2001 hijackers inspired by Islamist extremism killdc nearly 3,000 people after crashing commercial aircrafts into a famous Manhattan building")
        print("What was the name of this building?")
        ans = input("Write your answer here: \n")
        if ans == "World Trade Center":
            score += 10
            print("Spot on!")
        else:
            print("Incorrect!")
    



def main():
    welcome_logo()
    start_game()
    choose_year()
    chosen_year = choose_year()
    show_question()

main()
