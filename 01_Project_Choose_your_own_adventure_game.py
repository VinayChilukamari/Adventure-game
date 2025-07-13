
def choose_options():
    player_choice=input('Where do you want to go, Left or Right?').lower()
    return player_choice

   
def play_again():
    while True:
        play=input("Would like to play again? (yes/no) | (y/n)").lower()
        if play == 'yes'or play == 'y':
            print('Let \'s start the game!')
            start_game()
            break
        elif play=='no' or play=='n':
            print('Ok, we will play some other time!')
            break
        else:
            print("Invalid input, please enter yes or no")
       
def start_game():
    while True:
        choose=choose_options()
        if choose=='left':
            print('You went left and fell off the cliff, game over, try again.')
            play_again()
            break
        elif choose=='right':
            print('You reached weapon store, choose your weapon')
            weapon=input("Sword or stick?").lower()
            if weapon=='stick':
                print('Crocodile ate you, game over, try again.')
                play_again()
                break
            elif weapon=='sword':
                print('Great! you defeated Crocodile and won the game.')
                play_again()
                break
            else:
                print('Invalid choice, try again')        
        else:
            print('Invalid choice, try again')
        

player_name=input("Enter your name: ")
print(f"Hello {player_name}, Welcome to Choose your own adventure game!")

while True:
    play=input("Should we start the game? (yes/no) | (y/n)").lower()
    if play == 'yes'or play == 'y':
        print('Let \'s start the game!')
        start_game()
        break
    elif play=='no' or play=='n':
        print('Ok, we will play some other time!')
        break
    else:
        print("Invalid input, please enter yes or no")


