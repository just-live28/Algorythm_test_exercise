n = int(input())
arr_s = []
arr_b = []
for _ in range(n):
    s, b = map(int, input().split())
    arr_s.append(s)
    arr_b.append(b)

min_diff = int(1e9)
for each in range(1, 2**n):
    cur_s = 0
    cur_b = 0
    for i in range(n):
        if (each >> i) % 2 == 1:
            if cur_s:
                cur_s *= arr_s[i]
            else:
                cur_s = arr_s[i]
            
            cur_b += arr_b[i]

    min_diff = min(min_diff, abs(cur_s - cur_b))

print(min_diff)