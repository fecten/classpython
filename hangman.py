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


#Play the game!
banner()