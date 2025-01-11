# 수직선 위 집 N개 / 집 좌표 중복 x ( x는 1~ 10억 )
# 한 집 한 공유기, 가장 인접한 공유기 사이 거리를 가능한 크게 
# 공유기 사이의 최대 거리 출력 -> 이진 탐색을 이용한 parametric search 유형

# 가장 인접한 공유기 사이 거리가 중간값(mid)가 된다.
# 집을 순회하면서 집이 mid 이상 떨어져 있어야 설치 개수를 올린다.
# 설치 개수가 c보다 더 많으면 기록 후, 거리를 늘린다. (설치가 가능하다는 뜻이므로)
# 설치 개수가 c보다 더 적으면 거리를 줄인다. (너무 큰 값이라는 뜻이므로)
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()

def binary_search(arr, target, left, right):
    result = 0
    while left <= right:
        mid = (left + right) // 2
        
        count = 1
        prev = arr[0]
        for i in range(1, len(arr)):
            if arr[i] - prev >= mid:
                count += 1
                prev = arr[i]
        
        if count >= target:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

print(binary_search(houses, c, 1, houses[-1] - houses[0]))