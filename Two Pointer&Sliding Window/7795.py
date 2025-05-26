t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    arr_a.sort()
    arr_b.sort()

    rp = 0
    count = 0
    for i in arr_a:
        while rp < m and i > arr_b[rp]:
            rp += 1
        count += rp
    print(count)