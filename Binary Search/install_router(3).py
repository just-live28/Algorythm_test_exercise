# 구하는 것 : 공유 사이의 거리
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()

def count_router(array, interval):
    count = 1
    prev = array[0]
    for i in array:
        if i - prev >= interval:
           count += 1
           prev = i
    
    return count
             
left = 1
right = houses[-1] - houses[0]

result = 0
while (left <= right):
    mid = (left + right) // 2
    
    if count_router(houses, mid) < c:
        right = mid - 1
    else:
        result = mid
        left = mid + 1

print(result)