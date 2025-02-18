import sys
input = sys.stdin.readline

n = int(input())
freq = [0] * 2000001
for _ in range(n):
    freq[int(input()) + 1000000] += 1

for i in range(len(freq)):
    for j in range(freq[i]):
        print(i - 1000000)