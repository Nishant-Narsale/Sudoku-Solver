
board = [
    [0,0,0,0,0,0,8,1,7],
    [0,2,0,9,0,0,0,3,0],
    [8,0,0,7,0,0,9,0,0],
    [5,0,0,0,8,0,0,0,0],
    [0,0,3,1,0,2,5,0,0],
    [0,0,0,0,4,0,0,0,6],
    [0,0,8,0,0,5,0,0,4],
    [0,7,0,0,0,4,0,6,0],
    [2,9,4,0,0,0,0,0,0]
]

def show_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('-----------------------------')
        
        for j in range(len(board[0])):

            if j % 3 == 0 and j != 0:
                print('| ',end='')

            print(board[i][j],' ',end='')

            if j == 8:
                print('')

# find a empty place
def find_empty(board):
    done = False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                done = True
                return (i,j)
    
    return ()

"""
 find a number that can be fit there by checking for first number from 0 to 1
 a number is fit at that particular position if it is not present in that column or on its box or in it's row
"""

assigned_numbers = []
def valid_number(board,empty_row,empty_col,start_from=1):
    done = False
    if not done:
        for i in range(start_from,10):
            #checking in row
            for j in board[empty_row]:
                if j == i:  #if in row break checking row loop and check for another value of i
                    break

            else:
                # i value not in row then checking in column 
                for k in range(len(board)):
                    c = board[k][empty_col]
                    if c == i:  #if i value in column break checking column loop and check for another value of i
                        break

                else:
                    # now value of i is not in column and also not in row
                    # now checking does i value exist in the 3 x 3 box of that element
                    """ 
                    now i will devide board in 3 new-rows and 3 new-columns
                    and every new-row contain 3 rows
                    and every new-col contain 3 columns

                    hence,
                    new-row will start from 0 and end on 2
                    same for new-col

                    hence, formula for both is 
                    new-row = row // 3
                    new-col = column //3 
                    """

                    new_row = empty_row // 3
                    new_col = empty_col // 3

                    #checking in row three times so that all the elements will be checked
                    for c in range(3):
                        in_box = False
                        #following loop check it for single row of that box
                        for r in range(3):
                            n = board[(new_row*3)+c][(new_col*3)+r]
                            if n == i:
                                in_box = True
                                break

                        if in_box:
                            break

                    if not in_box:
                        board[empty_row][empty_col] = i
                        assigned_numbers.append([empty_row , empty_col, i])
                        done = True
                        break

        if i == 9 and board[empty_row][empty_col] == 0:
            board[empty_row][empty_col] = '#'


# main loop to execute this functions multiple times
while True:
    try:
        empty_row , empty_col = find_empty(board)
        valid_number(board, empty_row, empty_col)
    except:
        break

show_board(board)
print("Assigned Numbers = ",assigned_numbers)