n = int(input())

d = [[0] * 10 for _ in range(n+1)]
for i in range(1, 10):
    d[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        left = right = 0
        
        if j-1 >= 0:
            left = d[i-1][j-1]
        
        if j+1 <= 9:
            right = d[i-1][j+1]
        
        d[i][j] = (left + right) % int(1e9)

print(sum(d[n]) % int(1e9))