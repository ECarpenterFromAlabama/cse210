# CSE210 - W1 Tic-Tac-Toe 
# Easterling Carpenter

def main():
    table = [ '1', '2', '3' , '4' , '5', '6', '7', '8', '9' ]
    x_turn = True
    while(check_win(table)):
        disp_table(table)
        prompt_turn(table, x_turn)
        x_turn = not x_turn

def disp_table(t):
    print(t[0], t[1], t[2], sep='|')
    print('-+-+-')
    print(t[3], t[4], t[5], sep='|')
    print('-+-+-')
    print(t[6], t[7], t[8], sep='|')
    print()

def prompt_turn(t, x):
    if(x):
        player = 'x'
    elif(not x):
        player = 'o'
    placement = int(input(f'{player}\'s turn to choose a square (1-9): '))
    t[placement-1] = player
    print()

def check_win(t):
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
    return next_turn

if __name__ == '__main__':
    main()