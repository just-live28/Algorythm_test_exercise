n, t = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search(array, start, end, target):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, mid+1, end, target)
    else:
        return binary_search(array, start, mid-1, target)

result = binary_search(arr, 0, n, t)

if result == None:
    print("없음")
else:
    print(result + 1)