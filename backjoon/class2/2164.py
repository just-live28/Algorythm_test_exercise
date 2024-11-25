from collections import deque

n = int(input())

q = deque()

for i in range(1, n+1):
    q.append(i)
    
while True:
    num1 = q.popleft()
    
    if len(q) == 0:
        print(num1)
        break
    
    num2 = q.popleft()
    q.append(num2)