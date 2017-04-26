def spiralize(size):
    if size == 1:
        return [[1]]
    spiral = [[0] * size for i in range(size)]
    spiral = draw_nulls(spiral, 0, 0)
    while spiral[1][0]:
        spiral = rotate_table(spiral)
    return(spiral)


def rotate_table(board):
    board = [row[::-1] for row in board]
    new_board = []
    for i in range(len(board)):
        new_board.append([row[i] for row in board])
    return new_board


def draw_nulls(board, r, c, d=1):
    N = len(board)
    if d < 4:
        isthree = 1 if d == 3 else 0
        board[r][c:N-isthree] = [1] * (N - c-isthree)
        c = N - 1
    else:
        _count = 0
        while not board[r][c+_count + 1]:
            board[r][c+_count] = 1
            _count += 1
        if _count < 3:
            return board
        c = c + _count - 1
    r, c = N - c - 1, r
    board = rotate_table(board)
    board = draw_nulls(board, r, c, d+1)
    return board


for r in spiralize(10):
    print(r)
