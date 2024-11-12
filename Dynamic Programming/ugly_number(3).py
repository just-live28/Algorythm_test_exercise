import heapq

n = int(input())

array = set()
array.add(1)

q = []
heapq.heappush(q, 2)
heapq.heappush(q, 3)
heapq.heappush(q, 5)

while q:
    num = heapq.heappop(q)
    
    array.add(num)
    
    if len(array) == n:
        break
    
    heapq.heappush(q, 2 * num)
    heapq.heappush(q, 3 * num)
    heapq.heappush(q, 5 * num)

array = sorted(array)
print(array[-1])