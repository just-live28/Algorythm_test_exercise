# 연산자 우선순위 무시
# 나눗셈 : //
# 음수 나눗셈 : 양수로 전환 -> // -> 음수로 전환
from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
plus, minus, multiple, division = map(int, input().split())

opers = []
opers.extend(['+'] * plus)
opers.extend(['-'] * minus)
opers.extend(['*'] * multiple)
opers.extend(['/'] * division)

max_result = -int(1e9) - 1
min_result = int(1e9) + 1
for each in permutations(opers, n-1):
    result = arr[0]
    for i in range(1, n):
        if each[i-1] == '+':
            result += arr[i]
        elif each[i-1] == '-':
            result -= arr[i]
        elif each[i-1] == '*':
            result *= arr[i]
        else:
            if result >= 0:
                result //= arr[i]
            else:
                result *= (-1)
                result //= arr[i]
                result *= (-1)
    max_result = max(max_result, result)
    min_result = min(min_result, result)
    
print(max_result)
print(min_result)