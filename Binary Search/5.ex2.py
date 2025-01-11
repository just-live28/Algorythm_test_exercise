# H로 설정. H보다 긴 떡들의 잘린 나머지를 가져간다.
# 만족한다면, 값을 기록 후 H를 올린다
# 만족하지 않는다면, H를 내린다.
# 언제까지? H의 길이를 binary_search하여 left > right인 때까지



def calculate_ramains(arr, target, h):
    result = 0
    for i in arr:
        if i - h > 0:
            result += i - h
    
    if result >= target:
        return h
    else:
        return None

# n 떡 개수 m 요청 길이
n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
min_length = 0
max_length = max(arr)
while min_length <= max_length:
    mid = (min_length + max_length) // 2
    
    each_remains = calculate_ramains(arr, m, mid)
    if each_remains == None:
        max_length = mid - 1
    else:
        result = mid
        min_length = mid + 1

print(result)