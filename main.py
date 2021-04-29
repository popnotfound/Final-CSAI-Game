#EscapeFromTarkovTextGame
import time

print("Welcome to Escape from Tarkov Text Edition!")
print(" ")
print("Enter the word instructions to read them, but if you don't \nneed them enter the word no.")

print(" ")
instructions = str(input(" "))

if instructions == "instructions":
  print(" ")
  print("You are a character trying to scavenge for materials, like \nguns, ammunition, and many more things to help you level up \nyour hideout, which is where you live and store all the things \nyou find.")
  print(" ")
  print("I will give you 30 seconds to read the instructions. ")
  time.sleep(30)
elif instructions == "no":
  print("Let's get into the game!")

