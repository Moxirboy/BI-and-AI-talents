import random

choices = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "Player wins!"
    else:
        return "Computer wins!"

while player_score < 5 and computer_score < 5:
    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    if player_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(player_choice, computer_choice)
    print(result)
    
    if result == "Player wins!":
        player_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    
    print(f"Player Score: {player_score} | Computer Score: {computer_score}")
    print("-" * 40)

if player_score == 5:
    print("Congratulations! You won the match!")
else:
    print("Computer won the match! Better luck next time!")
