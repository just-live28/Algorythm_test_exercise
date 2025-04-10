s1 = input()
s2 = input()

d = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

for i in range(1, len(s1)+1):
    d[i][0] = i
for j in range(1, len(s2)+1):
    d[0][j] = j

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i-1] == s2[j-1]:
            d[i][j] = d[i-1][j-1]
        else:
            d[i][j] = 1 + min(d[i-1][j], d[i][j-1], d[i-1][j-1])

print(d[len(s1)][len(s2)])