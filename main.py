#EscapeFromTarkovTextGame

import time

def help():
  playerhelp = input("Enter 'help' for help, and enter 'start' to immediately start. ")
  if playerhelp == "help":
    print("Welcome to Escape from Tarkov Text Edition!")
    print(" ")
    print("You are a character trying to scavenge for materials, like \nguns, ammunition, and many more things to help you level up \nyour hideout, which is where you live and store all the things \nyou find. To find these types of items, type directions or try and look in things and eventually you will find the extract to exit back to your hideout. ")
    print("You may also only use lowercase words and there are no spaces. All you have to do is 'y' for yes, and 'n' for no.")
    print(" ")
    print("I will give you 1:30 minutes to read the instructions. ")
    time.sleep(90)
    print(" ")
    print("Okay. Lets's get into the game!")
  elif playerhelp == "start":
    start()

def start():
  print("You are in a map called Customs and are in the POI, Dorms. ")
  print("")
  print("You have a knife that can be used to kill any enemies around you. ")
  print("")
  print("You can go inside one huge dorm building or you can extract immediately with the knife and keep safe however the extract is guarded by Scavs, or also known as enemies. ")
  print("")
  enterdorms = input("Do you want to enter the huge dorms building? ")

  if enterdorms == "y":
    print("You enter the dorms building and there are many different rooms. It is a one story building with 4 different rooms labeled Dorm 001, Dorm 002, Dorm 003, and Dorm 004. There are also random pieces of furniture you can look through to find keys to open these different dorm rooms. ")
  elif enterdorms == "n":
    print("You go towards the extract/exit and there are two enemies guarding it. You want to sneak around trees, kill one, and leave or risk trying to kill both of them.")
    print("")
    extracting = input("Do you want to 'sneak and kill one' or 'kill both'?")

