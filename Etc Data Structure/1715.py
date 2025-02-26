import heapq
import sys
input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))
heapq.heapify(cards)

result = 0
while cards:
    card1 = heapq.heappop(cards)
    if not cards:
        break
    card2 = heapq.heappop(cards)
    
    result += card1 + card2
    heapq.heappush(cards, card1 + card2)

print(result)    