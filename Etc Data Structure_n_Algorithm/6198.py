import sys
input = sys.stdin.readline

n = int(input())
buildings = []
for _ in range(n):
    buildings.append(int(input()))
buildings.reverse()

stack = [(0, int(1e9))]
views = [0] * (n+1)
for i in range(1, n+1):
    height = buildings[i-1]
    
    while height > stack[-1][1]:
        stack_idx, _ = stack.pop()
        views[i] += views[stack_idx] + 1
    stack.append((i, height))

print(sum(views))