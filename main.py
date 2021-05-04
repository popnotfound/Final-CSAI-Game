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

print('\n'*25)
while True: 
  playerhealth = 100
  playerstamina = 100
  
  print("You are in the map, Customs, and you spawn at dorms. Type \nanything to move towards completing the game.")
  print(" ")
  firstplayeraction = input()
  inventory = ['knife']
  outwhileloop = False


  while outwhileloop == False:
    if firstplayeraction.lower() == "north":
      print("You have moved towards some factory shacks and a bus. Since you ran to this direction, you lost 5 stamina")
      playerstamina = playerstamina - 5
      outwhileloop = True
    elif firstplayeraction.lower() == "east":
      print("You are moving through the forest and come to a dead end. Since you ran to this direction, you lost 5 stamina ")
      print(" ")
    elif firstplayeraction.lower() == "south":
      print("You go south and come across a dead end. There is nothing here. Since you ran to this direction, you lost 5 stamina ")
      print(" ")
    elif firstplayeraction.lower() == "west":
      print("You come across a dead end. Except you find a campfire. Since you ran to this direction, you lost 5 stamina")
      print(" ")
      outwhileloop = True
    elif firstplayeraction.lower() == "show inventory":
      print(inventory)