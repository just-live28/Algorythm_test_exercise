
# d[n] = max(d[n-1] + arr[n], d[n-2] + arr[n]) 
# 단, count가 2인 경우, d[n] = d[n-2] + arr[n]

# step(0, 0)
# n이 n을 넘어가면 n인 경우에만 max_score 갱신 후 return
import sys
input = sys.stdin.readline

n = int(input())
arr = [0]
for i in range(1, n+1):
    arr.append(int(input()))

d = [0] * 301

if n >= 1:
    d[1] = arr[1]
if n >= 2:
    d[2] = arr[1] + arr[2]
if n >= 3:
    for i in range(3, n+1):
        d[i] = max(d[i-2] + arr[i], d[i-3] + arr[i-1] + arr[i])

print(d[n])