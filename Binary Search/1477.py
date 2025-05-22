def cal_need_construct(rests, target_length):
    count = 0
    for rest in rests:
        if rest > target_length:
            count += (rest-1) // target_length

    return count

n, m, l = map(int, input().split())

if n > 0:
    arr = [0] + list(map(int, input().split()))
    arr.append(l)
    arr.sort()
else:
    arr = [0, l]

rests = []
for i in range(len(arr)-1):
    rests.append(arr[i+1] - arr[i])
rests.sort()

min_length = 1
max_length = rests[-1]
result = 0
while min_length <= max_length:
    mid = (min_length + max_length) // 2

    if cal_need_construct(rests, mid) <= m:
        result = mid
        max_length = mid - 1
    else:
        min_length = mid + 1
        
print(result)