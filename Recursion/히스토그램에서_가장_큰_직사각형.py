def get_max_area(arr, st, en):
    if st > en or not arr:
        return 0
    if st == en:
        return arr[st]
    
    mid = (st + en) // 2
    pl, pr = mid, mid
    max_area = arr[mid]
    min_height = arr[mid]
    while True:
        if pl == st and pr == en:
            break
        elif pl == st:
            pr += 1
            
        elif pr == en:
            pl -= 1
        else:
            if arr[pl-1] > arr[pr+1]:
                pl -= 1
            else:
                pr += 1
        min_height = min(min_height, arr[pr], arr[pl])
        max_area = max(max_area, (pr - pl + 1) * min_height)
    
    return max(get_max_area(arr, st, mid-1), get_max_area(arr, mid + 1, en), max_area)

while True:
    line = list(map(int, input().split()))
    
    if line[0] == 0:
        break
    
    n = line[0]
    heights = line[1:]
    
    print(get_max_area(heights, 0, n-1))