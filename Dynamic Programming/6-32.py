n = int(input())
d = []
for _ in range(n):
    d.append(list(map(int, input().split())))

for i in range(n-2,-1,-1):
    for j in range(len(d[i])):
        d[i][j] = d[i][j] + max(d[i+1][j], d[i+1][j+1])

print(d[0][0])