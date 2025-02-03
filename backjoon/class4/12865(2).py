n, k = map(int, input().split())

d = [0] * (k+1)

for _ in range(n):
    w, v = map(int, input().split())
    
    for i in range(k, w-1, -1):
        d[i] = max(d[i], d[i-w] + v)

print(d[k])