import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort(key = lambda x : (x[0], x[1]))

    huddle = arr[0][1]
    result = 1
    for i in range(1, n):
        if arr[i][1] < huddle:
            result += 1
            huddle = arr[i][1]

    print(result)