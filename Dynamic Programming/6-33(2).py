N = int(input())

times = []
pays = []

for _ in range(N):
    t, p = map(int, input().split())
    times.append(t)
    pays.append(p)

d = [0] * (N+1)

max_earn = 0
for i in range(N-1, -1, -1):
    duration = i + times[i]
    
    if duration <= N:
        d[i] = max(pays[i] + d[duration], max_earn)
        max_earn = d[i]
    else:
        d[i] = max_earn

print(d[0])