import sys
input = sys.stdin.readline

n = int(input())
numbers = [0] * 10001
for _ in range(n):
    numbers[int(input())] += 1

for i in range(1, 10001):
    if numbers[i] > 0:
        for j in range(numbers[i]):
            print(i)