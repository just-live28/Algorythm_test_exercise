def mergy_sort(st, en):
    if en - st == 1:
        return
    
    mid = (st + en) // 2
    mergy_sort(st, mid)
    mergy_sort(mid, en)
    
    pl, pr = st, mid
    for i in range(st, en):
        if pl == mid:
            temp[i] = arr[pr]
            pr += 1
        elif pr == en:
            temp[i] = arr[pl]
            pl += 1
        else:
            if arr[pl] <= arr[pr]:
                temp[i] = arr[pl]
                pl += 1
            else:
                temp[i] = arr[pr]
                pr += 1
    
    for i in range(st, en):
        arr[i] = temp[i]

MX = 1000000
arr = [0] * MX
temp = [0] * MX

n = int(input())
for i in range(n):
    arr[i] = int(input())
mergy_sort(0, n)
for i in range(n):
    print(arr[i], end=' ')
print()