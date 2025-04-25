# 일단 rp 옮기기 -> 커지겠지
# 해당 수에 도달하면 count + 1 옮기기
# 해당 수보다 더 커지면 lp 옮기기
# 두 포인터가 끝에 도달하면 종료

n = int(input())
arr = [x for x in range(1, n+1)]
lp, rp = 0, 0

count = 0
cur_sum = arr[0]

if n == 1:
    print(1)
else:
    while True:
        if rp == n and lp == n:
            break
        
        if cur_sum > n or rp == n:
            cur_sum -= arr[lp]
            lp += 1
        else:
            rp += 1
            if rp < n:
                cur_sum += arr[rp]
        
        if cur_sum == n and (lp != n and rp != n):
            count += 1

    print(count)
