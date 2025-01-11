# 선형 탐색보다 빠르게 동작해야 함.
# 정렬되어 있는 배열에서 O(logN) 으로 목표값을 찾아낼 수 있는 방법은 이진 탐색.
# 중간 인덱스(mid)를 구하고 arr[mid] 의 값이 mid보다 작다면 오른쪽으로, mid보다 크다면 왼쪽으로 가야 한다.

def binary_search(arr, left, right):
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return None

N = int(input())
numbers = list(map(int, input().split()))

result = binary_search(numbers, 0, N-1)
if result == None:
    print(-1)
else:
    print(result)