import sys
import heapq
input = sys.stdin.readline

n = int(input())

cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

count = 0
while cards:
    min_card = heapq.heappop(cards)
    
    if not cards:
        break
    else:
        second_card = heapq.heappop(cards)
    
        shake = min_card + second_card
        
        count += shake
        heapq.heappush(cards, shake)
    
print(count)