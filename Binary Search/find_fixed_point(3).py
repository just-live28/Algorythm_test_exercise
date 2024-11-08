# 값이 인덱스와 동일한 원소

def find_fixed_point(array, left, right):
    if left > right:
        return None
    
    mid = (left + right) // 2
    
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return find_fixed_point(array, left, mid-1)
    else:
        return find_fixed_point(array, mid+1, right)

n = int(input())
arr = list(map(int, input().split()))

result = find_fixed_point(arr, 0, n)

if result == None:
    print(-1)
else:
    print(result)