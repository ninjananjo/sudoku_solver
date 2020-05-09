import numpy as np


board_np = np.array([
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
])


def print_board(board):
    """prints 3x3 Sudoku board"""
    for i in range(9):
        if i % 3 == 0 and i != 0:  # horizontal break after every 3 row
            print('- - - - - - - - - - -')
        for j in range(9):
            if j == 8:  # no space on last column
                print(board[i][j])
            elif(j + 1) % 3 == 0:  # add pipe after every 3rd column
                print(board[i][j], '|', end=' ')
            else:  # space separated for all other numbers
                print(board[i][j], end=' ')


def find_empty(board):
    """Returns location of first empty (0) in Sudoku board. If no empty cell is found a False is returned"""
    empty_cells = np.where(board == 0)
    if empty_cells[0].size == 0:
        return False
    else:
        return empty_cells[0][0], empty_cells[1][0]


def valid(board: np.ndarray, num: int, position: tuple) -> bool:
    """Check if the suggested number, 'num' is valid in the specified position on the Sudoku board.
    If valid return True else False"""
    if num in board[position[0], :]:  # check row
        print(num, 'Row duplication')
        return False

    if num in board[:, position[1]]:  # check column
        print(num, 'Column duplication')
        return False

    mini_sq_row, mini_sq_col = map(lambda x: x//3*3, position)
    if num in board[mini_sq_row: mini_sq_row + 3, mini_sq_col: mini_sq_col + 3]:  # check 3x3
        print(num, '3x3 duplication')
        return False

    return True


def solve(board):
    """Finds a valid number for an empty cell"""
    empty_cell = find_empty(board)
    print(empty_cell)

    for num in range(1, 10):
        if valid(board, num, empty_cell):
            print(num)
            board[empty_cell[0]][empty_cell[1]] = num
            break



print_board(board_np)
solve(board_np)
print_board(board_np)
#print(find_empty(board_np))
# print(valid(board_np, 6, (0, 2))