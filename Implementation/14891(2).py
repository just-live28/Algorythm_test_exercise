# 현재 상태에 대해 전체 톱니바퀴의 회전을 기록하고, 일괄 회전시키는 함수
def turn_gear(num, dir, gears, indexes):
    turns = [0] * 5
    turns[num] = dir
    
    # 왼쪽으로 전파
    idx = num
    while idx > 1 and gears[idx-1][(indexes[idx-1] + 2) % 8] != gears[idx][(indexes[idx] + 6) % 8]:
        turns[idx-1] = -turns[idx]
        idx -= 1
    
    # 오른쪽으로 전파
    idx = num
    while idx < 4 and gears[idx+1][(indexes[idx+1] + 6) % 8] != gears[idx][(indexes[idx] + 2) % 8]:
        turns[idx+1] = -turns[idx]
        idx += 1
    
    # 일괄 회전
    for i in range(1, 5):
        # 반시계 방향 회전
        if turns[i] == -1:
            indexes[i] = (indexes[i] + 1) % 8
        # 시계 방향 회전
        elif turns[i] == 1:
            indexes[i] = (indexes[i] - 1) % 8

gears = [None]
for _ in range(4):
    gears.append(list(map(int, input())))

indexes = [0] * 5
k = int(input())
for _ in range(k):
    num, dir = map(int, input().split())
    turn_gear(num, dir, gears, indexes)

result = 0
for i in range(1, 5):
    if gears[i][indexes[i]] == 1:
        result += 2 ** (i-1)

print(result)