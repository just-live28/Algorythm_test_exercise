# n 행 m 열
n, m = map(int, input().split())

min_cards = []
for _ in range(n):
    line = list(map(int, input().split()))
    
    min_cards.append(min(line))

print(max(min_cards))