def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        col_index=move-1
        for row_index in range(len(board)):
            if board[row_index][col_index] !=0 :
                doll = board[row_index][col_index]
                board[row_index][col_index] =0
                if stack and stack[-1]==doll:
                    stack.pop()
                    answer+=2
                else:
                    stack.append(doll)
                break
                
    return answer
    
