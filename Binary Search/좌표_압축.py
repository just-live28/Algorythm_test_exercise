n = int(input())
arr = list(map(int, input().split()))

# idx_arr = sorted(list(set(arr)))
# for find in arr:
#     print(bisect_left(idx_arr, find), end=' ')

def delete_duplicate(arr):
    temp = []
    prev = -1
    
    for i in arr:
        if i != prev:
            temp.append(i)
            prev = i
    
    return temp

def binary_search(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return None

idx_arr = delete_duplicate(sorted(arr))
for i in arr:
    print(binary_search(idx_arr, i, 0, len(idx_arr)-1), end=' ')