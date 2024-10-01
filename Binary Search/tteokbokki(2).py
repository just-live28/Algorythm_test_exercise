n, m = map(int, input().split())

array = list(map(int, input().split()))

# 중간값으로 자를 높이를 설정한 후, 결과가 합리적이면 일단 result에 할당하고, 높이를 올린다.
# 결과가 비합리적이면 자를 높이를 내린다.

def get_tteok(array, target):
    new_array = [x - target for x in array if x > target]
    
    return sum(new_array)

min_height = 0
max_height = max(array)
result_height = 0
while(min_height <= max_height):
    mid = (min_height + max_height) // 2
    
    result = get_tteok(array, mid)
    
    if result >= m:
        result_height = mid
        min_height = mid + 1
    else:
        max_height = mid - 1

print(result_height)
    
