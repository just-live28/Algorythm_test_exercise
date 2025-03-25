import sys
input = sys.stdin.readline

def merge(st, en):
    mid = (st + en) // 2
    pl, pr = st, mid
    
    for i in range(st, en):
        if pl == mid:
            tmp[i] = arr[pr]
            pr += 1
        elif pr == en:
            tmp[i] = arr[pl]
            pl += 1
        else:
            if arr[pr] <= arr[pl]:
                tmp[i] = arr[pr]
                pr += 1
            else:
                tmp[i] = arr[pl]
                pl += 1
    
    for i in range(st, en):
        arr[i] = tmp[i]
    
def merge_sort(st, en):
    if en - st == 1:
        return
    
    mid = (st + en) // 2
    merge_sort(st, mid)
    merge_sort(mid, en)
    merge(st, en)

n = int(input())
arr = [0] * 1000000
tmp = [0] * 1000000
for i in range(n):
    arr[i] = int(input())
merge_sort(0, n)
for i in range(n):
    print(arr[i])