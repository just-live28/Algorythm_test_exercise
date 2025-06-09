import copy
INF = int(1e9)

n = int(input())
first_off_cur = [int(x) for x in input()]
first_on_cur = copy.deepcopy(first_off_cur)
target = [int(x) for x in input()]

if first_on_cur[0] == 0:
    first_on_cur[0] = 1
else:
    first_on_cur[0] = 0
if first_on_cur[1] == 0:
    first_on_cur[1] = 1
else:
    first_on_cur[1] = 0

def make_target_bulb(arr, init_count):
    count = init_count
    for i in range(1, n):
        if arr[i-1] != target[i-1]:
            count += 1
            if arr[i-1] == 0:
                arr[i-1] = 1
            else:
                arr[i-1] = 0
            if arr[i] == 0:
                arr[i] = 1
            else:
                arr[i] = 0
            if i < n-1:
                if arr[i+1] == 0:
                    arr[i+1] = 1
                else:
                    arr[i+1] = 0
    
    if arr == target:
        return count
    else:
        return INF

first_off_count = make_target_bulb(first_off_cur, 0)
first_on_count = make_target_bulb(first_on_cur, 1)

if first_off_count == INF and first_on_count == INF:
    print(-1)
else:
    print(min(first_off_count, first_on_count))