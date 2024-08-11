import random

def play_game():
  
    user_score = 0
    computer_score = 0
    user_turn_to_win = True  

    while True:
    
        user_choice = input("Choose rock, paper, or scissors: ").lower()

     
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            continue

      
        choices = ['rock', 'paper', 'scissors']
        if user_turn_to_win:
           
            if user_choice == 'rock':
                computer_choice = 'scissors'
            elif user_choice == 'paper':
                computer_choice = 'rock'
            elif user_choice == 'scissors':
                computer_choice = 'paper'
            result = "You win!"
            user_score += 1
        else:
          
            if user_choice == 'rock':
                computer_choice = 'paper'
            elif user_choice == 'paper':
                computer_choice = 'scissors'
            elif user_choice == 'scissors':
                computer_choice = 'rock'
            result = "You lose!"
            computer_score += 1

        user_turn_to_win = not user_turn_to_win

        
        print(f"Computer chose: {computer_choice}")
        print(f"{result} (User: {user_choice}, Computer: {computer_choice})")
        print(f"Score -> You: {user_score}, Computer: {computer_score}")

        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("The game has ended. Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
