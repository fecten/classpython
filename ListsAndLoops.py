fruitList=["Appple","Pear","Guava","Pomegranate"]

for i in fruitList:
    print(i)

#In range starts at 0 and stops before ever hitting the final number, so if you want to hit 100 and your counting by 2 then you have to put in 102
for num in range (0,102,2):
    print(num)

div = 0
notDiv = 0
#range of all the numbers divis by 3 from 1-100 using an if cond
for three in range(0,100):
    if three%3 == 0:
        print(f"The number {three} is divisible by 3")
        div+=1

    else:
        print(f"The number {three} is not Divisible by 3.")
        notDiv+=1


print (f"There is {div} numbers divisible by 3, and {notDiv} number not divisible by 3")