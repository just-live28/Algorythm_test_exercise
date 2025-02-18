import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
temp = [0] * len(arr)
    
def merge_sort(start, end):
    if end == start + 1:
        return
    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid, end)
    merge(start, end)

def merge(start, end):
    mid = (start + end) // 2
    lidx = start
    ridx = mid
    for i in range(start, end):
        if lidx == mid:
            temp[i] = arr[ridx]
            ridx += 1
        elif ridx == end:
            temp[i] = arr[lidx]
            lidx += 1
        elif arr[lidx] <= arr[ridx]:
            temp[i] = arr[lidx]
            lidx += 1
        else:
            temp[i] = arr[ridx]
            ridx += 1
    for i in range(start, end):
        arr[i] = temp[i]

merge_sort(0, n)
for i in arr:
    print(i)