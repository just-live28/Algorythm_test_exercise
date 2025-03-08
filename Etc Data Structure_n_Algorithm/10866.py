# 덱
# 1. q.popleft() [뽑아내기]
# 인덱스 증가

# 2. q.append(q.popleft())
# 인덱스 증가

# 3. q.appendleft(q.pop())
# 인덱스 감소

# 현재 큐 길이의 반절에 대해 해당 수의 index가 왼쪽 부분이면 2번연산(while), 오른쪽 부분이면 3번연산(while)
# 해당 수를 제일 왼쪽에 위치시킨 후 뽑아낸다. 이후 큐 길이 - 1

from collections import deque

n, m = map(int, input().split())
q = deque([x for x in range(1, n+1)])
order = list(map(int, input().split()))

count = 0
for i in range(m):
    half = n // 2
    idx = q.index(order[i])
    
    if idx <= half:
        while q[0] != order[i]:
            q.append(q.popleft())
            count += 1
    else:
        while q[0] != order[i]:
            q.appendleft(q.pop())
            count += 1
    q.popleft()
    n -= 1

print(count)