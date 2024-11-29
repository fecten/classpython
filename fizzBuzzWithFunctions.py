#!/usr/bin/python3
#https://docs.python.org/3/library/functions.html
#The link provided above can be used to look through some of the Built-in functions in python

#defines the variables 
fizz="fizz"
buzz="buzz"

#Define function
def fizzBuzzFunction(num1,num2,userRange):
    for i in range(0,userRange):
        if i % num1 == 0 and i % num2 == 0:
            print(fizz+buzz)
        elif i % num1 == 0:
            print(fizz)
        elif i % num2 == 0:
            print(buzz)
        else:
            print(i)

#The order you parse your parameters matters if it is incorrect it will just put that number in and it could be wrong 
fNum=int(input("What is the first number for fizzbuzzFunction: "))
sNum=int(input("What is the second number for fizzBuzzFunction: "))
rangeNum=int(input("How many numbers do you want to test against fizzBuzzFunction: "))

#this function is putting in the user inputs from fNum, sNum and the range of the numbers. 
fizzBuzzFunction(fNum,sNum,rangeNum)

#Problem #2
#create a fucntion that can take in an input of the users name 
#save the name in a variable
#pass the variable throught he function and print "hello [name]"

def helloFunction(fName):
    print(f"Hello {fName}")

name=input("What is your first name: ")
helloFunction(name)


#Proble #3
#Lets ask for an ip address
#then define the function

def nmapScan(ip):
    print(f"nmap -sV {ip}")

ip=input("What is the Target IP Address: ")
nmapScan(ip)

#super basics of functions but it is important to understand how they work because if you do not understand then it will be hard to use for automation of scans
#important to understand that sometimes certain scans will not work, and since they are in functions you can just ctrl-c and it will stop