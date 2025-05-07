n = int(input())
arr = list(map(int, input().split()))
arr.sort()

min_diff = 3 * int(1e9) + 1
result_arr = []
early_return = False
for i in range(n):
    if early_return == True:
        break
    
    fixed = arr[i]
    lp = 0
    rp = n-1
    
    if lp == i:
        lp += 1
    elif rp == i:
        rp -= 1
    
    while (lp != rp):
        each_sum = fixed + arr[lp] + arr[rp]
        
        if abs(each_sum) < min_diff:
            min_diff = abs(each_sum)
            result_arr = [fixed, arr[lp], arr[rp]]
            if each_sum == 0:
                early_return = True
                break
        
        if each_sum < 0:
            lp += 1
            if lp == i:
                lp += 1
        else:
            rp -= 1
            if rp == i:
                rp -= 1

result_arr.sort()
print(*result_arr)