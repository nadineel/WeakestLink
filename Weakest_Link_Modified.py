#Weakest Link Modified Program
# takes into account the strongest and weakest link  [have to remove players every round]
#will have to aggregate total banked points each round manually

# Initialize variables
chain = 0
points = 0
banked = False
total_questions = 0
max_chain=0
banked_points=0
player_index = 0
players = ['Player 1','Player 2'] #in a circular order, insert more players 
player_stats = [{'name': player, 'correct': 0, 'incorrect': 0, 'banked': 0} for player in players]


# Define points dictionary
points_dict = {1: 20, 2: 50, 3: 100, 4: 200, 5: 300, 6: 450, 7: 600, 8: 800, 9: 1000}

# Loop until the user enters "stop"
while True:
    # Get the current player
    current_player = player_stats[player_index]

    # Get the contestant's answer
    answer = input(f" {current_player['name']}: \nIf correct, type 'C' \n If incorrect, type 'W' \n If the player banks, type 'bank'\n If round is over, type 'stop' \n ")
    
    if banked_points>=1000:
        print(f"\nBanked Points reached the maximum!")
        for player in player_stats:
            score = player
            print(f"{score['name']}: {score['correct']} correct answers, {score['incorrect']} incorrect answers, {score['banked']} points banked")
        break  # if we want to stop at the max. else remove this
    
    # Check if round is over
    if answer.lower() == "stop":
        print("\n\n")
        print("Thanks for playing!\n")
        print(f"Current Chain:{chain} \nTotal Points:{banked_points} \nTotal Questions:{total_questions}")

        for player in player_stats:
            score = player
            print(f"{score['name']}: {score['correct']} correct answers, {score['incorrect']} incorrect answers, {score['banked']} points banked")
        break

    # Check if the answer is correct
    if answer.lower() == "c":
        current_player['correct']+=1
        # Increment the chain
        chain += 1
        points = points_dict[chain]
        total_questions += 1
        print(f"Chain: {chain}, Points: {points}")

        # Update max_chain if applicable
        if chain > max_chain:
            max_chain = chain
        
        # Check if the chain is at 9 (the end of the round)
        if chain == 9:
            points = points_dict[chain]
            
            # Print the score and break out of the loop
            print(f"Congratulations! Your final score is {points} with {total_questions} consecutive questions answered correctly.")
            for player in player_stats:
                score = player
            print(f"\n{score['name']}: {score['correct']} correct answers, {score['incorrect']} incorrect answers, {score['banked']} points banked")
        
            break

        # Reset the banked variable
        banked = False


    elif answer.lower() == "bank":
        player_index-=1     #shady thing going on
        if chain > 0:
            # Save the banked points, and reset the chain and points
            current_player['banked']+=points
            banked_points += points
            print(f"Points banked: {points} Total banked points:{banked_points}")
            chain = 0
            points = 0
            banked = True
            
            
        else:
            print("You can't bank 0 points!")
            continue

    # If the answer is wrong, reset the chain and points if there are no banked points
    else:
        total_questions+=1
        current_player['incorrect']+=1
        if banked:
            # Save the banked points and reset the chain and points
            chain = 0
            points = 0
            banked = False
            print(f"Incorrect! Points banked: {banked_points}")
        else:
            # Reset the chain and points if the answer is incorrect and there are no banked points
            chain = 0
            points = 0
            print("Incorrect!")
        print(f"Chain: {chain}, Points: {points}")
        

    # Update the max_chain variable if the current chain is higher than the previous max_chain
    if chain > max_chain:
        max_chain = chain

    player_index+=1 
    player_index= player_index % len(players)

        
print(f"Max chain: {max_chain}")