n = int(input())
arr = list(map(int, input().split()))
pl, pr = 0, n-1

sol1, sol2 = 0, 0
result = int(1e9) * 2 + 1
while pl < pr:
    sol_sum = arr[pl] + arr[pr]
    if abs(sol_sum) < result:
        result = abs(sol_sum)
        sol1, sol2 = arr[pl], arr[pr]
        
    if sol_sum == 0:
        break
    elif sol_sum < 0:
        pl += 1
    else:
        pr -= 1

print(sol1, sol2)