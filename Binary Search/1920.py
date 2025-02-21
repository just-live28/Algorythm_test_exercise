from bisect import bisect_left

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
m = int(input())
for find in map(int, input().split()):
    print(binary_search(numbers, find, 0, n-1))