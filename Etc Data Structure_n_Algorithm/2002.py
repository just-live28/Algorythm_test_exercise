from collections import deque

n = int(input())
start_orders = []
for _ in range(n):
    start_orders.append(input())
end_orders = []
for _ in range(n):
    end_orders.append(input())

idx = 0
violate = 0
visited = set()
q = deque(end_orders)
while q:
    now = q.popleft()
    visited.add(now)

    if now == start_orders[idx]:
        idx += 1
        while idx < n and start_orders[idx] in visited:
            idx += 1
    else:
        violate += 1

print(violate)