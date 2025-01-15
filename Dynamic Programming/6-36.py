a = input()
b = input()

d = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    d[i][0] = i

for j in range(1, len(b) + 1):
    d[0][j] = j
    
# 문자열 접근 시 -1 해줘야 함.(0-side)
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i-1] == b[j-1]:
            d[i][j] = d[i-1][j-1]
        else:
            d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1

print(d[len(a)][len(b)])