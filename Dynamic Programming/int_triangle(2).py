# 2층부터 아래층까지 (1~n)
# 윗층의 큰 것 + 자기 수
# d[n][m] = max(d[n-1][m-1] + arr[n][m], d[n-1][m] + arr[n][m])

import sys
input = sys.stdin.readline

n = int(input())

array = []
d = []

for _ in range(n):
    line = list(map(int, input().split()))
    array.append(line)
    d.append([0] * len(line))

d[0][0] = array[0][0]

for a in range(1, n):
    length = len(array[a])
    for b in range(length):
        if b-1 < 0:
            up_left = 0
        else:
            up_left = d[a-1][b-1]
        
        if b > length-2:
            up_right = 0
        else:
            up_right = d[a-1][b]
        
        d[a][b] = max(up_left, up_right) + array[a][b]

print(max(d[n-1]))