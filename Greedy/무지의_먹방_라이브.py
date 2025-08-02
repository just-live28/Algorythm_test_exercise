def solution(food_times, k):
    n = len(food_times)
    sorted_arr = []
    for i in range(1, n+1):
        sorted_arr.append((food_times[i-1], i))
    sorted_arr.sort(key = lambda x : -x[0])
    
    total = 0
    cur = 0
    while sorted_arr and total + (sorted_arr[-1][0] - cur) * n <= k:
        time, _ = sorted_arr.pop()
        total += (time - cur) * n
        cur = time
        n -= 1
    
    if not sorted_arr:
        return -1
    else:
        sorted_arr.sort(key = lambda x : x[1])
        idx = (k - total) % n
        return sorted_arr[idx][1]