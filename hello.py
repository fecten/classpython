#This is the print statement.
#Inside of it is a string.
print("Hello, World this is my first program")

#Using \n to create a new line.
 
print("Kind regards,\nAdam Malick")

#Using + in a print statement to connect 2 different strings
#Note you have to have a space before or after one of the names
#Or you can add a space in between another set of plus
#String concatination

print("Adam"+" Malick")

#We get the same result 
print("Adam"+" "+"Malick")

#Below is the same as above byt using variables which when doing repetitive tasks becomes valuable
str1="Adam"
str2="Malick"
space=" "
print(str1 + space + str2)

#We can instead of making a whole variable to print a space we can use an f string which formats number and strings with space and variables
#Have to use the {} for variables
print(f"{str1} {str2}")

#Getting user input
#Setting the user input for ip to the variable ip
#ip=input("Input the target ip: ")
#print("Scanning the target... "+ip)

#Different way of doing it 
#print( "Targeting IP " + input("Input the target ip: "))

#Using variables and printing out the values
x=5
y=7
sum=x+y
print(x+y)
print(sum)
print(f"{x} + {y} = {sum}")

#You can change the value of 5 into a string to get the number 57
print(str(x)+ str(y))

#You can also make strings into ints
z="123"
sumOfZandY=int(z)+y
print(f"{z} + {y} = {sumOfZandY}")

#Have to specify int for user input as user input is read as a string 
num1=int(input("Input num1: "))
num2=int(input("Input num2: "))
sumNum=num1+num2
print(f"{num1}+{num2}={sumNum}")



