import heapq

n = int(input())
parent = [-1] * (n+1)
w_list = []
for _ in range(n):
    w_list.append(int(input()))

graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 0:
            continue
        graph[i].append((line[j], j+1))

tree = [False] * (n+1)
tree[0] = True
q = []
for i in range(1, n+1):
    heapq.heappush(q, (w_list[i-1], i))

result = 0
count = 0
while q:
    if count == n:
        break
    
    cost, now = heapq.heappop(q)
    
    if tree[now]:
        continue
    
    tree[now] = True
    count += 1
    result += cost
    
    for cost, b in graph[now]:
        if not tree[b]:
            heapq.heappush(q, (cost, b))

print(result)