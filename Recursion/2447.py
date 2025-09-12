# 전체 보드의 x~x+k, y~y+k인 k * k 보드에 '*'과 ' '을 적절하게 채우는 함수
def func(k, x, y):
    if k == 1:
        board[x][y] = '*'
        return
    
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            
            nxt = k // 3
            func(nxt, x + nxt * i, y + nxt * j)
            

n = int(input())
board = [[' '] * n for _ in range(n)]
func(n, 0, 0)

for i in range(n):
    for j in range(n):
        print(board[i][j], end='')
    print()