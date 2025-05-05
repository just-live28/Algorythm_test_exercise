import heapq

n = int(input())
classes = []
for _ in range(n):
    num, st, en = map(int, input().split())
    classes.append((st, en))
classes.sort(key = lambda x: (x[0], x[1]))

q = []
heapq.heappush(q, 0)
result = 1
for st, en in classes:
    if st >= q[0]:
        heapq.heappop(q)
    else:
        result += 1
    heapq.heappush(q, en)

print(result)