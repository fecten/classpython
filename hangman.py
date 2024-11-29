#!/usr/bin/python3
#create greeting /
#create your word list /
#randomly choose a word from the list you have created /
#ask the user to guesss a letter 
#bonus make the program taek the input from the user and make it lower case
#check if the letter is in the word

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

#lengths of the lists
easyLen=len(easy_words)
mediumLen=len(medium_words)
hardLen=len(hard_words)

def banner():
    banner = pyfiglet.figlet_format("HANGMAN")
    print(banner)
    print("By: Adam Malick for The process of learning Cybersecurity and Ethical Hacking.")

# the random word should be stored in a variable and everytime they guess a letter it checks each letter in the word treating the word like a list iterating throug it
#if the letter dne then give a body part if it does exist then put the letter in printed out word with the letters they used and the other default information.

def getRandomWord(level):
    if level == 1:
        hangWord=(easy_words[random.randint(0, easyLen - 1 )])
    elif level == 2:
        hangWord=(medium_words[random.randint(0, mediumLen - 1 )])
    else:
        hangWord=(hard_words[random.randint(0, hardLen - 1 )])
    return hangWord

def wordSizeUnder(wordLength):
    for i in range (0,wordLength+1):
        print("_", end=" ")

def whichWordList():
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    lvl=input("Enter the number for the level of difficulty: ")

    if lvl.isalpha():
        print("String, that is invalid please type the number.")
        whichWordList()

    elif int(lvl) == 1:
        lenRandWord=len(getRandomWord(1))
        wordSizeUnder(lenRandWord)

    elif int(lvl) == 2:
        lenRandWord=len(getRandomWord(2))
        wordSizeUnder(lenRandWord)

    elif int(lvl) == 3:
        lenRandWord=len(getRandomWord(3))
        wordSizeUnder(lenRandWord)

    else:
        print("Try Again invalid input.")
        whichWordList()
    
    
#Start of the game printing the banner    
banner()
whichWordList()
