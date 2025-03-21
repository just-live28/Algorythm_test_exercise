# 1~N의 카드 1 위 ~ N 아래
# 위 카드 바닥 버리기
# 그다음 위 카드를 제일 아래에 옮기기
from collections import deque

n = int(input())
q = deque([x for x in range(n, 0, -1)])

while n > 1:
    q.pop()
    q.appendleft(q.pop())    
    n -= 1
    
print(q.popleft())