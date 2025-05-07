INF = int(1e9)

n = int(input())
arr = [()]
for _ in range(n):
    r, g, b = map(int, input().split())
    arr.append((r, g, b))

def func(first_color):
    d = [[INF] * 3 for _ in range(n+1)]
    d[1][first_color] = arr[1][first_color]
    
    for i in range(2, n+1):
        d[i][0] = min(d[i-1][1], d[i-1][2]) + arr[i][0]
        d[i][1] = min(d[i-1][0], d[i-1][2]) + arr[i][1]
        d[i][2] = min(d[i-1][1], d[i-1][0]) + arr[i][2]
    
    d[n][first_color] = INF

    return min(d[n])
    
print(min(func(0), func(1), func(2)))