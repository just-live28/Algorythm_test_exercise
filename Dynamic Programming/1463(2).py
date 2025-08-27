n = int(input())
d = [0] * (n+1)
d[1] = 0

for i in range(2, n+1):
    count = int(1e9)
    if i % 2 == 0:
        count = min(count, d[i//2] + 1)
    
    if i % 3 == 0:
        count = min(count, d[i//3] + 1)
    
    d[i] = min(d[i-1] + 1, count)

print(d[n])