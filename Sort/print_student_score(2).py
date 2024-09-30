import sys
input = sys.stdin.readline

n = int(input())

array = []

for _ in range(n):
    name, score = input().split()
    
    array.append((name, int(score)))

array.sort(key = lambda x : x[1])

for i in array:
    print(i[0], end=' ')