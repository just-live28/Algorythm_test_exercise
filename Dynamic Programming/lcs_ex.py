word1 = "DATABASE"
word2 = "ALPHABET"
n, m = len(word1), len(word2)

d = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if word1[i-1] == word2[j-1]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])

# print(d[n][m])    출력: 4

i, j = n, m
result = []
while i > 0 and j > 0:
    if word1[i-1] == word2[j-1]:
        result.append(word1[i-1])
        i -= 1
        j -= 1
    elif d[i-1][j] >= d[i][j-1]:
        i -= 1
    else:
        j -= 1

print(''.join(reversed(result)))    # AABE