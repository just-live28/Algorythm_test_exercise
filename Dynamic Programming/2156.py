import sys
input = sys.stdin.readline

n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

if n == 1:
    print(arr[1])
elif n == 2:
    print(arr[1] + arr[2])
else:
    d = [0] * (n+1)
    d[1] = arr[1]
    d[2] = arr[1] + arr[2]
    
    for i in range(3, n+1):
        d[i] = max(arr[i] + arr[i-1] + d[i-3], arr[i] + d[i-2], d[i-1])

    print(max(d))