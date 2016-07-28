tictac={'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def board(b):
        print tictac['top-L']+'|'+tictac['top-M']+'|'+tictac['top-R']
        print "-+-+-"
        print tictac['mid-L']+'|'+tictac['mid-M']+'|'+tictac['mid-R']
        print "-+-+-"
        print tictac['low-L']+'|'+tictac['low-M']+'|'+tictac['low-R']

board(tictac)
turn='X'
for i in range(9):
    print 'it\'s '+turn+'\'s turn'
    choice=raw_input('enter ur choice:')
    tictac[choice]=turn
    if turn=='X':
        turn='O'
    else:
        turn='X'
    if tictac['top-L']==tictac['top-M']==tictac['top-R']=='X' or tictac['mid-L']==tictac['mid-M']==tictac['mid-R']=='X' or tictac['low-L']==tictac['low-M']==tictac['low-R']=='X' or tictac['mid-M']==tictac['top-M']==tictac['low-M']=='X' or tictac['top-L']==tictac['mid-L']==tictac['low-L']=='X' or tictac['top-R']==tictac['mid-R']==tictac['low-R']=='X' or tictac['top-L']==tictac['mid-M']==tictac['low-R']=='X' or tictac['top-R']==tictac['mid-M']==tictac['low-L']=='X':
        print 'X won'
        break
    elif tictac['top-L']==tictac['top-M']==tictac['top-R']=='O' or tictac['mid-L']==tictac['mid-M']==tictac['mid-R']=='O' or tictac['low-L']==tictac['low-M']==tictac['low-R']=='O' or tictac['mid-M']==tictac['top-M']==tictac['low-M']=='O' or tictac['top-L']==tictac['mid-L']==tictac['low-L']=='O' or tictac['top-R']==tictac['mid-R']==tictac['low-R']=='O' or tictac['top-L']==tictac['mid-M']==tictac['low-R']=='O' or tictac['top-R']==tictac['mid-M']==tictac['low-L']=='O':
        print 'O won'
        break
    board(tictac)


if tictac['top-L']!=tictac['top-M']!=tictac['top-R'] and tictac['mid-L']!=tictac['mid-M']!=tictac['mid-R'] and tictac['low-L']!=tictac['low-M']!=tictac['low-R']:
    print 'it\'s a draw'
