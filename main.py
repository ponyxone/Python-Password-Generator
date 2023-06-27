import os
import random

lowcaseLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercaseLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
symbols = ['!', '"', '£', '$', '%', '&', '/', '(', ')', '=', 'à', 'è', 'ì', 'ò', 'ù', '@', '#', '[', ']', '^', '{', ']', '?', '*', '-', '_', '.', ' ', 'é', '\\', '|', ':', ',', ';']

passLengthStr = input("Password length:")
passLength = int(passLengthStr)
password = ""

for _ in range(passLength):
    charType = random.randint(0, 3)
    if charType == 0:
        password += random.choice(lowcaseLetters)
    elif charType == 1:
        password += random.choice(uppercaseLetters)
    elif charType == 2:
        password += random.choice(numbers)
    elif charType == 3:
        password += random.choice(symbols)

print(password)


savePass = input("Save this password in a file? Y/N\n")
if savePass == "y" or savePass == "Y":
    name=input("File name:")
    f = open(str(name)+".txt", "x")
    f.write(password)
    f.close()