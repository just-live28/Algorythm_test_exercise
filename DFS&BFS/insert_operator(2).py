from itertools import permutations

n = int(input())

numbers = list(map(int, input().split()))

# + - * /
line = list(map(int, input().split()))

oper_set = ['+', '-', '*', '/']
array = []
for i in range(4):
    for _ in range(line[i]):
        array.append(oper_set[i])

# 중복이 없는 순열

result = []
for opers in list(permutations(array, len(array))):
    total = numbers[0]
    
    for i in range(len(opers)):
        if opers[i] == '+':
            total += numbers[i+1]
        elif opers[i] == '-':
            total -= numbers[i+1]
        elif opers[i] == '*':
            total *= numbers[i+1]
        else:
            if total < 0:
                total = -(-total // numbers[i+1])
            else:
                total //= numbers[i+1]
    
    result.append(total)

result.sort()

print(result[-1])
print(result[0])