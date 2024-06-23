import numpy as np
import math

"""
Tic-tac-toe using 1-9 grid system for input
User is always 'X' and the computer is 'O' 

The functions referring to the player and comp taking their turn return a boolean value.
If either one makes a move to end the game, then we can break from the game loop.
To elaborate, either function returning True means they have won.
"""
USER_CHAR = 'X'
COMP_CHAR = 'O'



def coin_flip() -> bool:
    return True if np.random.randint(1,3) == 1 else False

# Return 2d index from single digit number
def get_2d_coord(cell):
    """
     1    2    3
     4    5    6
     7    8    9

    0,0  0,1  0,2
    1,0  1,1  1,2
    2,0  2,1  2,2
    """
    cell -= 1
    row = int(cell / 3)
    col = cell % 3
    coord = [row, col]
    return coord

def get_input(board):
    while True:
        cell = input("Where are you going to move? Enter number 1-9: ")
        try: 
            cell = int(cell)
            
            if cell > 0 and cell < 10:
                cell = get_2d_coord(cell)
                if board[cell[0], cell[1]] == ' ':
                    return cell
                else:
                    print("Square already occupied.")
            else:
                print("Invalid target.")

        except ValueError:
            print("Invalid input. Please try again.")

def find_open_cells(board):
    open_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                open_cells.append([i,j])
    return open_cells

def comp_cell(board):
    open_cells = find_open_cells(board)
    return open_cells[np.random.randint(0,len(open_cells))]

def user_turn(board):
    cell = get_input(board)
    board[cell[0], cell[1]] = USER_CHAR
    return [board, cell]

def comp_turn(board):
    cell = comp_cell(board)
    board[cell[0], cell[1]] = COMP_CHAR
    return [board, cell]

def check_for_win(board, cell):
    # Create sub arrays that are one dimensional to check if a row or column is complete
    # Columns and diagonals are treated as rows; They are simply lists of length 3
    all_rows = []
    row = np.array(board[cell[0]])
    col = []
    for i in range(3):
        col.append(board[i][cell[1]])
    col = np.array(col)
    # col = np.array([curr_row[cell[0]] for curr_row in board])

    all_rows.append(row)
    all_rows.append(col)

    # While we always have to check the rows/columns, diagonals are conditional
    if cell == [0,0] or cell == [1,1] or cell == [2,2]:
        diag1 = np.array([board[0][0], board[1][1], board[2][2]])
        all_rows.append(diag1)
    
    if cell == [0,2] or cell == [1,1] or cell == [2,0]: 
        diag2 = np.array([board[0][2], board[1][1], board[2][0]])
        all_rows.append(diag2)

    #print(all_rows)
    for row in all_rows:
        if all(x == row[0] for x in row):
            return True
        
    return False
   
def tic_tac_toe():
    board = np.full((3,3), fill_value=' ', dtype=str)
    # User goes first
    if coin_flip():
        print("Player moves first.", '\n')
        print(board, '\n')
        while True:
            turn = user_turn(board)
            board = turn[0]
            cell = turn[1]
            print(board, 'Player moved at:', cell, '\n')
            user_victory = check_for_win(board, cell)
            if user_victory: 
                print("Congrats, you win!")
                break
            if len(find_open_cells(board)) < 1:
                print("Draw!")
                break

            turn = comp_turn(board)
            board = turn[0]
            cell = turn[1]
            print(board, 'CPU moves at:', cell, '\n')
            comp_victory = check_for_win(board, cell)
            if comp_victory:
                print("Rats, you lost!")
                break

    # Computer goes first        
    else:
        print("Computer goes first.")
        while True:
            turn = comp_turn(board)
            board = turn[0]
            cell = turn[1]
            print(board, 'CPU moves at:', cell, '\n')
            comp_victory = check_for_win(board, cell)
            if comp_victory:
                print("Rats, you lost!")
                break
            if len(find_open_cells(board)) < 1:
                print("Draw!")
                break

            turn = user_turn(board)
            board = turn[0]
            cell = turn[1]
            print(board, 'Player moved at:', cell, '\n')
            user_victory = check_for_win(board, cell)
            if user_victory: 
                print("Congrats, you win!")
                break
            
tic_tac_toe()
# board = np.full((3,3), fill_value=' ', dtype=str)
# print(comp_move(board))




