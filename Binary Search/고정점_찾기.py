# 고정점: 값이 인덱스와 동일한 원소
# 중간 idx의 값이 더 큰 경우 -> 왼쪽 배열로
# 중간 idx의 값이 더 작은 경우 -> 오른쪽 배열로

n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n-1
result = -1
while left <= right:
    mid = (left + right) // 2

    if arr[mid] == mid:
        result = mid
        break
    elif mid > arr[mid]:
        left = mid + 1
    elif mid < arr[mid]:
        right = mid - 1

print(result)