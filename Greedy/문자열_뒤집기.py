# 0 그룹, 1 그룹 다 세기
# 더 적은 그룹의 수가 답

line = input() + '2'
group_0 = 0
group_1 = 0
prev = line[0]
for i in range(1, len(line)):
    if line[i] != prev:
        if prev == '0':
            group_0 += 1
        else:
            group_1 += 1
    prev = line[i]

print(min(group_0, group_1))