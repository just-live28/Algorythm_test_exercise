import sys
input = sys.stdin.readline

n = int(input())

conventions = []
for _ in range(n):
    a, b = map(int, input().split())
    
    conventions.append((a, b))

conventions.sort(key = lambda x : (x[1], x[0]))

result = 0
prev = 0
for start, end in conventions:
    if start >= prev:
        result += 1
        prev = end
    else:
        continue

print(result)