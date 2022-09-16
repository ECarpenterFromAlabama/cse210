# CSE210 - W1 Tic-Tac-Toe 
# Easterling Carpenter

def main():
    table = [ 1, 2, 3 , 4 , 5, 6, 7, 8, 9 ]
    x_turn = True
    play_count = 0
    while(check_win(table, play_count)):
        disp_table(table)
        prompt_turn(table, x_turn)
        x_turn = not x_turn
        play_count+= 1

def disp_table(t):
    print(t[0], t[1], t[2], sep='|')
    print('-+-+-')
    print(t[3], t[4], t[5], sep='|')
    print('-+-+-')
    print(t[6], t[7], t[8], sep='|')
    print()

def prompt_turn(t, x):
    playable = True
    while(playable):
        if(x):
            player = 'x'
        elif(not x):
            player = 'o'
        while(True):
            try:
                placement = int(input(f'{player}\'s turn to choose a square (1-9): '))
                playable = can_place(t[placement-1])
                break
            except ValueError:
                print('Please enter a valid number 1-9')
                print()
        if(playable and placement <=9 and placement >= 1 ):
            t[placement-1] = player
            print()
            return
        else:
            print('Please make sure the number is between 1 and 9 and the space is not currently taken.')
            disp_table(t)
            playable = True
    print()

def can_place(ti):
    if ti == 'x' or ti == 'o':
        print('That place is already taken, please try again.\n')
        can_play = False
    else:
        can_play = True
    return can_play

def check_win(t, c):
    next_turn = True
    WIN_CONDS = [ t[0] == t[1] and t[0] == t[2], \
                  t[3] == t[4] and t[3] == t[5], \
                  t[6] == t[7] and t[6] == t[8], \
                  t[0] == t[3] and t[0] == t[6], \
                  t[1] == t[4] and t[1] == t[7], \
                  t[2] == t[5] and t[2] == t[8], \
                  t[0] == t[4] and t[0] == t[8], \
                  t[2] == t[4] and t[2] == t[6]
                ] 
    if(any(WIN_CONDS)):
        next_turn = False
        disp_table(t)
        print('Good game. Thanks for playing!')
    elif(c == 9):
        print('Game Over')
        next_turn = False
    else:
        return next_turn

if __name__ == '__main__':
    main()