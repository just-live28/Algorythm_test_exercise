# 1~N 번의 사람들
# k 번째 사람을 제거
# 남은 원에서 또 k번째 사람을 제거

from collections import deque

n, k = map(int, input().split())
q = deque([x for x in range(1, n+1)])

count = 0
result = []
while len(result) < n:
    num = q.popleft()
    count += 1
    if count == k:
        result.append(num)
        count = 0
    else:
        q.append(num)

print('<', end='')
for i in range(n):
    if i != n-1:
        print(result[i], end=', ')
    else:
        print(result[i], end='')
        print('>')