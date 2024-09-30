import sys
input = sys.stdin.readline
import heapq

n = int(input())

q = []

for _ in range(n):
    heapq.heappush(q, int(input()))

result = 0
while(True):
    min_card = heapq.heappop(q)
    
    if len(q) == 0:
        break
    
    second_card = heapq.heappop(q)
    
    shake = min_card + second_card
    result += shake
    
    heapq.heappush(q, shake)

print(result)