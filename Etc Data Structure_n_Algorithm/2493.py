n = int(input())
towers = list(map(int, input().split()))
stack = []
stack.append((0, 100000001))

for i in range(1, n+1):
    h = towers[i-1]
    
    while stack[-1][1] < h:
        stack.pop()
    
    print(stack[-1][0], end=' ')
    stack.append((i, h))