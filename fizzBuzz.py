#!/usr/bin/python3
#FizzBuzz

#If a number is divisible by 3, print fizz
#If a number is divisible by 5, print buzz
#If a number is divisible by both print fizzbuzz

#Loop through the numbers 1-100
fizz="fizz"
buzz="buzz"

for i in range(0,100):
    if i % 3 == 0 and i % 5 == 0:
        print(fizz+buzz)
    elif i % 3 == 0:
        print(fizz)
    elif i % 5 == 0:
        print(buzz)
    else:
        print(i)