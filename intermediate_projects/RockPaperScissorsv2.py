from random import randint

player_BO3_score = 0
computer_BO3_score = 0
computer_possible_choices = ["Rock", "Paper", "Scissors"]
computer_choice = (computer_possible_choices[randint(0, 2)])
# Run game until one player reaches 3 points

while computer_BO3_score < 3 and player_BO3_score < 3:
# Have computer make a random roll from the array of options
    computer_choice = (computer_possible_choices[randint(0, 2)])
# Have Player select RP or S
    player_choice = input("Choose one: Rock, Paper, or Scissors: ")
    print("You guessed: " + str(player_choice))
    print("Computer guessed: " + str(computer_choice))
# Compare choices from player and computer and add scores to BO3 total
    
# Reset the computers choice
    computer_choice = (computer_possible_choices[randint(0, 2)])


# Show BO3 winner
if player_BO3_score == 3:
    print("Oh damn, you won the game!  Aint dat some shit.")
else:
    print("You lost the game?  Try again like your momma taught you right.")
