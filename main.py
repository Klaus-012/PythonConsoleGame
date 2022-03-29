# Modular program for Game design

# importing the random number generator module
import random


# Constants
GENERATED_NUMBER = random.randint(1,100)
GAME_TITLE = "OCTO GAMES"
LINE = "------------------------"

# Hi-Lo guessing game. A number is generated at random and the user has to guess what the number is
# the user is asked to enter the secret number
def getValue():
    x = int(input("Guess the secret number: "))
    return x

# a loop is run 10 times and the user input is compared to the secret number for 10 tries
# if 10 tries are exceeded, the user is shown the value
def guessingGame():
    print("You have 10 tries to guess the number")
    print("Hint : The generated number is " + str(GENERATED_NUMBER))
    for i in range (0, 10):
        print("Try number: " + str(i + 1))
        user_number = getValue()
        if user_number < GENERATED_NUMBER:
            print("The number is too low")
        elif user_number > GENERATED_NUMBER:
            print("The number is too high")
        else:
            print("Congratulations you won !!!")
            break
    print("\nThe winning number was " + str(GENERATED_NUMBER))

# This is the madlibs game user inputs. Words are collected from the user and put into a list
def getWords():
    print("Welcome to the Madlibs game please fill in the words as directed")
    name = input("Enter your name: ")
    alias = input("What's your nickname: ")
    favorite_food = input("Whats's your favorite food ")
    favorite_color = input("Whats's your favorite color: ")
    favorite_superhero = input("Enter your favorite super hero: ")
    superhero_movie = input("Which movie is the hero from: ")
    favorite_subject = input("Whats's your favorite subject: ")
    favorite_movie = input("Whats's your favorite movie: ")
    times_watched = int(input("How many times have you watched it: "))
    return[name, alias, favorite_food, favorite_color, favorite_superhero, favorite_subject, favorite_movie, superhero_movie, times_watched]

# The list from the getWords function is passed into the madLibs function and specific words are inserted into the mad libs paragraphs
def madLibs():
    paragraph = getWords()
    print("\nYou know it’s a bad day when you jump out of bed and miss the floor!")
    print("Hi, my name is " + paragraph[0] + " but my friends call me " + paragraph[1])
    print("I have travelled around and tasted different cuisines but i'll say nothing tastes as good as " + paragraph[2])
    print("Especially when i put on my " + paragraph[3] + " pyjamas while watching " + paragraph[6])
    print("I've probably done this like " + str(paragraph[8]) + " times, more or less")
    print("On an unrelated note ... I think i could beat " + paragraph[4] + " from " + paragraph[7] + " in a fight ...")
    print("That's if we're competing in " + paragraph[5] + " because honestly I'm pretty good at it")


# This is the rock paper scissors game
# The user is prompted to enter a correct letter, if it doesn't match R,P or S they have to reenter it
# The correct input is then compared to the rock paper rules with nested if else statements
# the corresponding outcomes are printed
def rockPaperScissors():
    print("Lets Play Rock Paper Scissors !!")
    while True:
        hand_sign = input("Choose R for rock, P for paper, S for scissors: ").upper().strip()
        if hand_sign == 'R' or hand_sign == 'P' or hand_sign == 'S':
            computer_value = random.randint(0, 2)
            if computer_value == 0:
                computer_sign = 'R'
            elif computer_value == 1:
                computer_sign = 'P'
            else:
                computer_sign = 'S'

            if computer_sign == 'R':
                if hand_sign == 'S':
                    print("you chose Scissors, the computer chose Rock")
                    print("The Computer wins !!!")
                elif hand_sign == 'P':
                    print("you chose Paper, the computer chose Rock")
                    print("You win !!!")
                else:
                    print("you chose Rock, the computer chose Rock")
                    print("Its a draw ..")
                break
            elif computer_sign == 'P':
                if hand_sign == 'S':
                    print("you chose Scissors, the computer chose Paper")
                    print("You win !!!")
                elif hand_sign == 'P':
                    print("you chose Paper, the computer chose Paper")
                    print("Its a draw ..")
                else:
                    print("you chose Rock, the computer chose Paper")
                    print("The Computer wins !!!")
                break
            elif computer_sign == 'S':
                if hand_sign == 'S':
                    print("you chose Scissors, the computer chose Scissors")
                    print("Its a draw ..")
                elif hand_sign == 'P':
                    print("you chose Paper, the computer chose Scissors")
                    print("The Computer wins !!!")
                else:
                    print("you chose Rock, the computer chose Scissors")
                    print("You win !!!")
                break
        else:
            print("Please enter a valid letter .")

# A function to print all list elements
def printGames(thelist):
    for element in thelist:
        print(element)

# the main function where all the games are chosen
# it contains the menu and an if else statement to select the games
def main():
    print(GAME_TITLE)
    print("Game menu:")
    print(LINE)
    games = ["1. Mad Libs", "2. The Guessing Game", "3. Rock Paper Scissors"]
    print("Welcome to " + GAME_TITLE + " please select a game you would like to play from the selection")
    printGames(games)
    while True:
        game = int(input("\nSelect the game you want to play using the number. Press 9 to exit : "))
        if game == 1:
            madLibs()
        elif game == 2:
            guessingGame()
        elif game == 3:
            rockPaperScissors()
        elif game == 9:
            break
    print("You have Exited the Game !! Hope you enjoyed yourself")

# executing the code
if __name__ == "__main__":
    main()