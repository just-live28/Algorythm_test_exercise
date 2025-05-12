n = int(input())
arr = [()]
for _ in range(n):
    st, en, people = map(int, input().split())
    arr.append((st, en, people))

d = [[0] * 2 for _ in range(n+1)]
for i in range(1, n+1):
    d[i][0] = max(d[i-1][0], d[i-1][1])
    d[i][1] = d[i-1][0] + arr[i][2]
    
print(max(d[n]))