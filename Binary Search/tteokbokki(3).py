# n 떡 개수 m 요청 길이
n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

def calulate_length(arr, split_length):
    return sum([x - split_length for x  in arr if x > split_length])

start, end = array[0], array[-1]
result = 0
while (start <= end):
    mid = (start + end) // 2
    
    if calulate_length(array, mid) < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)