# String Slicing

# abc = "Hello World"
# print(abc[0]) #First Index
# print(abc[1]) # Second Index
# print(abc[-1]) # Last Index

# print(abc[0]+abc[-1]) # String Concatenation


# userInput =  input("Enter a number: ") #Ask for user input
# print("You Entered "+userInput)


# Ask for input from user and print its first, second 
# and second last and last character

# userInput =  input("Enter Something: ") #Ask for user input
# print(userInput[0]+userInput[1]+userInput[-2]+userInput[-1])


# text = "asndasklnkasncskacnascnascnsacoiascijsa "
# print(text[0:-1:2])
# print(text)


#1) Write a Python program to calculate the length of a string.
# print(len(text))

# 3) Write a Python program to change a given string to a new string
#  where the first and last chars have been exchanged

# user = input('Enter Something')
# first = user[0]
# last = user[-1]

# print(last+user[1:-1]+first)


# print(str[-1:-4:-1])


# 4) Write a Python script that takes input from the 
# user and displays that input back in
# upper and lower cases.
# str = input("Enter Something: ")
# print(str.upper())
# print(str.lower())



#5) Write a Python program to check whether a 
# string starts with specified character

# specifiedCharacter = "a"
# userInput = input("Enter Something: ")
# print(userInput[0]==specifiedCharacter)

# if(userInput[0]==specifiedCharacter):
#     print("True")
# else:
#     print("False")



# 6) Write a program to reverse a string
inp = input("Enter Something")
# print(inp[-1:0:-1]+inp[0])
# print(inp[-1::-1])
print(inp[::-1])
