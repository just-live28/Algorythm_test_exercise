import sys
input = sys.stdin.readline

n, m = map(int, input().split())
results = []
for _ in range(n):
    results.append(min(map(int, input().split())))

print(max(results))