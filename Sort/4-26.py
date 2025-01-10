import sys
input = sys.stdin.readline
import heapq

n = int(input())

cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

count = 0
while cards:
    one = heapq.heappop(cards)
    
    if not cards:
        break
    
    two = heapq.heappop(cards)
    
    shake = one + two
    count += shake
    heapq.heappush(cards, shake)
        
print(count)