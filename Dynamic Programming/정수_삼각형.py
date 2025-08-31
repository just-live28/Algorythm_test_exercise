# d[i][j(0~i)]: i층의 j열에서 얻을수 있는 최대합
# d[i][j] = arr[i][j] + max(d[i+1][j], d[i+1][j+1])
# 초깃값: d[제일아래층][0~제일아래층] = arr[제일아래층][0~제일아래층]

n = int(input())
arr = [None]
for _ in range(n):
    arr.append(list(map(int, input().split())))

d = [[0] * n for _ in range(n+1)]
d[n] = arr[n]

for i in range(n-1, 0, -1):
    for j in range(i):
        d[i][j] = arr[i][j] + max(d[i+1][j], d[i+1][j+1])

print(max(d[1]))