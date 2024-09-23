numbers = list(map(int, input()))

# 합계가 0혹은 1일 때 -> 모든 수에 대해 +가 이득
# 합계가 1을 넘을 때 -> 0, 1은 더하는게 이득, 2 이상은 곱하는게 이득

total = 0

for num in numbers:
    if total <= 1:
        total += num
    else:
        if num < 2:
            total += num
        else:
            total *= num

print(total)
        

