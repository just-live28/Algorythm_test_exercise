import sys
input = sys.stdin.readline

n = int(input())
times = [0]
pays = [0]
for _ in range(n):
    t, p = map(int, input().split())
    times.append(t)
    pays.append(p)

d = [0] * (n+2)
cur_earn = 0
for i in range(n, 0, -1):
    if i + times[i] - 1 <= n:
        earn = d[i+ times[i]] + pays[i]
        d[i] = max(cur_earn, earn)
        if d[i] == earn:
            cur_earn = earn
    else:
        d[i] = cur_earn

print(d[1])