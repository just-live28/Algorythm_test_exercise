import heapq
import sys
input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n):
    s, t = map(int, input().split())
    classes.append((s, t))
classes.sort()
            
rooms = []
heapq.heappush(rooms, 0)
for i in range(n):
    if classes[i][0] >= rooms[0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, classes[i][1])

print(len(rooms))