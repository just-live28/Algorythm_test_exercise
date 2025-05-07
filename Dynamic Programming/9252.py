s1 = input()
s2 = input()

n = len(s1)
m = len(s2)

d = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if s1[i-1] == s2[j-1]:
            d[i][j] = d[i-1][j-1] +1
        else:
            d[i][j] = max(d[i][j-1], d[i-1][j])

print(d[n][m])
if d[n][m] > 0:
    x, y = n, m
    result = []
    while x > 0 and y > 0:
        if s1[x-1] == s2[y-1]:
            result.append(s1[x-1])
            x -= 1
            y -= 1
        elif d[x-1][y] >= d[x][y-1]:
            x -= 1
        else:
            y -= 1
    
    result.reverse()
    print(''.join(result))