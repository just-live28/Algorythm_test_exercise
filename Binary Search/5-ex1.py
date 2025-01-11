# dictionary 이용하기
# n = int(input())

# parts = {}
# for part in list(map(int, input().split())):
#     parts[part] = True

# m = int(input())
# for find in list(map(int, input().split())):
#     if find in parts:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

n = int(input())
parts = list(map(int, input().split()))

def binary_search(arr, target, left, right):
    if left > right:
        return None
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    else:
        if arr[mid] > target:
            return binary_search(arr, target, left, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, right)

m = int(input())
finds = list(map(int, input().split()))
for i in range(m):
    if binary_search(parts, finds[i], 0, n-1) == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')