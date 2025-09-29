import sys
input = sys.stdin.readline

n = int(input())
arr = [None] + list(map(int, input().split()))

d = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    d[i][i] = 1
    
    if arr[i-1] == arr[i]:
        d[i-1][i] = 1

for length in range(3, n+1):
    for st in range(1, n-length+2):
        en = st + length -1
        
        if arr[st] == arr[en] and d[st+1][en-1]:
            d[st][en] = 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(d[s][e])