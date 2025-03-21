def check(x, y, length):
    prev = board[x][y]
    for a in range(x, x + length):
        for b in range(y, y + length):
            if a == x and b == y:
                continue
            if board[a][b] != prev:
                return False
    return True

def func(k, x, y):
    global blue, white
    if k == 0:
        if board[x][y] == 1:
            blue += 1
        else:
            white += 1
        return
    
    half = 2 ** (k-1)
    
    if check(x, y, 2 * half):
        if board[x][y] == 1:
            blue += 1
        else:
            white += 1
        return
    
    func(k-1, x, y)
    func(k-1, x, y + half)
    func(k-1, x + half, y)
    func(k-1, x + half, y + half)

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
blue, white = 0, 0
exp = 0
while n > 1:
    n //= 2
    exp += 1
    
func(exp, 0, 0)
print(white)
print(blue)