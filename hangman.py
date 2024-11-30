#!/usr/bin/python3

import pyfiglet
import random

easy_words = [
    "cat", "dog", "sun", "hat", "car",
    "apple", "book", "duck", "fish", "star",
    "tree", "cloud", "grass", "bird", "house",
    "chair", "table", "milk", "shoe", "clock"
]

medium_words = [
    "garden", "market", "bottle", "window", "pencil",
    "bridge", "orange", "basket", "travel", "winter",
    "silver", "tunnel", "rocket", "forest", "pirate",
    "dragon", "helmet", "jungle", "island", "wallet"
]

hard_words = [
    "labyrinth", "quarantine", "melancholy", "meticulous", "conundrum",
    "ephemeral", "paradoxical", "abundance", "inception", "serendipity",
    "enigmatic", "hypothesis", "eloquence", "perseverance", "benevolent",
    "phenomenon", "prestigious", "unorthodox", "exuberance", "grandiloquent"
]


def banner():
    banner = pyfiglet.figlet_format("HANGMAN")
    print(banner)
    print("By: Adam Malick for The process of learning Cybersecurity and Ethical Hacking.")

def getRandomWord(level):
    if level == 1:
        word = random.choice(easy_words)
        easy_words.remove(word)
        return word
    elif level == 2:
        word = random.choice(medium_words)
        medium_words.remove(word)
        return word
    elif level == 3:
        word = random.choice(hard_words)
        hard_words.remove(word)
        return word
    else:
        return None
 
#if its not in guessed letters it prints _ and use .join to join the list of displayed letters
def displayWord(word, guessedLetters):
    displayed = [
        letter if letter in guessedLetters else "_" 
        for letter in word
    ]
    return " ".join(displayed)

#Start of the game printing the banner
def playGame():
    # Difficulty selection
    print("Select a difficulty level:")
    print("1. Easy\n2. Medium\n3. Hard")
    #try level take user input
    #if level is in the list 1,2,3 the break its good
    #else invalid 
    #try |except valueError invalid input try again and since in loop 
    #it only breaks out of the loop if its in the 1,2,3 rather than having to do 17 million if conditions
    while True:
        try:
            level = int(input("Enter the number for the level of difficulty: "))
            if level in [1, 2, 3]:
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Select the random word and initialize game state
    word = getRandomWord(level)

#set function is  a built in function
#gotta learn
    guessedLetters = set()
    attemptsLeft = 5

    print("\nLet's start the game!")
    print(f"The word has {len(word)} letters.")
    
    # Game loop
    while attemptsLeft > 0:
        print("\n" + displayWord(word, guessedLetters))
        print(f"Guessed letters: {' '.join(sorted(guessedLetters))}")
        print(f"Attempts left: {attemptsLeft}")

        # Get user's guess
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessedLetters:
            print("You already guessed that letter. Try again.")
            continue

        guessedLetters.add(guess)

        # Check if the guess is correct
        if guess in word:
            print("Good guess!")
            # Check if the player has guessed the whole word
            if all(letter in guessedLetters for letter in word):
                print(f"\nCongratulations! You guessed the word: {word}")
                break
        else:
            print("Wrong guess.")
            attemptsLeft -= 1

    # If out of attempts, reveal the word
    if attemptsLeft == 0:
        print(f"\nGame over! The word was: {word}")

def mainGame():
    banner()
    while True:
        playGame()
        # Ask if the player wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("\nThanks for playing! Goodbye!")
            break


#Play the game!
mainGame()