n, x = map(int, input().split())
array = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while(start <= end):
        mid = (start + end) // 2
        
        result = None
        if array[mid] == target:
            result = mid
            end = mid - 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return result

left = binary_search(array, x, 0, n-1)

if left == None:
    print(-1)
else:
    if array[-1] == x:
        right = n - 1
    elif array[-1] > x:
        right = binary_search(array, x+1, 0, n-1) - 1

    print(left)
    print(right)
    print(right - left + 1)