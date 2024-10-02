n = int(input())
INF = int(1e9)

d = [INF] * 30001
d[0], d[1] = 0, 0

# d[n-1] = min(d[n-1], d[n] + 1)

def to_one(n):
    d[n] = d[n-1] + 1
    
    if n % 2 == 0:
        d[n] = min(d[n], d[n // 2] + 1)
    elif n % 3 == 0:
        d[n] = min(d[n], d[n // 3] + 1)
    elif n % 5 == 0:
        d[n] = min(d[n], d[n // 5] + 1)

for i in range(1, n+1):
    to_one(i)

print(d[n])