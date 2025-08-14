from itertools import permutations
INF = int(1e9)

n = int(input())
arr = list(map(int, input().split()))
plus, minus, product, divide = map(int, input().split())
opers = []
opers.extend(['+'] * plus)
opers.extend(['-'] * minus)
opers.extend(['*'] * product)
opers.extend(['/'] * divide)

max_result = -INF
min_result = INF
for each_opers in permutations(opers, n-1):
    cur = arr[0]
    for i in range(1, n):
        cur_oper = each_opers[i-1]
        if cur_oper == '+':
            cur += arr[i]
        elif cur_oper == '-':
            cur -= arr[i]
        elif cur_oper == '*':
            cur *= arr[i]
        else:
            if cur >= 0:
                cur //= arr[i]
            else:
                cur *= (-1)
                cur //= arr[i]
                cur *= (-1)
                
    max_result = max(max_result, cur)
    min_result = min(min_result, cur)

print(max_result)
print(min_result)