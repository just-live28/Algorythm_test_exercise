tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    arr_a.sort()
    arr_b.sort()

    total = 0
    bidx = 0
    for a in arr_a:
        if bidx == len(arr_b):
            total += len(arr_b)
            continue
        while a > arr_b[bidx]:
            bidx += 1
            if bidx == len(arr_b):
                break
        total += bidx
    print(total)