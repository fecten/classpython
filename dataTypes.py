#learning the basic data types
#I already know this stuff but I think it is worth having notes on it for the long run if you ever have a gap in knowledge having notes is a god send

#Strings
str="Hello"
typeStrVar=type(str)
print(f"{str} is a {typeStrVar}.")
#You can select specific characters from a string
#It looks like this H [0], e [1], l [2], l [3], o [4]
#So if you select the numbers below you get HooHoHoo
print(str[0]+str[4]+str[4]+str[0]+str[4]+str[0]+str[4]+str[4])


#Integers
int=3
typeIntVar=(type(int))
print(f"{int} is a {typeIntVar}.")

#Float
float=3.3333
typeFloatVar=(type(float))
print(f"{float} is a {typeFloatVar}.")

#boolean
#used in if else, while loops, for loops
t=True
f=False
typeBoolTVar=(type(t))
typeBoolFVar=(type(f))
print(f"{t} and {f} is a {typeBoolTVar} and {typeBoolFVar}.")

