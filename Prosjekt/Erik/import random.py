import random

def coin_flip():
    # Generate a random number (0 or 1) to represent heads or tails
    result = random.randint(0, 1)
    
    # Return the result
    return result

def main():
    print("Welcome to the Coin Flip Game!")
    
    while True:
        input("Press Enter to flip the coin...")
        
        # Call the coin_flip function to get the result
        result = coin_flip()
        
        # Display the result
        if result == 0:
            print("Heads!")
        else:
            print("Tails!")
        
        # Ask the player if they want to play again
        play_again = input("Do you want to flip again? (yes/no): ").lower()
        
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break
