import sys
input = sys.stdin.readline

n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))
ropes.sort()

result = 0
for i in range(1, n+1):
    result = max(result, ropes[n-i] * i)

print(result)