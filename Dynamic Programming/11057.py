# 오르막 수: 인접한 직전 수가 같거나 작은 수
# d[length][prev_last_num]: 직전 수가 prev_last_num인 length 길이의 오르막 수의 합
# prev_last_num: 0~9
# 정답: sum(d[n])
# 점화식: d[l][num] = sum(d[l-1][0] ~ d[l-1][num])

n = int(input())

d = [[0] * 10 for _ in range(n+1)]
for i in range(10):
    d[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        count = 0
        for k in range(j+1):
            count += d[i-1][k] % 10007
        d[i][j] = count % 10007

print(sum(d[n]) % 10007)