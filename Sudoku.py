import copy

def solve(board, d=1):
    mi = most_information(board)
    if not mi:
        return board
    for (r, c) in mi:
        possib = valid_nums(board, r, c)
        print(possib)
        #print(d)
        if not possib:
            return
        for v in possib:
            new_board = copy.deepcopy(board)
            new_board[r][c] = v
            print(new_board)
            result = solve(new_board, d+1)
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
            if board[r][c]:
                inf.append(0)
            else:
                all_inf = (
                    len([i for i in board[r] if i]) +
                    len([j[c] for j in board if j[c]]) +
                    len([k for k in list_gen(board, r, c) if k])
                    )
                inf.append(all_inf)
    inf = sorted([i for i in enumerate(inf) if i[1]], key=lambda x: x[1], reverse=True)
    inf = [(i[0] // 9, i[0] % 9) for i in inf]
    return inf


def valid_nums(board, r, c):
    nums = list(set(range(1, 9)) - (
        set(board[r]) |
        set([j[c] for j in board]) |
        set(list_gen(board, r, c))
    ))
    return nums



puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]


#print(most_information(puzzle))
#print(list_gen(puzzle, 5, 5))
#print(valid_nums(puzzle, 0, 2))
#solve(puzzle)

puzzle2=[[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solve(puzzle2)
    

