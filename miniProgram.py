#Greet User ask for user input if y continue if n exit 
x=1

while x >= 1:
    userConfirm=input("Enter y/Y to continue n/N to exit: ")
    if userConfirm.upper() =="Y":
        print("Super basic while loop which checks user input y and n!")
    
    elif userConfirm.upper() == "N":
        x=0
    else:
        print("That was a bad input try again. ")


#By adding the .upper() to the end of the input variable we always get a uppercase variable so when comparing or checking if Y or N it will always compare to Y or N 
#You can also do .lower() which will make it lowercase
print(userConfirm.upper())
