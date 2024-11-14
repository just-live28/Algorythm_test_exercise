# t 상담시간 p 페이

n = int(input())

times = []
pays = []
for i in range(n):
    t, p = map(int, input().split())
    times.append(t)
    pays.append(p)

d = [0] * (n+1)

max_value = 0
for i in range(n-1, -1, -1):
    if i + times[i] <= n:
        d[i] = max(max_value, pays[i] + d[i + times[i]])
        max_value = d[i]
    else:
        d[i] = max_value

print(max(d))