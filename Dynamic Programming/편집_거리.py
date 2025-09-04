# 두 문자열 모두 1-sided하게 테이블 생성
# word1[i] == word2[j]라면, d[i][j] = d[i-1][j-1]
# 같지 않다면, d[i][j] = min(d[i][j-1], d[i-1][j], d[i-1][j-1]) + 1
## 즉, 직전의 삽입, 삭제, 교체 중 편집 거리가 가장 적은 쪽에 + 1
# 초깃값: 비교 안하고 그냥 계속 바꾸는 경우: 0행, 0열을 iterative하게 할당

word1 = input()
word2 = input()
n, m = len(word1), len(word2)

d = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    d[i][0] = i
for i in range(1, m+1):
    d[0][i] = i

for i in range(1, n+1):
    for j in range(1, m+1):
        if word2[j-1] == word1[i-1]:
            d[i][j] = d[i-1][j-1] 
        else:
            d[i][j] = min(d[i][j-1], d[i-1][j], d[i-1][j-1]) + 1

print(d[n][m])