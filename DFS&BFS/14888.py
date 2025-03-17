from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
plus, minus, product, divide = map(int, input().split())

opers = []
opers.extend(['+'] * plus) if plus > 0 else None
opers.extend(['-'] * minus) if minus > 0 else None
opers.extend(['*'] * product) if product > 0 else None
opers.extend(['/'] * divide) if divide > 0 else None

max_result, min_result = -int(1e9)-1, int(1e9)+1
for each_opers in permutations(opers, n-1):
    result = arr[0]
    for i in range(1, n):
        if each_opers[i-1] == '+':
            result += arr[i]
        elif each_opers[i-1] == '-':
            result -= arr[i]
        elif each_opers[i-1] == '*':
            result *= arr[i]
        else:
            if result < 0:
                result *= -1
                result //= arr[i]
                result *= -1
            else:
                result //= arr[i]
    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)