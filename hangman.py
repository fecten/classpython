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


def getRandomWord(level):
    if level == 1:
        print(easy_words[random.randint(0, easyLen - 1 )])
    elif level == 2:
        print(medium_words[random.randint(0, mediumLen - 1 )])
    else:
        print(hard_words[random.randint(0, hardLen - 1 )])


def whichWordList():
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    lvl=input("Enter the number for the level of difficulty: ")

    if lvl.isalpha():
        print("String, that is invalid please type the number.")
        whichWordList()

    elif int(lvl) == 1:
        getRandomWord(1)
    
    elif int(lvl) == 2:
        getRandomWord(2)

    elif int(lvl) == 3:
        getRandomWord(3)

    else:
        print("Try Again invalid input.")
        whichWordList()

    
    
#Start of the game printing the banner    
banner()
whichWordList()
