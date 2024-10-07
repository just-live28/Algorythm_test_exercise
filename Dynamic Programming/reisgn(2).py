# 파이프라인처럼 이어져있다 -> 뒤에서부터 보는 DP문제
# d[i] = max(d[i + t[i]] + p[i], max_value)
# i일부터 시작해 상담을 끝내고 받는 돈 + 그 일자의 최대 수익 / i일부터 시작한 종합적인 최대 수익

import sys
input = sys.stdin.readline

n = int(input())

t = []
p = []
d = [0] * (n+1)

for _ in range(n):
    time, cost = map(int, input().split())
    t.append(time)
    p.append(cost)

max_value = 0
for i in range(n-1, -1, -1):
    if i + t[i] <= n:
        d[i] = max(d[i + t[i]] + p[i], max_value)
        max_value = d[i]
    #벗어날 경우 그동안의 최대 수익이 총 최대 수익
    else:
        d[i] = max_value

print(max_value)