word1 = input()
word2 = input()

n, m = len(word1), len(word2)

d = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    d[i][0] = i

for j in range(1, m+1):
    d[0][j] = j

for a in range(1, n+1):
    for b in range(1, m+1):
        if word1[a-1] == word2[b-1]:
            d[a][b] = d[a-1][b-1]
        else:
            d[a][b] = 1 + min(d[a-1][b-1], d[a-1][b], d[a][b-1])

print(d[n][m])