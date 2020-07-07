# Things that could be improved:
# Make the way the computer picks a choice smarter so that it wins more consistently 
# Allow more choices other than rock, paper, scissors
# Save the outcomes 
# Sanitize the user input: make it so that the program can handle inputs like "r" for rock
# Be smarter about comparing user and computer choices 
# Add some funny commentary from the computer 
# Add more game types 
# Win/loss percentage 
# Encapsulate the comparison logic in its own function to make the code easier to read 
​
# Planning 
# Write a program to play Rock Paper Scissors with a user 
# Let's flesh out the rules and think about how this is going  to work 
​
# Rules: Rock -> Scissors
    #    Scissors -> Paper
    #    Paper -> Rock 
​
import random
​
# Flow: 
# Start up program 
​
# Keep track of number of wins, losses, and ties for the user 
    # How do we do this? 
    # Have separate variables for each 
wins = 0
losses = 0
ties = 0
​
# takes as input both the player's and computer's choices 
# decides the outcome 
# what should this function return? 
# Returns 0 to indicate a tie, 1 to indicate the user won,
# and -1 to indicate the computer won 
def compare_choices(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 0
    # player wins 
    elif (player_choice == "rock" and computer_choice == "scissors") or \
        (player_choice == "scissors" and computer_choice == "paper") or \
        (player_choice == "paper" and computer_choice == "rock"):
        return 1
    # player loses
    else:
        return -1
​
possible_choices = ["rock", "paper", "scissors"]
​
# keep all of this going in an infinite loop until the user decies to quit
while True:
    # User will specify their choice, or can type "quit" in order to exit the program
​
    users_choice = input("Choose rock, paper, or scissors: ")
        # How does the program read the user's choice? 
        # Use Python's `input` function 
    
    if users_choice == "quit":
        print("See you next time!")
        break
    elif users_choice not in possible_choices:
        print("I don't understand that")
        # go on to the next iteration of the game loop 
        continue
    
    # Program also needs to specify its choice 
    programs_choice = random.choice(possible_choices)
    print(f"Program picked {programs_choice}")
        # How does the program determine its choice? 
        # Just have it randomly pick a choice
        # Use Python's `random.choice` function 
​
    # Once both choices are made, compare them via the rules to 
    # see who won 
        # How do we do the comparison? 
        # use if statements
​
    # Let's refactor this to make it more easily readable 
    result = compare_choices(users_choice, programs_choice)
​
    if result == 0:
        print("A tie!")
        ties += 1
    elif result == 1:
        print("You won!")
        wins += 1
    else:
        print("You lost!")
        losses += 1
​
    print(f"Wins: {wins}, ties: {ties}, losses: {losses}")