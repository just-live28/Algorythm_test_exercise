import sys
input = sys.stdin.readline

# 끝나는 시간이 빠른 회의대로 정렬하고, 끝날 때마다 다음 회의를 집어넣으면 된다.

n = int(input())

arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key = lambda x : (x[1], x[0]))

count = 0
prev = 0
for i in range(n):
    start, end = arr[i]
    
    if start >= prev:
        count += 1
        prev = end

print(count)