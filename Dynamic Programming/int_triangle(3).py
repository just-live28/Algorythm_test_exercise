import sys
input = sys.stdin.readline

n = int(input())

d = []

for i in range(n):
    d.append(list(map(int, input().split())))

for a in range(n-2,-1,-1):
    for b in range(len(d[a])):
        d[a][b] = d[a][b] + max(d[a+1][b], d[a+1][b+1])

print(d[0][0])