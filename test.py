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
                    list_gen(board, r, c)[1]
                    )
                inf.append(all_inf)
    inf = sorted([i for i in enumerate(inf) if i[1]], key=lambda x: x[1], reverse=True)
    inf = [(i[0] // 9, i[0] % 9) for i in inf]
    #inf = sorted(inf, key=lambda x: valid_nums(board, x[0], x[1]), reverse=True)
    for i in inf:
        print(len(valid_nums(board, i[0], i[1])))
    return inf