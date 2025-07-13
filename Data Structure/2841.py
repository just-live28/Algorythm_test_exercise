import heapq
import sys
input = sys.stdin.readline

n, p = map(int, input().split())
q = [[] for _ in range(7)]

count = 0
for _ in range(n):
    line, pret = map(int, input().split())

    if not q[line]:
        count += 1
        heapq.heappush(q[line], -pret)
    else:
        if pret > -q[line][0]:
            count += 1
            heapq.heappush(q[line], -pret)
        elif pret == -q[line][0]:
            continue
        else:
            while q[line] and -q[line][0] > pret:
                count += 1
                heapq.heappop(q[line])
            
            if q[line] and -q[line][0] == pret:
                continue
            else:
                count += 1
                heapq.heappush(q[line], -pret)
    
print(count)