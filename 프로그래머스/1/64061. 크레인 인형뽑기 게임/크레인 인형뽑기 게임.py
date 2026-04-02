def solution(board, moves):
    answer = 0
    basket = []

    for move in moves:
        col = move - 1

        for i in range(len(board)):
            if board[i][col] != 0:
                doll = board[i][col]
                board[i][col] = 0

                if basket and basket[-1] == doll:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(doll)

                break

    return answer