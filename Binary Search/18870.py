import copy

n = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(copy.deepcopy(arr))
sorted_distinct_arr = [sorted_arr[0]]
for num in sorted_arr[1:]:
    if num != sorted_distinct_arr[-1]:
        sorted_distinct_arr.append(num)
if sorted_arr[-1] != sorted_distinct_arr[-1]:
    sorted_distinct_arr.append(sorted_arr[-1])

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in arr:
    print(binary_search(sorted_distinct_arr, i, 0, len(sorted_distinct_arr) - 1), end=' ')