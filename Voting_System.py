# Define the candidates and initialize the vote count
candidates = {"Salman Khan": 0, "Abhishek": 0, "Aishwarya": 0}

# Function to cast a vote
def cast_vote():
    print("Candidates: ")
    for candidate in candidates:
        print(candidate)
    vote = input("Enter the name of the candidate you want to vote for: ")
    
    if vote in candidates:
        candidates[vote] += 1
        print(f"Your vote for {vote} has been recorded.")
    else:
        print("Invalid candidate. Please try again.")
    
# Function to display the vote counts
def display_results():
    print("\nVoting Results:")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {votes} votes")

# Function to announce the winner
def announce_winner():
    winner = max(candidates, key=candidates.get)
    print(f"\nThe winner is {winner} with {candidates[winner]} votes!")

# Main program
if __name__ == "__main__":
    print("Welcome to the Simple Voting System!")
    
    while True:
        print("\n1. Cast Vote")
        print("\n2. Display Results")
        print("\n3. Announce Winner")
        print("\n4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "1":
            cast_vote()
        elif choice == "2":
            display_results()
        elif choice == "3":
            announce_winner()
            break
        elif choice == "4":
            print("Exiting the voting system.")
            break
        else:
            print("Invalid choice. Please try again.")
