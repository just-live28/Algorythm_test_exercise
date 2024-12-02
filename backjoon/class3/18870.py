import heapq

n = int(input())

q = []
idx = 0
min_num = int(1e9)
for i in map(int, input().split()):
    heapq.heappush(q, [i, idx])
    min_num = min(i, min_num)
    idx += 1

label = 0
result = []
prev = min_num
while q:
    now_num, now_idx = heapq.heappop(q)
    
    if now_num != prev:
        label += 1
    
    result.append((label, now_idx))
    prev = now_num

result.sort(key = lambda x : x[1])
for num, _ in result:
    print(num, end=' ')