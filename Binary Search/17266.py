import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))

min_h = 1
max_h = n
result = 0
while min_h <= max_h:
    mid = (min_h + max_h) // 2

    covers = [(0,0)]
    for x in arr:
        st = max(0, x - mid)
        en = min(n, x + mid)
        covers.append((st, en))
    covers.append((n, n))

    enable = True
    for i in range(1, len(covers)):
        if covers[i][0] - covers[i-1][1] > 0:
            enable = False
            break

    if enable:
        result = mid
        max_h = mid - 1
    else:
        min_h = mid + 1

print(result)