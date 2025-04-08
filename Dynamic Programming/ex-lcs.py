str1 = 'ABCDEF'
str2 = 'GBCDFE'

# 최장 공통 문자열
# lcs = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]

# for i in range(1, len(str1)+1):
#     for j in range(1, len(str2)+1):
#         if str1[i-1] == str2[j-1]:
#             lcs[i][j] = lcs[i-1][j-1] + 1
#         else:
#             lcs[i][j] = 0

# print(max([max(x) for x in lcs]))


#최장 공통 부분수열(이것이 주로 lcs라 불림)
lcs = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i-1] == str2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs)

i, j = len(str1), len(str2)
result = []
while i > 0 and j > 0:
    if str1[i-1] == str2[j-1]:
        result.append(str1[i-1])
        i -= 1
        j -= 1
    elif lcs[i-1][j] >= lcs[i][j-1]:
        i -= 1
    else:
        j -= 1

print(''.join(reversed(result)))