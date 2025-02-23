# 우측 - 좌측 >= M 이면서 가장 작아야 함.
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

if n == 1:
    print(0)
elif n == 2:
    diff = arr[1] - arr[0]
    if diff >= m:
        print(diff)
    else:
        print(0)
else:
    left = 0
    right = 0
    result = int(2e9) + 1
    while True:
        if right == n or left == n:
            break
        
        diff = arr[right] - arr[left]
        if diff < m:
            right += 1
        else:
            result = min(result, diff)
            left += 1
            
    print(result)