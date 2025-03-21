# 큰 게 들어오면 이것보다 큰 게 나올때까지 작은 것들은 전부 나가리
# 작은게 들어오면 넣기
import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    bar = int(input())
    
    if not stack or stack[-1] > bar:
        stack.append(bar)
    elif stack[-1] == bar:
        continue
    else:
        while stack:
            if stack[-1] <= bar:
                stack.pop()
            else:
                break
        stack.append(bar)

print(len(stack))