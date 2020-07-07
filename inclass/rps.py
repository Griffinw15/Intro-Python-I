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
​
    # Program also needs to specify its choice 
    possible_choices = ["rock", "paper", "scissors"]
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
    if users_choice == "rock":
        if programs_choice == "rock":
            print("A tie!")
            ties += 1
        elif programs_choice == "paper":
            print("Program won!")
            losses += 1
        else:
            print("You won!")
            wins += 1
    elif users_choice == "paper":
        if programs_choice == "rock":
            print("You won!")
            wins += 1
        elif programs_choice == "paper":
            print("A tie!")
            ties += 1
        else:
            print("Program won!")
            losses += 1
    elif users_choice == "scissors":
        if programs_choice == "rock":
            print("Program won!")
            losses += 1
        elif programs_choice == "paper":
            print("You won!")
            wins += 1
        else:
            print("A tie!")
            ties += 1
    else:
        print("I don't understand that")
        # go on to the next iteration of the game loop 
        continue
​
    print(f"Wins: {wins}, ties: {ties}, losses: {losses}")