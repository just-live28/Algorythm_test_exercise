def binary_search(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
finds = list(map(int, input().split()))
for find in finds:
    if binary_search(arr, find, 0, n-1) != None:
        print(1)
    else:
        print(0)