import sys
input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))
cards.sort()
cards.append(2**62 + 1)

max_count = 0
target_number = 0
prev = cards[0]
count = 1
for i in range(1, n+1):
    if cards[i] == prev:
        count += 1
    else:
        if count > max_count:
            target_number = prev
            max_count = count
        prev = cards[i]
        count = 1
    
print(target_number)