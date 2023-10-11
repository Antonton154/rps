import random
from time import sleep

#Check if the move is valid
def playerChoice():
   try: 
      choice = ["Rock", "Paper", "Scissors"].index(input("Please choose your move (Rock, Paper, or Scissors): ")) 
   except:
      print("You have chosen an invalid move! Please try again.")
      playerChoice()
   else: 
      return choice
   return 0

def Game(move):
   #The result of the game based on player and computer choices
   results = [["Tied","Won", "Lost"],
             ["Lost", "Tied", "Won"],
             ["Won", "Lost", "Tied"]] 
   opponent = random.randint(0,2) #computer's choice randomly selected
   sleep(1)
   print("The opponent chose: " + ["Rock", "Paper", "Scissors"][opponent]) #Notify computer's choice
   sleep(1)
   print(f"You have {results[opponent][move]}!") #Notify the result of the match
   sleep(1)
   #Rematch
   replay = 0
   #Check if the user's input is appropriate
   while replay != "Yes" and replay != "No":
      replay = input("Do you want a rematch? (Yes/No): ")
   if replay == "Yes":
      player = playerChoice()
      Game(player)
   else:
      print("Thanks for playing!!!")
      return 0


#Instructions
print("Welcome to the 'Rock Paper Scissors' tournament!")
sleep(1)
print("You will choose between Rock, Paper, and Scissors.")
sleep(1)
print("Rock beats Scissors, Scissors beat Paper, and Paper beats Rock.")
sleep(1)
print("Lets play!")
sleep(1)

#Get the player's fist input
playerMove = playerChoice()
Game(playerMove)