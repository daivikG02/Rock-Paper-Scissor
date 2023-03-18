from random import randint
import time

a=["rock", "paper", "scissor"]

computer =a[randint(0,2)]

player =False

while player == False:
  player = input("rock,paper,scissor ?")

if player == computer: 
  print("Computer selected -", computer)
  print("It is a tie. No one wins.")
elif player == "rock":
  if computer == "paper":
    print("Computer selected -", computer)
    time.sleep(3)
    print("You lose. Paper has covered the rock. Computer wins")
  else:
    print("Computer selected -", computer)
    time.sleep(3)
    print("You win. As the rock will smash the scissor.")

elif player == "paper":
  if computer == "rock":
    print("Computer selected -", computer)
    time.sleep(3)
    print("You win. Paper has covered the rock. Player wins")
  else:
    print("Computer selected -", computer)
    time.sleep(3)
    print("You lose. As the scissor will cut the paper.")

elif player == "scissor":
  if computer == "paper":
    print("Computer selected -", computer)
    time.sleep(3)
    print("You win. AS the scissor will cut the paper.")
  else:
    print("Computer selected -", computer)
    time.sleep(3)
    print("You lose. As the rock will smash the scissor.")
    