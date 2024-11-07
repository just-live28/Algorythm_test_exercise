import sys
input = sys.stdin.readline

array = [[] for _ in range(101)]

n = int(input())

for _ in range(n):
    name, score = input().split()
    
    array[int(score)].append(name)

for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end=' ')