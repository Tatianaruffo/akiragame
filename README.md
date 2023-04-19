# Time Machine

Time Machine is a quiz game developed as a a Project 3 for Code Institute’s Full-Stack Web Development course.

The idea of the game is that the user enters a Time Machine which will travel to different historic moments of the world.
The user needs to guess all the answers correct in order to go back to the present(2023). 

![Responsice Mockup]()

Play the game [here]! ()

## CONTENTS

* [How to play](#how-to-play)
  * [Project Goals](#project-goals)

* [User Experience](#user-experience)
  * [User Expectations](#user-expectations)
  * [User Stories](#user-stories)

* [Features](#features)
  * [Welcome Logo](#welcome-logo)
  * [Story](#story)
  * [Name input](#name-input)
  * [Quiz](#quiz)
  * [Quiz end messages](#quiz-end-messages)
  * [Quiz replay](#quiz-replay)

* [Flow Chart](#flow-chart)

* [Future Implementations](#future-implementations)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Programs Used](#programs-used)

* [Deployment](#deployment)

* [Testing](#testing)

* [Credits](#credits)
  * [Code used and adapted](#code-used-and-adapted)
  * [Acknowledgments](#acknowledgments)

---

## How to Play
 1. - In the beginning of the game you will be asked to enter your username, choose a name and press enter.

 2. - The game will load and you will get 6 different questions with 3 answer options (a,b or c).<br>Answer the questions with the letter which has the correct answer.

 3. - Answer all the questions then you will see your total score. <br>If you get all 6 questions right you'll receive a Well Done message.

 4. - You can repeat the game or finish it.

### Project Goals
 - Develop quiz game using Python
 - Present the quiz in a clean and easy to understand manner
 - Keep good UX principles regarding colours/interaction
 - Robust Python code without issues/bugs

## Features

### Application Elements

The below elements are available to be experienced by the user across the quiz game application as a whole.

### Welcome Logo

* Quote and ASCII art

![Welcome Logo](docs/WelcomeLogo.JPG)

### Introduction and instructions 

* Shows the story of the game, the rules and asks for the username 

![Introduction](docs/introduction.gif)

* Asks if the user wants to start the game
* If the user answer "y" the quiz starts

![Start-game](docs/startgame.gif)

* If the user answer "n" the it gives another chance to input y, if not it ends the game

![end-game](docs/endgame.gif)

### Questions

* The Quiz contains 6 questions, with 3 choices each

![quiz](docs/quiz.gif)

* If the user answer all 6 questions right a special "Well Done" message appears
* At the end the user can choose if wants to play the quiz again, if yes the game restarts 

![endquiz](docs/endquiz.gif)

* If the user insert a different input than a,b or c it shows incorrect and goes back to the same question

![wrong-input](docs/wrongInput.gif)



## Flow Chart
![Flowchart](docs/Flowchart.jpg)