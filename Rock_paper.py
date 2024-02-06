import random

def user_move():
    print('1) Rock')
    print('2) Paper')
    print('3) Scissors')
    print('4) Exit')
    choice = int(input('Enter the move you want (1-4): '))
    return choice

def computer_move():
    random_num = random.randint(1, 3)
    print('Computer move:', random_num)
    return random_num

def play_round(real_move, fake_move):
    if real_move == fake_move:
        print('GAME TIE!!')
    elif (real_move == 1 and fake_move == 3) or (real_move == 2 and fake_move == 1) or (real_move == 3 and fake_move == 2):
        print('Congratulations! You Win Round')
    else:
        print('Computer Wins!!!')

def main():
    play_again = True

    while play_again:
        real_move = user_move()
        if real_move == 4:
            print('Exiting the game. Goodbye!')
            break

        fake_move = computer_move()
        play_round(real_move, fake_move)

        play_again_input = input('Do you want to play again? (yes/no): ').lower()
        play_again = play_again_input == 'yes'

if __name__ == "__main__":
    main()
