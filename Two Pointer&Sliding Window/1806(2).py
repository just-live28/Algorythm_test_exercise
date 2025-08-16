# st, en을 놓고 투 포인터로 확인
INF = int(1e9)

n, s = map(int, input().split())
arr = list(map(int, input().split()))

total = arr[0]
en = 0
min_length = INF
for st in range(n):
    while en < n and total < s:
        en += 1
        if en < n:
            total += arr[en]
    if en == n:
        break
    min_length = min(min_length, en - st + 1)
    total -= arr[st]

if min_length == INF:
    print(0)
else:
    print(min_length)