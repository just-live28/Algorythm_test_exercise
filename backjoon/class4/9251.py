s1 = input()
s2 = input()

d = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i-1] == s2[j-1]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])

print(d[len(s1)][len(s2)])