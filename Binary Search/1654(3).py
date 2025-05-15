k, n = map(int, input().split())

arr = []
for _ in range(k):
    arr.append(int(input()))
arr.sort()    

def cal_lans(split_length):
    count = 0
    for lan in arr:
        if lan >= split_length:
            count += lan // split_length
    
    return count

min_length = 1
max_length = arr[-1]
result = 0
while min_length <= max_length:
    mid = (min_length + max_length) // 2
    
    each_result = cal_lans(mid)
    if each_result >= n:
        result = mid
        min_length = mid + 1
    else:
        max_length = mid - 1

print(result)