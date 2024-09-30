import sys
input = sys.stdin.readline

array = []

n = int(input())

for _ in range(n):
    array.append(int(input()))
    
array.sort(reverse=True)

for i in array:
    print(i, end=' ')