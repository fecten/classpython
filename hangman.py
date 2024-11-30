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
    displayWord=["_" for _ in word]
    return displayWord

def updateDisplayWord(guess,word,displayWord):
    
    #we have to update the new word with "_" but when the letter guessed is correct put the new letter in the word and print that word with the underscores for letters not guessed 
    for letter in word:
        if letter == guess:
            displayWord.append(letter)
        else:
            displayWord.append("_")


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
        
        print(guess)

        print(attempts)

banner()
gameLoop()