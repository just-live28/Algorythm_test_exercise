import sys
input = sys.stdin.readline

n, h = map(int, input().split())

crash = [0] * h
for i in range(n):
    size = int(input())
    if i % 2 == 0:
        crash[0] += 1
        crash[size] -= 1
    else:
        crash[h - size] += 1

for i in range(1, h):
    crash[i] += crash[i-1]

min_crash = n+1
count = 0
for each in crash:
    if each < min_crash:
        min_crash = each
        count = 1
    elif each == min_crash:
        count += 1

print(min_crash, count)