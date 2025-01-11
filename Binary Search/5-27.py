# 계수 정렬 불가능 (최대 최소 차이가 100만 초과)
# 정렬된 배열에서의 탐색 -> 이진 탐색이 유리
# 해시 테이블은?

# dictionary 활용
# numbers = {}
# for num in map(int, input().split()):
#     if num in numbers:
#         numbers[num] += 1
#     else:
#         numbers[num] = 1

# if x in numbers:
#     print(numbers[x])
# else:
#     print(-1)
# 시간 복잡도 O(logN)을 만족할 수 있는가? 배열을 한 번 순회해야 하므로 O(N)이기에 적절하지 않다.
# 그렇다면 이진 탐색을 이용하는 것이 가장 합리적이다. 왼쪽 target을 구하는 데 O(logN), 오른쪽에 O(logN)이 걸리므로, 약 O(logN)에 문제를 해결할 수 있다.

N, x = map(int, input().split())
numbers = list(map(int, input().split()))

def binary_min_search(arr, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            result = mid
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            
    if result == 0:
        return None
    else:
        return result

def binary_max_search(arr, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            result = mid
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    if result == 0:
        return None
    else:
        return result

max_index = binary_max_search(numbers, x, 0, N-1)
if max_index == None:
    print(-1)
else:
    min_index = binary_min_search(numbers, x, 0, N-1)
    print(max_index - min_index + 1)