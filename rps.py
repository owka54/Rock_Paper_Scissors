from random import randint

# Display an initial message.
print("""

-------------------------
| Rock, Paper, Scissors |
-------------------------
""")

# Get input of total games they want to play. Keeps asking until a valid input is received.
def total_games():
    while True:
        try:
            games = int(input("How many games would you like to play? (1, 3, 5, 7) - "))
        # If the input is invalid, asks for another.
        except ValueError:
            print("Please select either 1, 3, 5 or 7 games...")
            continue
        # Check if input is in the list of available total games.
        if games in (1, 3, 5, 7):
            break
        else:
            continue
    return games

# Ask the player for their move.
def players_turn():
    move = ""
    ask = input("Select your move ('rock' or 'r', OR 'paper' or 'p', OR 'scissors' or 's' - ")
    if ask.lower() == "rock" or ask.lower() == "r":
        move = "Rock"
    elif ask.lower() == "paper" or ask.lower() == "p":
        move = "Paper"
    elif ask.lower() == "scissors" or ask.lower() == "s":
        move = "Scissors"
    # If input isn't valid, ask for another.
    else:
        print("Not a valid move...")
        players_turn()
    return move

# Get the computer's move.
def comps_turn():
    # Get random number between 1 and 3.
    num = randint(1, 3)
    if num == 1:
        move = "Rock"
    elif num == 2:
        move = "Paper"
    elif num == 3:
        move = "Scissors"
    return move

# Check the player's move and the computer's move to see who wins or if it's a draw.
def who_wins(player, comp):
    if player == comp:
        return "draw"

    elif player == "Rock" and comp == "Paper":
        return "comp"
    elif player == "Rock" and comp == "Scissors":
        return "player"

    elif player == "Paper" and comp == "Scissors":
        return "comp"
    elif player == "Paper" and comp == "Rock":
        return "player"
    
    elif player == "Scissors" and comp == "Rock":
        return "comp"
    elif player == "Scissors" and comp == "Paper":
        return "player"

# Ask if the player wants to play again.
def play_again():
    again = input("Do you want to play again? ('yes' or 'y', OR 'no' or 'n') - ")
    if again.lower() == "yes" or again.lower() == "y":
        return True
    elif again.lower() == "no" or again.lower() == "n":
        print("""

**************************************
                                      
Thanks for playing! Hope you had fun 
                                      
**************************************
        """)


# Start the game.
def rps_game():
    games = total_games()
    game_count = 1
    # Win counters.
    player_count = 0
    comp_count = 0

    while game_count <= games:
        player = players_turn()
        comp = comps_turn()

        # Print what move the player and the computer selected.
        print("\nPlayer selected: " + player + "\n")
        print("Computer selected: " + comp + "\n")

        # Determine who wins the round.
        winner = who_wins(player, comp)
        if winner == "comp":
            print("> Comp wins this round! <" + "\n")
            comp_count += 1
        elif winner == "player":
            print("> Player wins this round! <" + "\n")
            player_count += 1
        else:
            print("> It's a draw. Play again. <" + "\n")
            continue

        game_count += 1

    # Print final scores.
    print("The scores are: Player - " + str(player_count) + " | Comp - " + str(comp_count) + "\n")

    # Print who won.
    if player_count > comp_count:
        print("*** Player wins! :) ***")
    else:
        print("*** Computer wins :( ***")

    another = play_again()
    while another == True:
        rps_game()
        another = False


rps_game()