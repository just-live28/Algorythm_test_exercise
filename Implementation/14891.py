def turn_gear(num, dir, gears):
    turns = [0] * 5
    turns[num] = dir
    
    idx = num
    while idx > 1 and arr[idx-1][(gears[idx-1] + 2) % 8] != arr[idx][(gears[idx] + 6) % 8]:
        turns[idx-1] = -turns[idx]
        idx -= 1
    
    idx = num
    while idx < 4 and arr[idx+1][(gears[idx+1] + 6) % 8] != arr[idx][(gears[idx] + 2) % 8]:
        turns[idx+1] = -turns[idx]
        idx += 1

    for i in range(1, 5):
        # 시계 방향 회전의 경우, 이전 것이 12시가 됨
        if turns[i] == 1:
            gears[i] = (gears[i] - 1) % 8
        # 반시계 방향 회전의 경우, 다음 것이 12시가 됨
        elif turns[i] == -1:
            gears[i] = (gears[i] + 1) % 8

arr = [None]
for _ in range(4):
    arr.append(list(map(int, input().strip())))
k = int(input())
gears = [0] * 5
for _ in range(k):
    n, d = map(int, input().split())
    turn_gear(n, d, gears)

result = 0
for i in range(1, 5):
    if arr[i][gears[i]] == 1:
        result += 2 ** (i-1)

print(result)