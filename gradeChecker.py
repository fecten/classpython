#!/usr/bin/python3

#adding a bit of sohistication to the program, by making it a for loop iterating through the list of grades and outputing it on the terminal
#note you can also get your output to go into a .txt file as well.
#not sure if i can get it to go into a .xslx file 
#prompt user to enter their score from 0 - 100 and display their grade 
#90 - 100 = A
#80 to 89 = B 
#70 to 79 = C
#60 to 69 = D
#less than 60 but not = to 60 = F

grades=[100000,75,45,90,69,99,77,22,60,59,66,73,88,89,100,-22,-99999999999999999999999999999999999999999999999999]
#for loop iterating through grades list
for i in grades:
    if i >= 90 and i <= 100:
        print(f"{i} = A")
    
    elif i >= 80 and i <= 89:
        print(f"{i} = B")
    
    elif i >= 70 and i <= 79:
        print(f"{i} = C")
    
    elif i >= 60 and i <= 69:
        print(f"{i} = D")

    elif i < 60 and i >= 0:
        print (f"{i} = F")
    
    else:
        print(f"BAD input. {i}")
