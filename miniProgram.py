#!/usr/bin/python3
#Greet User ask for user input if y continue if n exit 

x=1

while x >= 1:
    #One day will make this cool cli tool where it has a sick banner like metasploit
    #super in effecient but thats okay
    print("Weclome to Python Basics")
    print("************************")

    userConfirm=input("Enter y/Y to continue n/N to exit: ")
    if userConfirm.upper() =="Y":
        #will ask user to input 2 numbers and it will tell you which number is greater than the other.
        userNum1=int(input("Enter a number: "))
        userNum2=int(input("Enter a number for comparing:"))

        if userNum1 > userNum2:
            print(f"{userNum1} is greater then {userNum2}.")
        
        elif userNum1 < userNum2:
            print(f"{userNum2} is greater than {userNum1}")
            
        
        else:
            print("The numbers are equal to eachother!")
            
    
    elif userConfirm.upper() == "N":
        x=0
    else:
        print("That was a bad input try again. ")


#By adding the .upper() to the end of the input variable we always get a uppercase variable so when comparing or checking if Y or N it will always compare to Y or N 
#You can also do .lower() which will make it lowercase
print(userConfirm.upper())


