def binary_search(array, target, left, right):
    if left > right:
        return None
    
    mid = (left + right) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid+1, right)
    elif array[mid] > target:
        return binary_search(array, target, left, mid-1)

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

m = int(input())
finds = list(map(int, input().split()))

for i in range(m):
    if binary_search(numbers, finds[i], 0, n-1) == None:
        print(0)
    else:
        print(1)