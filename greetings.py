#!/usr/bin/python3
"""
These are comments and are really important and should be used as much as possible
multiple line comments.
This is the super basics no if conditions nothing just the most basic of basic can be.

"""
#import random lib to make random number
import random

name = "Adam"
age = 22
pi = 3.14
num_list = [1, 2, 3, 4, 5]
team_color = {'blue': 'defensive' , 'red' : 'offensive', 'purple' : 'collaborative'}

print(name)
print(age)
print(pi)

print(num_list[0])
print(num_list[1])
print(num_list[2])
print(num_list[3])
print(num_list[4])

for number in num_list:
    print(number)

print(team_color['blue'])
print(team_color['red'])
print(team_color['purple'])


random_num = random.randint(1,10)
print("Random number:" , random_num)

random.shuffle(num_list)
print("Shuffled list:", num_list)

