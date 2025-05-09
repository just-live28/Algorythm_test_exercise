import sys
input = sys.stdin.readline

k, n = map(int, input().split())

arr = []
for _ in range(k):
    arr.append(int(input()))
arr.sort()

def count_lan(array, split_length):
    count = 0
    for length in array:
        count += length // split_length
    
    return count

min_length = 1
max_length = arr[-1]
result = 0
while (min_length <= max_length):
    mid = (min_length + max_length) // 2
    
    if count_lan(arr, mid) >= n:
        result = mid
        min_length = mid + 1
    else:
        max_length = mid - 1
    
print(result)