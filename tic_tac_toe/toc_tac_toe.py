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