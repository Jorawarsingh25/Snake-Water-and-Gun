import random

def game():
    choices = ['Snake', 'Water', 'Gun']
    
    # Get user's choice
    user_choice = input("Enter your choice (Snake, Water, or Gun): ").capitalize()
    
    # Validate user's choice
    if user_choice not in choices:
        print("Invalid choice! Please enter either Snake, Water, or Gun.")
        return
    
    # Get computer's choice
    computer_choice = random.choice(choices)
    
    # Determine the outcome
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'Snake':
        if computer_choice == 'Water':
            print("You win! Snake drinks the water.")
        else:
            print("You lose! Gun kills the snake.")
    elif user_choice == 'Water':
        if computer_choice == 'Gun':
            print("You win! Water drowns the gun.")
        else:
            print("You lose! Snake drinks the water.")
    else:   #user_choice == 'Gun'
        if computer_choice == 'Snake':
            print("You win! Gun kills the snake.")
        else:
            print("You lose! Water drowns the gun.")

# Run the game
game()
