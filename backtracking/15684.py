# N 세로선 M 가로선

# 가로 가능 # 세로 가능
# 1, 1 에 놓으면? (b, b+1) 세로선의 a 가로선에 놓는 사다리
# 1, 1 => 1(오른쪽) / 1, 2 => 2(왼쪽)

# 각각의 func(k, x, y) : 추가 사다리가 k개 배치됨. 조합이므로 x열 y행부터 순회
# 만약 사다리 놓기 전 현재 사다리가 3개이거나 최소 사다리 개수라면 나가리
# 해당 가로선이 오른쪽과 왼쪽으로 연결되지 않았다면 사다리 배치 및 func(k+1, i, j+2) 순회 <- j, j+1이 금지되므로 j+2부터 가능
# 이후 사다리 다시 빼기

# 시뮬레이션(check) : 모든 번호가 자기 번호로 떨어지는지. 가능하다면 True 반환

def check(ladder):
    for i in range(1, n+1):
        now = i
        for j in range(1, h+1):
            if ladder[j][now] == 1:
                now += 1
            elif ladder[j][now] == 2:
                now -= 1
        if now != i:
            return False
    return True

def func(cnt, x, y):
    global min_ladder
    
    if check(ladder):
        min_ladder = min(min_ladder, cnt)
        return
    elif cnt >= 3 or cnt >= min_ladder:
        return
    
    for i in range(x, h+1):
        k = y if i == x else 1
        for j in range(k, n):
            if ladder[i][j] == 0 and ladder[i][j+1] == 0:
                ladder[i][j] = 1
                ladder[i][j+1] = 2
                func(cnt + 1, i, j+2)
                ladder[i][j] = 0
                ladder[i][j+1] = 0

n, m, h = map(int, input().split())
ladder = [[0] * (n+1) for _ in range(h+1)]
for _ in range(m):
    a, b = map(int, input().split())
    ladder[a][b] = 1
    ladder[a][b+1] = 2
    
min_ladder = int(1e9)
func(0, 1, 1)
if min_ladder == int(1e9):
    print(-1)
else:
    print(min_ladder)