number = int(input("Enter a number: "))#user input and stored the same in variable number
y = number % 2 #check the remainder and stores in variable y
if y == 0:
    print(f"{number} is an even number")
elif y == 1:
    print(f"{number} is an odd number")

