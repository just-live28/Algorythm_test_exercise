from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
a, b, c, d = map(int, input().split())

opers = []
opers.extend(['+'] * a)
opers.extend(['-'] * b)
opers.extend(['*'] * c)
opers.extend(['/'] * d)

def calculate(opers, numbers):
    result = numbers[0]
    
    for i in range(len(opers)):
        if opers[i] == '+':
            result += numbers[i+1]
        elif opers[i] == '-':
            result -= numbers[i+1]
        elif opers[i] == '*':
            result *= numbers[i+1]
        else:
            if result < 0:
                result *= -1
                result //= numbers[i+1]
                result *= -1
            else:
                result //= numbers[i+1]
    return result

min_result = int(1e9)
max_result = -int(1e9)
for each_opers in set(permutations(opers, len(opers))):
    result = calculate(each_opers, numbers)
    min_result = min(min_result, result)
    max_result = max(max_result, result)

print(max_result)
print(min_result)