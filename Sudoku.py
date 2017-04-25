import copy


def sudoku_solver(board, d=1):
    print(board)
    print(d)
    inf = most_information(board)
    if not inf:
        return board
    if inf == 'STOP':
        return
    for idx in range(len(inf)):
        r, c = inf[idx][0], inf[idx][1]
        for v in inf[idx][2]:
            new_board = copy.deepcopy(board)
            new_board[r][c] = v
            result = sudoku_solver(new_board, d+1)
            if result:
                return result


def list_gen(board, r, c):
    _list = []
    for row in range(r - (r % 3), r + 3 - (r % 3)):
        for col in range(c - (c % 3), c + 3 - (c % 3)):
            _list.append(board[row][col])
    return _list


def most_information(board):
    inf = []
    for r in range(9):
        for c in range(9):
            if not board[r][c]:
                data = [r, c, valid_nums(board, r, c)]
                if len(data[2]) == 0:
                    return 'STOP'
                if len(data[2]) == 1:
                    return [data]
                inf.append(data)
    inf = sorted(inf, key=lambda x: len(x[2]))
    return inf[0]


def valid_nums(board, r, c):
    nums = list(set(range(1, 10)) - (
        set(board[r]) |
        set([j[c] for j in board]) |
        set(list_gen(board, r, c))
    ))
    return nums



puzzle = [[0, 0, 6, 1, 0, 0, 0, 0, 8], [0, 8, 0, 0, 9, 0, 0, 3, 0], [2, 0, 0, 0, 0, 5, 4, 0, 0], [4, 0, 0, 0, 0, 1, 8, 0, 0], [0, 3, 0, 0, 7, 0, 0, 4, 0], [0, 0, 7, 9, 0, 0, 0, 0, 3], [0, 0, 8, 4, 0, 0, 0, 0, 6], [0, 2, 0, 0, 5, 0, 0, 8, 0], [1, 0, 0, 0, 0, 2, 5, 0, 0]]


#print(most_information(puzzle))
#print(list_gen(puzzle, 5, 5))
#print(valid_nums(puzzle, 5, 3))

print(sudoku_solver(puzzle))
    

