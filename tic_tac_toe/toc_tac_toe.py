"""三目並べ"""

OPEN = 0
FIRST = 1
SECOND = 2
DRAW = 3

turn = 1                                                #手番
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]               #盤面

def show_turn() -> str:
    """手番を表す文字列を返す"""
    if turn == FIRST:
        return('先手')
    elif turn == SECOND:
        return('後手')
    else:
        return('手番の値が範囲外')

def init_turn() -> None:
    """手番を初期化する"""
    global turn
    turn = 1

def chage_turn() -> None:
    """手番を交代する"""
    global turn
    if turn == FIRST:
        turn = SECOND
    elif turn == SECOND:
        turn == FIRST

def show_board() -> str:
    """盤面を表す文字列を返す"""
    s = ' :0 1 2\n-----------\n'
    for i in range(3):
        s = s + str(i) + ':'
        for j in range(3):
            cell = ''
            if board[i][j] == OPEN:
                cell = ''
            elif board[i][j] == FIRST:
                cell = '0'
            elif board[i][j] == SECOND:
                cell = 'X'
            else:
                cell = '?'
            s = s + cell + ''
    return s

def init_board() -> None:
    """盤面を全て空(OPEN)に初期化する"""
    for i in range(3):
        for j in range(3):
            board[i][j] = OPEN

def examine_board(i: int, j: int) -> int:
    """盤面i,jの位置の値を返す"""
    return board[i][j]

def set_board(i: int, j: int, t: int) -> str:
    """盤面のi,jに手番を登録、状態を文字列で返す
    return 'OK'              #成功
           'illegal turn'    #手番が正しくない
           'illegal slot'    #指定された場所が正しくない
    """

    if(i >= 0) and (i < 3) and (j >= 0) and ( j < 3):
        if(t > 0) and ( t < 3):
            if examine_board(i, j) == 0:
                board[i][j] = t
                return 'OK'
            else:
                return 'Not empty'
        else:
            return 'illegal turn'
    else:
        return 'illegal slot'


        