#Weakest Link Program
#will have to aggregate total points each round manually

# Initialize variables
chain = 0
points = 0
banked = False
total_questions = 0
max_chain=0
banked_points=0

# Define points dictionary
points_dict = {1: 20, 2: 50, 3: 100, 4: 200, 5: 300, 6: 450, 7: 600, 8: 800, 9: 1000}

# Loop until the user enters "stop"
while True:
    # Get the contestant's answer
    answer = input(f" If answer is correct, type 'C' \n If answer is incorrect, type 'W' \n If the player banks, type 'bank'\n If round is over, type 'stop' \n ")
    
    if banked_points>=1000:
            print(f"\nBanked Points reached the maximum!")
            break #if we want to stop at the max. else remove this 
    
    # Check if round is over
    if answer.lower() == "stop":
        print("\n\n")
        print("Thanks for playing!\n")
        print(f"Current Chain:{chain} \nTotal Points:{1000 if banked_points > 1000 else banked_points} \nTotal Questions:{total_questions}")
        break

    # Check if the answer is correct
    if answer.lower() == "c":

        # Increment the chain and add points to the jackpot
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
            break

        # Reset the banked variable
        banked = False

    elif answer.lower() == "bank":
        if chain > 0:
            # Save the banked points, and reset the chain and points
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
        
print(f"Max chain: {max_chain}")