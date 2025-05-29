import sys
from bisect import bisect_left
input = sys.stdin.readline

n, m = map(int, input().split())

names = []
arr = []
for _ in range(n):
    name, standard = input().split()
    names.append(name)
    arr.append(int(standard))

for _ in range(m):
    power = int(input())
    print(names[bisect_left(arr, power)])