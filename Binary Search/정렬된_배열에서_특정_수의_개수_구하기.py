from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split()))

# result = bisect_right(arr, x) - bisect_left(arr, x)
# if not result:
#     print(-1)
# else:
#     print(result)

def first(array, target, st, en):
    if st > en:
        return None
    
    mid = (st + en) // 2
    
    # mid가 0이거나 arr[mid-1]이 target보다 작으면서, arr[mid]가 target일때 mid 반환
    if (mid == 0 or arr[mid-1] < target) and array[mid] == target:
        return mid
    # arr[mid]가 target보다 같거나 클 경우, 왼쪽으로
    elif array[mid] >= target:
        return first(array, target, st, mid-1)
    else:
        return first(array, target, mid+1, en)

def last(array, target, st, en):
    if st > en:
        return None
    
    mid = (st + en) // 2
    
    if (mid == n-1 or arr[mid+1] > target) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, st, mid-1)
    else:
        return last(array, target, mid+1, en)

start_idx = first(arr, x, 0, n-1)
if not start_idx:
    print(-1)
else:
    end_idx = last(arr, x, 0, n-1)
    print(end_idx - start_idx + 1)