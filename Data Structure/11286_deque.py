import heapq

n = int(input())

q = []
for _ in range(n):
    cmd = int(input())
    
    if cmd != 0:
        if cmd > 0:
            heapq.heappush(q, (abs(cmd), 1))
        else:
            heapq.heappush(q, (abs(cmd), 0))
    else:
        if not q:
            print(0)
        else:
            num, sign = heapq.heappop(q)
            if sign == 1:
                print(num)
            else:
                print(-num)