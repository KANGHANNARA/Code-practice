def solution(board, moves):
    result = []
    answer = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                result.append(board[i][move-1])
                board[i][move-1] = 0
                if result[-2:-1] == result[-1:]:
                    result = result[:-2]
                    answer += 1
                break
    return answer*2