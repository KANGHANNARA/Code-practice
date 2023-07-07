def solution(n):
    answer = [[0]*n for i in range(n)]
    x = 0
    y = 0
    direction = "right"
    for i in range(1,n*n+1):
        answer[x][y] = i
        if direction == "right":
            if y == n-1 or answer[x][y+1] != 0:
                direction = "down"
                x += 1
            else:
                y += 1
        elif direction == "down":
            if x == n-1 or answer[x+1][y] != 0:
                direction = "left"
                y -= 1
            else:
                x += 1
        elif direction == "left":
            if y == 0 or answer[x][y-1] != 0:
                direction = "top"
                x -= 1
            else:
                y -= 1
        elif direction == "top":
            if x == 0 or answer[x-1][y] != 0:
                direction = "right"
                y += 1
            else:
                x -= 1
    return answer