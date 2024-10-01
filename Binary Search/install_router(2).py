# 거리가 parammetric search : length
# 첫번째 집에 설치를 한다. -> length만큼 더한 곳에 집이 있으면 설치 / 없으면 다음 집에 설치
# 반복해서 설치한 후 --> 개수가 c개보다 적으면(비합리) length를 줄인다.
# 개수가 c개보다 많으면 result에 할당 후 length를 늘린다.

import sys
input = sys.stdin.readline

n, c = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))

array.sort()

start = 1
end = array[-1] - array[0]

result = 0
while(start <= end):
    mid = (start + end) // 2
    
    count = 1
    prev = array[0]
    for i in range(1, n):
        difference = array[i] - prev
        # 거리를 만족하면
        if difference >= mid:
            count += 1
            prev = array[i]
    
    if count < c:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)