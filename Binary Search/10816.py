n = int(input())
array = list(map(int, input().split()))
array.sort()

def lower_index(target, l):
    start = 0
    end = l
    while (start < end):
        mid = (start + end) // 2
        if array[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start

def upper_index(target, l):
    start = 0
    end = l
    while (start < end):
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid
        else:
            start = mid + 1
    return start

m = int(input())
for find in map(int, input().split()):
    print(upper_index(find, n) - lower_index(find, n), end=' ')