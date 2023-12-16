from random import randint  # this code line is how our computer will play

#create a list of playable options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]  #(0,2) is the index of the playable options

#set player to false
player = False

while player == False:
    #set player to true
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling Sherlock!")

#player was set to true, but we want it to be false so the loop continues
player = False
computer = t[randint(0,2)]