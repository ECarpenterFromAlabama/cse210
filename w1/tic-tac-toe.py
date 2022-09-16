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
    """Displays the current tic-tac-toe table in the following format:
        1|2|3 \n
        -+-+- \n
        4|5|6 \n
        -+-+- \n
        7|8|9
    Where any integer may replaced by and 'x' or an 'o'
    Parameters
        t: a list of elements in the current tic-tac-toe table
    Return: Nothing
    """                         
    print(t[0], t[1], t[2], sep='|')
    print('-+-+-')
    print(t[3], t[4], t[5], sep='|')
    print('-+-+-')
    print(t[6], t[7], t[8], sep='|')
    print()

def prompt_turn(t, x):
    """Prompts the current player to take their turn by
    asking for a position(1-9) on the grid. It can catch errors
    where the input value is not an integer of 1 through 9.
    Utilizes can_place() to check to se if the space is taken.
    Parameters
        t: a list of elements in the current tic-tac-toe table
        x: boolean asking if it is x's turn or not
    Return: Nothing
    """
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
    """Determines whether or not a space on the grid
    is already occupied by a player.
    Parameters
        ti: the item in the list that corresponds to the player's
            selection
    Return: can_play: Boolean indicating if that spot on the grid
                      is playable
    """
    if ti == 'x' or ti == 'o':
        print('That place is already taken, please try again.\n')
        can_play = False
    else:
        can_play = True
    return can_play

def check_win(t, c):
    """Checks to see if a player has won or if
    the game can no longer continue due to the grid
    being full.
    Parameters
        t: a list of elements in the current tic-tac-toe table
        c: count of how many turns have passed.
    Return: next_turn: Boolean determining if the game continues.
    """
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