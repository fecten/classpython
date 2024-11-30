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
        attempts=10
    elif level == 2:
        word = random.choice(medium_words)
        medium_words.remove(word)
        attempts=8
    elif level == 3:
        word = random.choice(hard_words)
        hard_words.remove(word)
        attempts=5 
    else:
        return None

    return word,attempts

def getLevel():
    print("1.Easy \n2.Medium \n3.Hard")
    while True:
        level=input("Enter the number for the level difficulty you want: ")
        if level.isdigit() and 1<= int(level) <= 3:
            return level
        else:
            print("Invalid input. Try Again. 1 | 2 | 3")

def initDisplayWord(word):
    return ["_" for _ in word]

def updateDisplayWord(guess,word,displayWord,guessedLetters):
    if guess in guessedLetters:
        print(f"You've already guessed '{guess}'. Try again. ")
        return displayWord, guessedLetters #no change
    
    #appends if not in guessed letters because gets caught by init if cond updates guessed letters with the new guess
    guessedLetters.append(guess)

    #this updates the display word
    for i in range(len(word)):
        if word[i] == guess:
            displayWord[i]=guess

    return displayWord, guessedLetters

def getContinue():
    while True:
        # Ask the user if they want to continue playing
        continue_game = input("Do you want to play again? (yes/no): ").lower()
        if continueGame == 'yes':
            gameLoop()
        elif continueGame == 'no':
            print("Thanks for playing! Goodbye.")
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")


def gameLoop():
    #get the level 
    level=getLevel()
    #get the random word from the list and the number of attempts
    getWordResult=getRandomWord(int(level))
    #seperate the results from last function
    word=getWordResult[0]
    attempts=getWordResult[1]

    displayWord=initDisplayWord(word)
    guessedLetters = []
    

    while attempts > 0:
        print(" ".join(displayWord)) #print init state
        guess = input("Guess a letter: ").lower()
        
        displayWord, guessedLetters = updateDisplayWord(guess, word, displayWord, guessedLetters)
        print(guess)

        if guess not in word:
            attempts -= 1
            print(f"Incorrect. You have {attempts} attempts remaining.")
        
        if "_" not in displayWord:
            print(f"Congratulations! You've guessed the word: {word}")
            break
    
    if attempts == 0:
        print(f"Game Over! The word was : {word}") 
    
    getContinue()

#main game running functions
banner()
gameLoop()