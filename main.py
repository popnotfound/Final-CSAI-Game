#EscapeFromTarkovTextGame

import time

print("Welcome to Escape from Tarkov Text Edition!")
print(" ")
print("Enter the word instructions to read them, but if you don't \nneed them enter the word no.")

print(" ")
instructions = str(input(" "))

if instructions == "instructions":
  print(" ")
  print("You are a character trying to scavenge for materials, like \nguns, ammunition, and many more things to help you level up \nyour hideout, which is where you live and store all the things \nyou find. To find these types of items, type directions or try and look in things and eventually you will find the extract to exit back to your hideout. ")
  print(" ")
  print("I will give you 1 minute to read the instructions. ")
  time.sleep(60)
  print(" ")
  print("Okay. Lets's get into the game!")
elif instructions == "no":
  print("Let's get into the game!")
