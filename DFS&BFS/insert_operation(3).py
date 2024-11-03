from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
array = list(map(int, input().split()))
oper = ['+', '-', '*', '/']

opers = []
for i in range(4):
    for j in range(array[i]):
        opers.append(oper[i])

max_result = -int(1e9)
min_result = int(1e9)

for symbols in set(permutations(opers, len(opers))):
    result = numbers[0]
    for i in range(len(opers)):
        if symbols[i] == '+':
            result += numbers[i+1]
        elif symbols[i] == '-':
            result -= numbers[i+1]
        elif symbols[i] == '*':
            result *= numbers[i+1]
        elif symbols[i] == '/':
            if result < 0 and numbers[i+1] > 0:
                result *= (-1)
                result //= numbers[i+1]
                result *= (-1)
            else:
                result //= numbers[i+1]
    
    if result > max_result:
        max_result = result
    
    if result < min_result:
        min_result = result

print(max_result)
print(min_result)