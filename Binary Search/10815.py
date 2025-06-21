import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
finds = list(map(int, input().split()))

def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for find in finds:
    print(binary_search(arr, 0, n-1, find), end=' ')