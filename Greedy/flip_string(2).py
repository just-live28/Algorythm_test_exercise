# 0의 집합과 1의 집합을 산출
# 더 적은 쪽의 집합을 뒤집는다. (더 적은 쪽 집합의 개수가 곧 최소 행동 횟수)

numbers = list(map(int, input()))

group_0 = 0
group_1 = 0

prev = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] != prev:
        if prev == 0:
            group_0 += 1
        else:
            group_1 += 1
        prev = numbers[i]
    else:
        prev = numbers[i]

if numbers[-1] == 0:
    group_0 += 1
else:
    group_1 += 1

print(min(group_0, group_1))
        