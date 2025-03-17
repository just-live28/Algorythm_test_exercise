import sys
input = sys.stdin.readline

def merge(st, en):
    mid = (st + en) // 2
    idx1 = st
    idx2 = mid
    for i in range(st, en):
        if idx1 == mid:
            tmp[i] = arr[idx2]
            idx2 += 1
        elif idx2 == en:
            tmp[i] = arr[idx1]
            idx1 += 1
        else:
            if arr[idx1] <= arr[idx2]:
                tmp[i] = arr[idx1]
                idx1 += 1
            else:
                tmp[i] = arr[idx2]
                idx2 += 1
    for i in range(st, en):
        arr[i] = tmp[i]

def merge_sort(st, en):
    if en == st + 1:
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