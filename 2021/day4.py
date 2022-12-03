from fileHandle import readfile
import re


def search(number, board):
    for i in range(5):
        for j in range(5):
            if board[i][j]['value'] == number:
                board[i][j]['flag'] = True
                row_is_marked = True
                column_is_marked = True
                for k in range(5):
                    row_is_marked &= board[i][k]['flag']
                    column_is_marked &= board[k][j]['flag']
                return row_is_marked or column_is_marked
    return False


def puzzle7(input_file='day4.txt'):
    data = readfile(input_file).split('\n\n')
    numbers = data[0].split(',')
    boards = []
    for board in data[1:]:
        rows = board.split('\n')
        b = [re.split(' +', re.sub('^ *', '', row)) for row in rows]
        b = [[dict(value=col, flag=False) for col in row] for row in b]
        boards.append(b)
    for number in numbers:
        for board in boards:
            if search(number, board):
                thesum = 0
                for row in board:
                    for col in row:
                        thesum += 0 if col['flag'] else int(col['value'])
                return int(number), thesum, int(number) * thesum
    return None


def puzzle8(input_file='day4.txt'):
    data = readfile(input_file).split('\n\n')
    numbers = data[0].split(',')
    boards = []
    for board in data[1:]:
        rows = board.split('\n')
        b = [re.split(' +', re.sub('^ *', '', row)) for row in rows]
        b = [[dict(value=col, flag=False) for col in row] for row in b]
        boards.append(b)

    to_be_removed = []
    for number in numbers:
        for board in to_be_removed:
            boards.remove(board)
        to_be_removed.clear()
        for board in boards:
            if search(number, board):
                if len(boards) == 1:
                    thesum = 0
                    for row in board:
                        for col in row:
                            thesum += 0 if col['flag'] else int(col['value'])
                    return int(number), thesum, int(number) * thesum
                to_be_removed.append(board)
    return None
